Name: criu	
Version: 1.3.1
Release: 1%{?dist}
Provides: crtools = %{version}-%{release}
Obsoletes: crtools <= 1.0-2
Summary: Tool for Checkpoint/Restore in User-space
Group: System Environment/Base
License: GPLv2
URL: http://criu.org/
Source0: http://download.openvz.org/criu/criu-%{version}.tar.bz2

BuildRequires: protobuf-c-devel asciidoc xmlto

# user-space and kernel changes are only available for x86_64 and ARM
# code is very architecture specific
# once imported in RCS it needs a bug openend explaining the ExclusiveArch
# https://bugzilla.redhat.com/show_bug.cgi?id=902875
ExclusiveArch: x86_64 %{arm}

%description
criu is the user-space part of Checkpoint/Restore in User-space
(CRIU), a project to implement checkpoint/restore functionality for
Linux in user-space. 

%package devel
Summary: Header files and libraries for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains header files and libraries for %{name}.


%prep
%setup -q -n criu-%{version}

%build
# %{?_smp_mflags} does not work
# -fstack-protector breaks build
CFLAGS+=`echo %{optflags} | sed -e 's,-fstack-protector\S*,,g'` make V=1 WERROR=0 PREFIX=%{_prefix}
make docs V=1


%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir} LOGROTATEDIR=%{_sysconfdir}/logrotate.d

# upstream renamed to binary to criu
ln -s %{_sbindir}/criu $RPM_BUILD_ROOT%{_sbindir}/crtools

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_sbindir}/%{name}
%{_sbindir}/crtools
%{_mandir}/man8/*
%{_unitdir}/criu.service
%{_unitdir}/criu.socket
%{_libdir}/*.so.*
%{_sysconfdir}/logrotate.d/%{name}-service
%doc README COPYING

%files devel
%{_includedir}/criu
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
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
