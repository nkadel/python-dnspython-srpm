python-dnspython-srpm
=====================

SRPM building tools for python-dnspython. These were assembled with "py2pack", to provide python3-dnspython on RHEL 7.

The "make" command will do these steps.

	make build	# Build the package on the local OS
	make all	# Use "mock" to build the packages with the local
			# samba4repo-f29-x96_64 configuration

		Nico Kadel-Garcia <nkadel@gmail.com>
