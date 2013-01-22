Name: crtools	
Version: 0.3	
Release: 3%{?dist}
Summary: Tool for Checkpoint/Restore in User-space
Group: System Environment/Base
License: GPLv2
URL: http://criu.org/
Source0: http://download.openvz.org/criu/crtools-0.3.tar.bz2

BuildRequires: protobuf-c-devel asciidoc xmlto

# user-space and kernel changes are only available for x86_64
# code is very architecture specific
# once imported in RCS it needs a bug openend explaining the ExclusiveArch
# https://bugzilla.redhat.com/show_bug.cgi?id=902875
ExclusiveArch: x86_64

%description
crtools is the user-space part of Checkpoint/Restore in User-space
(CRIU), a project to implement checkpoint/restore functionality for
Linux in user-space. 


%prep
%setup -q
# quick fix for broken Makefile in Documentation/
sed -i -e 's,$(E),echo,g' Documentation/Makefile
# allow our CLFAGS to enhance the existing
sed -i -e "s,CFLAGS\t\t=,CFLAGS\t\t+=,g" Makefile

%build
# %{?_smp_mflags} does not work
# -fstack-protector breaks build
CFLAGS+=`echo %{optflags} | sed -e 's,-fstack-protector,,g'` make V=1 WERROR=0
make -C Documentation V=1


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -m 644 Documentation/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%{_bindir}/%{name}
%{_mandir}/man1/*
%doc README COPYING

%changelog
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
