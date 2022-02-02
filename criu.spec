%if 0%{?fedora} >= 27 || 0%{?rhel} > 7
%global py_prefix python3
%global py_binary %{py_prefix}
%else
%global py_prefix python
%global py_binary python2
%endif

# With annobin enabled, CRIU does not work anymore. It seems CRIU's
# parasite code breaks if annobin is enabled.
%undefine _annotated_build

# Disable automatic call to the set_build_flags macro
# at the beginning of the build, check, and install.
# This change was introduced in Fedora 36.
%undefine _auto_set_build_flags

Name: criu
Version: 3.16.1
Release: 6%{?dist}
Summary: Tool for Checkpoint/Restore in User-space
License: GPLv2
URL: http://criu.org/
Source0: https://github.com/checkpoint-restore/criu/archive/v%{version}/criu-%{version}.tar.gz

Patch4: 0004-criu-8-add-external-net-option.patch
Patch5: 0005-criu-Introduce-new-device-file-plugin-hooks.patch
Patch6: 0006-criu-plugin-Implement-dummy-amdgpu-plugin-hooks.patch
Patch7: 0007-criu-files-Don-t-cache-fd-ids-for-device-files.patch
Patch8: 0008-tcp-Skip-restoring-TCP-state-when-dumping-with-tcp-c.patch
Patch9: 0009-zdtm-Dumping-restoring-with-tcp-close-on-TCP_CLOSE-s.patch
Patch10: 0010-criu-8-Add-more-detailed-description-about-tcp-close.patch
Patch11: 0011-Add-support-for-python3-in-criu-coredump.patch
Patch12: 0012-Add-new-files-for-running-criu-coredump-via-python-2.patch
Patch13: 0013-coredump-remove-unused-import.patch
Patch14: 0014-coredump-sort-imports.patch
Patch15: 0015-coredump-convert-indentation-to-spaces.patch
Patch16: 0016-python-replace-equality-with-identity-test.patch
Patch17: 0017-coredump-drop-unused-variable.patch
Patch18: 0018-coredump-drop-exec-permission.patch
Patch19: 0019-coredump-lint-fix-for-block-comments.patch
Patch20: 0020-coredump-fix-missing-whitespace-around-operator.patch
Patch21: 0021-coredump-fix-too-many-blank-lines.patch
Patch22: 0022-coredump-fix-comparison-to-true.patch
Patch23: 0023-coredump-lint-fix-visually-indented-line.patch
Patch24: 0024-test-coredump-fix-shellcheck-errors.patch
Patch25: 0025-make-enable-lint-for-coredump.patch
Patch26: 0026-ci-enable-coredump-tests.patch
Patch27: 0027-pie-restorer-remove-excess-hash-printf-specifier.patch
Patch28: 0028-tty-fix-the-null-pointer-of-get_tty_driver.patch
Patch29: 0029-util-use-nftw-in-rmrf-helper.patch
Patch30: 0030-criu-ns-make-pidns-init-first-do-setsid.patch
Patch31: 0031-net-optimize-restore_rule-to-not-open-the-CR_FD_RULE.patch
Patch32: 0032-ci-replace-deprecated-codecov-bash-uploader.patch
Patch33: 0033-ci-fix-userfaultfd-test-failures.patch
Patch34: 0034-ci-use-Fedora-34-for-lint-CI-runs.patch
Patch35: 0035-tests-improve-the-image-streamer-process-control.patch
Patch36: 0036-sockets-don-t-call-sk_setbufs-asyncronously.patch
Patch37: 0037-kerndat-check-for-set-getsockopt-SO_BUF_LOCK-availab.patch
Patch38: 0038-sockets-c-r-bufer-size-locks.patch
Patch39: 0039-zdtm-add-test-for-socket-buffer-size-locks.patch
Patch40: 0040-zdtm-make-sock_opts02-also-check-lock-change-by-SO_-.patch
Patch41: 0041-clang-format-enable-AlignTrailingComments.patch
Patch42: 0042-clang-format-do-several-manual-comment-fixups.patch
Patch43: 0043-clang-format-do-automatic-comment-fixups.patch
Patch44: 0044-cr-dump-fail-dumping-when-zombie-process-with-sid-0.patch
Patch45: 0045-clang-format-make-x86_ins_capability_mask-human-read.patch
Patch46: 0046-ci-disable-socket-raw-test-on-centos8.patch
Patch47: 0047-zdtm.py-make-tests-with-link_remap-exclusive.patch
Patch48: 0048-tests-improve-the-deterministic-behavior-of-the-test.patch
Patch49: 0049-clang-format-zdtm-fix-clang-complains-about-strange-.patch
Patch50: 0050-seize-restore-cgroup-freezer-to-right-state.patch
Patch51: 0051-ci-Use-latest-Fedora-for-lint-ci-runs-again.patch
Patch52: 0052-crtools-ignore-SIGPIPE-in-swrk-mode.patch
Patch53: 0053-ci-switch-to-centos-stream-8.patch
Patch54: 0054-check-cleanup-child-processes.patch
Patch55: 0055-files-reg-fix-error-handling-in-open_path.patch
Patch56: 0056-files-reg-fix-error-handling-of-rm_parent_dirs.patch
Patch57: 0057-ghost-mount-allocate-remounted_rw-in-shmem-to-get-in.patch
Patch58: 0058-files-reg-temporary-remount-writable-the-mount-we-do.patch
Patch59: 0059-zdtm-add-ro-mount-check-after-c-r-to-mntns_ghost01.patch
Patch60: 0060-clang-format-disable-wrong-struct-pointer-declaratio.patch
Patch61: 0061-ci-Run-cross-compile-on-debian-stable.patch
Patch62: 0062-ci-Run-cross-compile-with-debian-testing.patch
Patch63: 0063-make-Explicitly-enable-FPU-on-ARMv7-builds.patch
Patch64: 0064-ci-disable-broken-tests-until-fixed.patch
Patch65: 0065-test-do-not-use-keep-going-for-single-zdtm-tests.patch
Patch66: 0066-files-reg-try-dump_ghost_remap-if-link-remap-failed-.patch
Patch67: 0067-util-make-page-server-IPv6-safe.patch
Patch68: 0068-sk-unix-Fix-TCP_ESTABLISHED-checks-in-unix-sockets.patch
Patch69: 0069-ci-Enable-disabled-unix-socket-related-tests.patch
Patch70: 0070-ci-install-procps-in-Alpine.patch
Patch71: 0071-test-another-try-to-correctly-fix-the-kernel-version.patch
Patch72: 0072-x86-compel-fault-inject-bound-xsave-features-set.patch
Patch73: 0073-x86-compel-fault-inject-print-the-initial-seed.patch
Patch74: 0074-ci-enable-x86-xsave-fault-injection-tests-back.patch
Patch75: 0075-Add-documentation-for-timeout-option.patch
Patch76: 0076-usernsd-UNS_FDOUT-should-not-require-an-input-descri.patch
Patch77: 0077-libcriu-add-setting-lsm-mount-context-to-libcriu.patch
Patch78: 0078-ci-use-unstable-release-for-cross-compile.patch
Patch79: 0079-ci-disable-glibc-rseq-support.patch
Patch80: 0080-libcriu-add-single-pre-dump-support.patch
Patch81: 0081-tests-added-test-for-single-pre-dump-support.patch
Patch82: 0082-zdtm.py-clean-up-MAKEFLAGS-env-variable-before-runni.patch
Patch83: 0083-zdtm-zdtm_ct-fix-compilation-error-with-strict-proto.patch
Patch84: 0084-zdtm-remove-mntns-deleted-dst-test-leftover-from-git.patch
Patch85: 0085-crtools-remove-excess-always-true-condition.patch
Patch86: 0086-crtools-rpc-export-current-criu-mode-to-opts.mode.patch
Patch87: 0087-crtools-use-new-opts.mode-in-image_dir_mode.patch
Patch88: 0088-crtools-check-that-cpuinfo-command-has-sub-command.patch
Patch89: 0089-sk-unix-Add-support-for-SOCK_SEQPACKET-unix-sockets.patch
Patch90: 0090-zdtm-Add-SOCK_SEQPACKET-variants-to-unix-socket-test.patch
Patch91: 0091-tls-fix-typo.patch
Patch92: 0092-tls-use-ssize_t-for-return-value.patch
Patch93: 0093-tls-add-more-comments.patch
Patch94: 0094-uffd-call-disconnect_from_page_server-to-shutdown-a-.patch
Patch95: 0095-tls-allow-to-terminate-connections-synchronously.patch
Patch96: 0096-page-xfer-stop-waiting-for-a-new-command-after-a-clo.patch
Patch97: 0097-ci-reenable-the-lazy-thp-test-in-the-lazy-remote-mod.patch
Patch98: 0098-test-log-testname.out.inprogress-if-a-test-has-faile.patch
Patch99: 0100-zdtm-static-uffd-events-add-more-log-messages.patch
Patch100: 0101-mount-split-check_mountpoint_fd-from-__open_mountpoi.patch
Patch101: 0102-mount-remove-mnt_fd-argument-of-__open_mountpoint.patch
Patch102: 0103-proc_parse-add-helper-to-resolve-sdev-from-fd.patch
Patch103: 0104-mount-btrfs-make-check_mountpoint_fd-fallback-to-get.patch
Patch104: 0105-ci-test-criu-image-streamer-with-all-tests.patch
Patch105: 0106-readme-add-docker-test-badge.patch
Patch106: 0107-contributing-remove-old-badges-and-logo.patch
Patch107: 0108-ci-update-to-latest-Vagrant-and-Fedora-images.patch
Patch108: 0109-ci-added-.lgtm.yml-file.patch
Patch109: 0110-lib-introduce-feature-check-in-libcriu.patch
Patch110: 0111-lib-added-tests-for-feature-check-in-libcriu.patch
Patch111: 0112-pagemap-tiny-fix-on-truncating-memory-image.patch
Patch112: 0113-zdtm-fix-zdtm-static-maps00-case-in-arm64.patch
Patch113: 0114-compel-fix-GCC-12-failure-out-of-bounds.patch
Patch114: 0115-criu-fix-configuration-file-scanner-with-GCC-12.patch
Patch115: 0116-compel-fix-parasite-with-GCC-12.patch
Patch116: 0117-ci-set-continue-on-error-for-cross-compile.patch
Patch117: 0118-test-autofs-fix-use-after-free.patch
Patch118: 0119-Fix-formatting-in-criu-documentation.patch
Patch119: 0120-compel-add-rseq-syscall-into-compel-std-plugin-sysca.patch
Patch120: 0121-kerndat-check-for-rseq-syscall-support.patch
Patch121: 0122-util-move-fork_and_ptrace_attach-helper-from-cr-chec.patch
Patch122: 0123-cr-check-Add-ptrace-rseq-conf-dump-feature.patch
Patch123: 0124-rseq-initial-support.patch
Patch124: 0125-zdtm-add-simple-test-for-rseq-C-R.patch
Patch125: 0126-Revert-ci-disable-glibc-rseq-support.patch
Patch126: 0127-ci-add-Fedora-Rawhide-based-test-on-Cirrus.patch
Patch127: 0128-fixup-attempt-to-disable-rseq-at-the-thread-start.patch
Patch128: 0129-zdtm-fixup-fix-rseq-test-when-linking-with-fresh-gli.patch

# Add protobuf-c as a dependency.
# We use this patch because the protobuf-c package name
# in RPM and DEB is different.
Patch199: criu.pc.patch

%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires: perl
# RHEL has no asciidoc; take man-page from Fedora 26
# zcat /usr/share/man/man8/criu.8.gz > criu.8
Source1: criu.8
Source2: crit.1
Source3: compel.1
Source4: criu-ns.1

# The patch aio-fix.patch is needed as RHEL7
# doesn't do "nr_events *= 2" in ioctx_alloc().
Patch200: aio-fix.patch
%endif

Source5: criu-tmpfiles.conf

BuildRequires: gcc
BuildRequires: systemd
BuildRequires: libnet-devel
BuildRequires: protobuf-devel protobuf-c-devel %{py_prefix}-devel libnl3-devel libcap-devel
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: asciidoctor
BuildRequires: perl-interpreter
BuildRequires: libselinux-devel
BuildRequires: gnutls-devel
# Checkpointing containers with a tmpfs requires tar
Recommends: tar
%if 0%{?fedora}
BuildRequires: libbsd-devel
BuildRequires: nftables-devel
%endif
%endif
BuildRequires: make

# user-space and kernel changes are only available for x86_64, arm,
# ppc64le, aarch64 and s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=902875
ExclusiveArch: x86_64 %{arm} ppc64le aarch64 s390x

%description
criu is the user-space part of Checkpoint/Restore in User-space
(CRIU), a project to implement checkpoint/restore functionality for
Linux in user-space.

%if 0%{?fedora} || 0%{?rhel} > 7
%package devel
Summary: Header files and libraries for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package contains header files and libraries for %{name}.

%package libs
Summary: Libraries for %{name}
Requires: %{name} = %{version}-%{release}

%description libs
This package contains the libraries for %{name}
%endif

%package -n %{py_prefix}-%{name}
%{?python_provide:%python_provide %{py_prefix}-%{name}}
Summary: Python bindings for %{name}
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires: protobuf-python
Requires: %{name} = %{version}-%{release} %{py_prefix}-ipaddr
%else
Requires: %{py_prefix}-protobuf
Obsoletes: python2-criu < 3.10-1
%endif

%description -n %{py_prefix}-%{name}
%{py_prefix}-%{name} contains Python bindings for %{name}.

%package -n crit
Summary: CRIU image tool
Requires: %{py_prefix}-%{name} = %{version}-%{release}

%description -n crit
crit is a tool designed to decode CRIU binary dump files and show
their content in human-readable form.

%package -n criu-ns
Summary: Tool to run CRIU in different namespaces
Requires: %{name} = %{version}-%{release}

%description -n criu-ns
The purpose of the criu-ns wrapper script is to enable restoring a process
tree that might require a specific PID that is already used on the system.
This script can help to workaround the so called "PID mismatch" problem.

%prep
%setup -q

%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1

%patch199 -p1

%if 0%{?rhel} && 0%{?rhel} <= 7
%patch200 -p1
%endif

%build
# This package calls LD directly without specifying the LTO plugins.  Until
# that is fixed, disable LTO.
%define _lto_cflags %{nil}

# %{?_smp_mflags} does not work
# -fstack-protector breaks build
CFLAGS+=`echo %{optflags} | sed -e 's,-fstack-protector\S*,,g'` make V=1 WERROR=0 PREFIX=%{_prefix} RUNDIR=/run/criu PYTHON=%{py_binary}
%if 0%{?fedora} || 0%{?rhel} > 7
make docs V=1
%endif


%install
make install-criu DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir}
make install-lib DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir} PYTHON=%{py_binary}
%if 0%{?fedora} || 0%{?rhel} > 7
# only install documentation on Fedora as it requires asciidoc,
# which is not available on RHEL7
make install-man DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir}
%else
install -p -m 644  -D %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8
install -p -m 644  -D %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/crit.1
install -p -m 644  -D %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man1/compel.1
install -p -m 644  -D %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/man1/criu-ns.1
%endif

mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d -m 0755 %{buildroot}/run/%{name}/

%if 0%{?rhel} && 0%{?rhel} <= 7
# remove devel and libs packages
rm -rf $RPM_BUILD_ROOT%{_includedir}/criu
rm $RPM_BUILD_ROOT%{_libdir}/*.so*
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig
rm -rf $RPM_BUILD_ROOT%{_libexecdir}/%{name}
%endif

# remove static lib
rm -f $RPM_BUILD_ROOT%{_libdir}/libcriu.a

%files
%{_sbindir}/%{name}
%doc %{_mandir}/man8/criu.8*
%doc %{_mandir}/man1/compel.1*
%if 0%{?fedora} || 0%{?rhel} > 7
%{_libexecdir}/%{name}
%endif
%dir /run/%{name}
%{_tmpfilesdir}/%{name}.conf
%doc README.md COPYING

%if 0%{?fedora} || 0%{?rhel} > 7
%files devel
%{_includedir}/criu
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files libs
%{_libdir}/*.so.*
%endif

%files -n %{py_prefix}-%{name}
%if 0%{?rhel} && 0%{?rhel} <= 7
%{python2_sitelib}/pycriu/*
%{python2_sitelib}/*egg-info
%else
%{python3_sitelib}/pycriu/*
%{python3_sitelib}/*egg-info
%endif

%files -n crit
%{_bindir}/crit
%doc %{_mandir}/man1/crit.1*

%files -n criu-ns
%{_sbindir}/criu-ns
%doc %{_mandir}/man1/criu-ns.1*

%changelog
* Mon Jan 31 2022 Radostin Stoyanov <radostin@redhat.com> - 3.16.1-6
- Fix typo in changelog
- Replace `asciidoc` and `xmlto` with `asciidoctor`
- Enable initial rseq support

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 3.16.1-4
- Rebuilt for protobuf 3.19.0

* Mon Oct 25 2021 Adrian Reber <adrian@lisas.de> - 3.16.1-3
- Rebuilt for protobuf 3.18.1

* Tue Oct 19 2021 Radostin Stoyanov <radostin@redhat.com> - 3.16.1-2
- Update protobuf-c to libprotobuf-c requirement

* Thu Oct 14 2021 Radostin Stoyanov <radostin@redhat.com> - 3.16.1-1
- Update to 3.16.1
- Add protobuf-c as required dependency (#2013775)

* Tue Oct 05 2021 Adrian Reber <adrian@lisas.de> - 3.16-3
- Fix build on RHEL 8

* Thu Sep 23 2021 Adrian Reber <adrian@lisas.de> - 3.16-2
- Include criu-ns sub package
- Use new github Source0 location

* Wed Sep 22 2021 Adrian Reber <adrian@lisas.de> - 3.16-1
- Update to 3.16

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.15-5
- Rebuilt for Python 3.10

* Fri Apr 09 2021 Adrian Reber <adrian@lisas.de> - 3.15-4
- Test for testing

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Adrian Reber <adrian@lisas.de> - 3.15-2
- Rebuilt for protobuf 3.14

* Wed Nov 04 2020 Adrian Reber <adrian@lisas.de> - 3.15-1
- Update to 3.15

* Wed Sep 23 2020 Adrian Reber <adrian@lisas.de> - 3.14-8
- Rebuilt for protobuf 3.13

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Jeff Law <law@redhat.com> - 3.14-6
- Disable LTO

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 3.14-5
- Rebuilt for protobuf 3.12

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.14-4
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Adrian Reber <adrian@lisas.de> - 3.14-3
- BuildRequire nftables-devel for working CI

* Thu Apr 30 2020 Adrian Reber <adrian@lisas.de> - 3.14-2
- Rebuild for CI fixes

* Wed Apr 29 2020 Adrian Reber <adrian@lisas.de> - 3.14-1
- Update to 3.14 (#1829399)

* Sun Mar 29 2020 Andrei Vagin <avagin@gmail.com> - 3.13-7
- Added patch for gcc-10

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Adrian Reber <adrian@lisas.de> - 3.13-5
- Update to 3.13 (#1751146)
- Drop upstreamed patches
- Drop static library
- Add compel man-page

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.12-14
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Adrian Reber <adrian@lisas.de> - 3.12-11
- Test different decision_context in gating.yaml

* Mon May 13 2019 Adrian Reber <adrian@lisas.de> - 3.12-10
- Added additional fixup patches for the socket labelling

* Sat May 04 2019 Adrian Reber <adrian@lisas.de> - 3.12-8
- Patch for socket labelling has changed upstream

* Mon Apr 29 2019 Adrian Reber <adrian@lisas.de> - 3.12-4
- Applied patch to correctly restore socket()s

* Sat Apr 27 2019 Adrian Reber <adrian@lisas.de> - 3.12-3
- Correctly exclude libs and devel for RHEL

* Thu Apr 25 2019 Adrian Reber <adrian@lisas.de> - 3.12-2
- Updated to official 3.12

* Tue Apr 23 2019 Adrian Reber <adrian@lisas.de> - 3.12-0.1
- Updated to 3.12 (pre-release)
- Create libs subpackage
- Build against SELinux (Fedora and RHEL8)
- Build against libbsd (Fedora)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Adrian Reber <adrian@lisas.de> - 3.11-2
- Added patch for gcc-9

* Tue Nov 06 2018 Adrian Reber <adrian@lisas.de> - 3.11-1
- Updated to 3.11
- Removed upstreamed patches

* Tue Oct 30 2018 Adrian Reber <adrian@lisas.de> - 3.10-5
- Added Recommends: tar
  It is necessary when checkpointing containers with a tmpfs

* Mon Jul 16 2018 Adrian Reber <adrian@lisas.de> - 3.10-4
- Add patch to fix errors with read-only runc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Adrian Reber <adrian@lisas.de> - 3.10-2
- Disable annobin as it seems to break CRIU

* Tue Jul 10 2018 Adrian Reber <adrian@lisas.de> - 3.10-1
- Update to 3.10 (#1599710)
- Switch to python3

* Wed Jun 06 2018 Adrian Reber <adrian@lisas.de> - 3.9-2
- Simplify ExclusiveArch now that there is no more F26

* Fri Jun 01 2018 Adrian Reber <adrian@lisas.de> - 3.9-1
- Update to 3.9

* Tue Apr 03 2018 Adrian Reber <adrian@lisas.de> - 3.8.1-1
- Update to 3.8.1

* Thu Mar 22 2018 Adrian Reber <adrian@lisas.de> - 3.8-2
- Bump release for COPR

* Wed Mar 14 2018 Adrian Reber <adrian@lisas.de> - 3.8-1
- Update to 3.8

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.7-4
- Switch to %%ldconfig_scriptlets

* Fri Jan 12 2018 Adrian Reber <adrian@lisas.de> - 3.7-3
- Fix python/python2 dependencies accross all branches

* Wed Jan 03 2018 Merlin Mathesius <mmathesi@redhat.com> - 3.7-2
- Cleanup spec file conditionals

* Sat Dec 30 2017 Adrian Reber <adrian@lisas.de> - 3.7-1
- Update to 3.7

* Fri Dec 15 2017 Iryna Shcherbina <ishcherb@redhat.com> - 3.6-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Oct 26 2017 Adrian Reber <adrian@lisas.de> - 3.6-1
- Update to 3.6

* Wed Oct 18 2017 Adrian Reber <adrian@lisas.de> - 3.5-5
- Added patch to fix build on Fedora rawhide aarch64

* Tue Oct 10 2017 Adrian Reber <areber@redhat.com> - 3.5-4
- Upgrade imported manpages to 3.5

* Mon Oct 09 2017 Adrian Reber <areber@redhat.com> - 3.5-3
- Fix ExclusiveArch on RHEL

* Mon Oct 02 2017 Adrian Reber <adrian@lisas.de> - 3.5-2
- Merge RHEL and Fedora spec file

* Thu Sep 28 2017 Adrian Reber <adrian@lisas.de> - 3.5-1
- Update to 3.5 (#1496614)

* Sun Aug 27 2017 Adrian Reber <adrian@lisas.de> - 3.4-1
- Update to 3.4 (#1483774)
- Removed upstreamed patches
- Added s390x (#1475719)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.3-5
- Python 2 binary package renamed to python2-criu
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Adrian Reber <adrian@lisas.de> - 3.3-2
- Added patches to handle changes in glibc

* Wed Jul 19 2017 Adrian Reber <adrian@lisas.de> - 3.3-1
- Update to 3.3

* Fri Jun 30 2017 Adrian Reber <adrian@lisas.de> - 3.2.1-2
- Added patches to handle unified hierarchy and new glibc

* Wed Jun 28 2017 Adrian Reber <adrian@lisas.de> - 3.2.1-1
- Update to 3.2.1-1

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 3.1-2
- Rebuild for protobuf 3.3.1

* Mon May 22 2017 Adrian Reber <adrian@lisas.de> - 3.1-1
- Update to 3.1

* Tue Apr 25 2017 Adrian Reber <adrian@lisas.de> - 3.0-1
- Update to 3.0

* Thu Mar 09 2017 Adrian Reber <adrian@lisas.de> - 2.12-1
- Update to 2.12

* Fri Feb 17 2017 Adrian Reber <adrian@lisas.de> - 2.11.1-1
- Update to 2.11.1

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
