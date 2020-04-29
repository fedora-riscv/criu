#!/bin/bash

set -eux

ls -la

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
