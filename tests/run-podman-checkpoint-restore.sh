#!/bin/bash

set -eux

ls -la

echo "Load additional SELinux policy for checkpointing"

# Add missing selinux policy
cat << EOF > criu.te

module criu 1.0;

require {
 type container_t;
 type container_var_lib_t;
 type sysctl_kernel_ns_last_pid_t;
 class file { append write };
}

allow container_t sysctl_kernel_ns_last_pid_t:file write;
allow container_t container_var_lib_t:file append;
EOF

cat criu.te

checkmodule -M -m criu.te -o criu.mod
semodule_package -o criu.pp -m criu.mod
#semodule -i criu.pp

echo "Start container with tomcat"
podman --log-level debug run --tmpfs /tmp --tmpfs /usr/local/tomcat/logs -d docker://docker.io/yovfiatbeb/podman-criu-test

echo "See which containers are running"
podman ps

# tomcat needs some time to start up
echo "Wait 15 seconds for tomcat to start"
sleep 15

echo "Connect to tomcat in the container"
curl `podman inspect -l | jq -r '.[0].NetworkSettings.IPAddress'`:8080/examples/servlets/servlet/HelloWorldExample -v

echo "Checkpoint container"
podman --log-level debug container checkpoint -l

podman ps -a
echo "Restore container"
podman --log-level debug container restore -l

podman ps -a
echo "Check if we can connect to the restored container"
curl `podman inspect -l | jq -r '.[0].NetworkSettings.IPAddress'`:8080/examples/servlets/servlet/HelloWorldExample -v

ls -la
echo test
