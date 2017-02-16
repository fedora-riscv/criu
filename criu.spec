Name: criu
Version: 2.11
Release: 1%{?dist}
Provides: crtools = %{version}-%{release}
Obsoletes: crtools <= 1.0-2
Summary: Tool for Checkpoint/Restore in User-space
Group: System Environment/Base
License: GPLv2
URL: http://criu.org/
Source0: http://download.openvz.org/criu/criu-%{version}.tar.bz2
Patch0: fix-clobber-list-item.patch

%if 0%{?rhel}
# RHEL has no asciidoc; take man-page from Fedora 24
# zcat /usr/share/man/man8/criu.8.gz > criu.8
Source1: criu.8
%endif

BuildRequires: libnet-devel
BuildRequires: protobuf-devel protobuf-c-devel python2-devel libnl3-devel libcap-devel
BuildRequires: perl
%if 0%{?fedora}
BuildRequires: asciidoc xmlto
%endif

# user-space and kernel changes are only available for x86_64 and ARM
# code is very architecture specific
# once imported in RCS it needs a bug openend explaining the ExclusiveArch
# https://bugzilla.redhat.com/show_bug.cgi?id=902875
%if 0%{?fedora}
ExclusiveArch: x86_64 %{arm} ppc64le aarch64
%else
ExclusiveArch: x86_64 ppc64le
%endif


%description
criu is the user-space part of Checkpoint/Restore in User-space
(CRIU), a project to implement checkpoint/restore functionality for
Linux in user-space.

%if 0%{?fedora}
%package devel
Summary: Header files and libraries for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains header files and libraries for %{name}.
%endif

%package -n python-%{name}
Summary: Python bindings for %{name}
Group: Development/Languages
Requires: %{name} = %{version}-%{release} python-ipaddr protobuf-python

%description -n python-%{name}
python-%{name} contains Python bindings for %{name}.

%package -n crit
Summary: CRIU image tool
Requires: python-%{name} = %{version}-%{release}

%description -n crit
crit is a tool designed to decode CRIU binary dump files and show
their content in human-readable form.


%prep
%setup -q
%patch0 -p1

%build
# %{?_smp_mflags} does not work
# -fstack-protector breaks build
CFLAGS+=`echo %{optflags} | sed -e 's,-fstack-protector\S*,,g'` make V=1 WERROR=0 PREFIX=%{_prefix}
%if 0%{?fedora}
make docs V=1
%endif


%install
make install-criu DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir}
make install-lib DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir}
%if 0%{?fedora}
# ony install documentation on Fedora as it requires asciidoc,
# which is not available on RHEL7
make install-man DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir}
%else
install -p -m 644  -D %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8
%endif

%if 0%{?rhel}
# remove devel package
rm -rf $RPM_BUILD_ROOT%{_includedir}/criu
rm $RPM_BUILD_ROOT%{_libdir}/*.so*
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_sbindir}/%{name}
%doc %{_mandir}/man8/criu.8*
%if 0%{?fedora}
%{_libdir}/*.so.*
%{_libexecdir}/%{name}
%endif
%doc README.md COPYING

%if 0%{?fedora}
%files devel
%{_includedir}/criu
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%endif

%files -n python-%{name}
%{python2_sitelib}/pycriu/*
%{python2_sitelib}/*egg-info

%files -n crit
%{_bindir}/crit
%doc %{_mandir}/man1/crit.1*


%changelog
* Thu Feb 16 2017 Adrian Reber <adrian@lisas.de> - 2.11-1
- Update to 2.11

* Mon Feb 13 2017 Adrian Reber <adrian@lisas.de> - 2.10-4
- Added patch to fix build on ppc64le

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Orion Poplawski <orion@cora.nwra.com> - 2.10-2
- Rebuild for protobuf 3.2.0

* Mon Jan 16 2017 Adrian Reber <adrian@lisas.de> - 2.10-1
- Update to 2.10

* Mon Dec 12 2016 Adrian Reber <adrian@lisas.de> - 2.9-1
- Update to 2.9
- Added crit manpage to crit subpackage

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 2.8-2
- Rebuild for protobuf 3.1.0

* Tue Nov 15 2016 Adrian Reber <adrian@lisas.de> - 2.8-1
- Update to 2.8
- Dropped 'mount_resolve_path()' patch

* Wed Oct 19 2016 Adrian Reber <adrian@lisas.de> - 2.7-2
- Added upstream patch to fix #1381351
  ("criu: mount_resolve_path(): criu killed by SIGSEGV")

* Wed Oct 19 2016 Adrian Reber <adrian@lisas.de> - 2.7-1
- Update to 2.7

* Tue Sep 13 2016 Adrian Reber <adrian@lisas.de> - 2.6-1
- Update to 2.6

* Tue Aug 30 2016 Adrian Reber <adrian@lisas.de> - 2.5-1
- Update to 2.5

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 12 2016 Adrian Reber <adrian@lisas.de> - 2.4-1
- Update to 2.4

* Tue Jun 14 2016 Adrian Reber <areber@redhat.com> - 2.3-1
- Update to 2.3
- Copy man-page from Fedora 24 for RHEL

* Mon May 23 2016 Adrian Reber <adrian@lisas.de> - 2.2-1
- Update to 2.2

* Tue Apr 12 2016 Adrian Reber <adrian@lisas.de> - 2.1-2
- Remove crtools symbolic link

* Mon Apr 11 2016 Adrian Reber <adrian@lisas.de> - 2.1-1
- Update to 2.1

* Wed Apr 06 2016 Adrian Reber <areber@redhat.com> - 2.0-2
- Merge changes from Fedora

* Thu Mar 10 2016 Andrey Vagin <avagin@openvz.org> - 2.0-1
- Update to 2.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Adrian Reber <adrian@lisas.de> - 1.8-1
- Update to 1.8

* Mon Nov 02 2015 Adrian Reber <adrian@lisas.de> - 1.7.2-1
- Update to 1.7.2

* Mon Sep 7 2015 Andrey Vagin <avagin@openvz.org> - 1.7-1
- Update to 1.7

* Thu Sep 3 2015 Andrey Vagin <avagin@openvz.org> - 1.6.1-3
- Build only for power64le

* Thu Sep 3 2015 Andrey Vagin <avagin@openvz.org> - 1.6.1-2
- Build for aarch64 and power64

* Thu Aug 13 2015 Adrian Reber <adrian@lisas.de> - 1.6.1-1
- Update to 1.6.1
- Merge changes for RHEL packaging

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Adrian Reber <areber@redhat.com> - 1.6-1.1
- adapt to RHEL7

* Mon Jun 01 2015 Andrew Vagin <avagin@openvz.org> - 1.6-1
- Update to 1.6

* Thu Apr 30 2015 Andrew Vagin <avagin@openvz.org> - 1.5.2-2
- Require protobuf-python and python-ipaddr for python-criu

* Tue Apr 28 2015 Andrew Vagin <avagin@openvz.org> - 1.5.2
- Update to 1.5.2

* Sun Apr 19 2015 Nikita Spiridonov <nspiridonov@odin.com> - 1.5.1-2
- Create python-criu and crit subpackages

* Tue Mar 31 2015 Andrew Vagin <avagin@openvz.org> - 1.5.1
- Update to 1.5.1

* Sat Dec 06 2014 Adrian Reber <adrian@lisas.de> - 1.4-1
- Update to 1.4

* Tue Sep 23 2014 Adrian Reber <adrian@lisas.de> - 1.3.1-1
- Update to 1.3.1 (#1142896)

* Tue Sep 02 2014 Adrian Reber <adrian@lisas.de> - 1.3-1
- Update to 1.3
- Dropped all upstreamed patches
- included pkgconfig file in -devel

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 07 2014 Andrew Vagin <avagin@openvz.org> - 1.2-4
- Include inttypes.h for PRI helpers

* Thu Aug 07 2014 Andrew Vagin <avagin@openvz.org> - 1.2-3
- Rebuilt for https://bugzilla.redhat.com/show_bug.cgi?id=1126751

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 28 2014 Adrian Reber <adrian@lisas.de> - 1.2-1
- Update to 1.2
- Dropped all upstreamed patches

* Tue Feb 04 2014 Adrian Reber <adrian@lisas.de> - 1.1-4
- Create -devel subpackage

* Wed Dec 11 2013 Andrew Vagin <avagin@openvz.org> - 1.0-3
- Fix the epoch of crtools

* Tue Dec 10 2013 Andrew Vagin <avagin@openvz.org> - 1.0-2
- Rename crtools to criu #1034677

* Wed Nov 27 2013 Andrew Vagin <avagin@openvz.org> - 1.0-1
- Update to 1.0

* Thu Oct 24 2013 Andrew Vagin <avagin@openvz.org> - 0.8-1
- Update to 0.8

* Tue Sep 10 2013 Andrew Vagin <avagin@openvz.org> - 0.7-1
- Update to 0.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Andrew Vagin <avagin@openvz.org> - 0.6-3
- Delete all kind of -fstack-protector gcc options

* Wed Jul 24 2013 Andrew Vagin <avagin@openvz.org> - 0.6-3
- Added arm macro to ExclusiveArch

* Wed Jul 03 2013 Andrew Vagin <avagin@openvz.org> - 0.6-2
- fix building on ARM
- fix null pointer dereference

* Tue Jul 02 2013 Adrian Reber <adrian@lisas.de> - 0.6-1
- updated to 0.6
- upstream moved binaries to sbin
- using upstream's make install

* Tue May 14 2013 Adrian Reber <adrian@lisas.de> - 0.5-1
- updated to 0.5

* Fri Feb 22 2013 Adrian Reber <adrian@lisas.de> - 0.4-1
- updated to 0.4

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Adrian Reber <adrian@lisas.de> - 0.3-3
- added ExclusiveArch blocker bug

* Fri Jan 18 2013 Adrian Reber <adrian@lisas.de> - 0.3-2
- improved Summary and Description

* Mon Jan 14 2013 Adrian Reber <adrian@lisas.de> - 0.3-1
- updated to 0.3
- fix building Documentation/

* Tue Aug 21 2012 Adrian Reber <adrian@lisas.de> - 0.2-2
- remove macros like %%{__mkdir_p} and %%{__install}
- add comment why it is only x86_64

* Tue Aug 21 2012 Adrian Reber <adrian@lisas.de> - 0.2-1
- initial release
