#!/bin/bash

set -x

uname -a

# These zdtm tests are skipped because they fail only in CI system
EXCLUDES=" \
	-x zdtm/static/socket-tcp-reseted \
	-x zdtm/static/socket-tcp-closed \
	-x zdtm/static/socket-tcp-closed-last-ack \
	-x zdtm/static/socket-tcp6-closed \
	-x zdtm/static/socket-tcp4v6-closed \
	-x zdtm/static/maps01 \
	-x zdtm/static/maps04 \
	-x zdtm/static/cgroup04 \
	-x zdtm/static/cgroup_ifpriomap \
	-x zdtm/static/netns_sub \
	-x zdtm/static/netns_sub_veth \
	-x zdtm/static/file_locks01 \
	-x zdtm/static/cgroup02 "

run_test() {
	./zdtm.py run --criu-bin /usr/sbin/criu ${EXCLUDES} \
		-a --ignore-taint --keep-going

	RESULT=$?
}


RESULT=42

# F30, F29 do not provide python -> python3 symlink
test -e /usr/bin/python || ln -sf /usr/bin/python3 /usr/bin/python
python -V

# this socket brakes CRIU's test cases
rm -f /var/lib/sss/pipes/nss

cd source

echo "Build CRIU"
make

cd test

echo "Run the actual CRIU test suite"
run_test

if [ "$RESULT" -ne "0" ]; then
	# Run tests a second time to make sure it is a real failure
	echo "Something failed. Run the actual CRIU test suite a second time"
	run_test
	if [ "$RESULT" -ne "0" ]; then
		echo "Still a test suite error. Something seems to be actually broken"
		exit $RESULT
	fi
fi

exit 0
