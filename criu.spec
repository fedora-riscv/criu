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
Release: 12%{?dist}
Summary: Tool for Checkpoint/Restore in User-space
License: GPLv2
URL: http://criu.org/
Source0: https://github.com/checkpoint-restore/criu/archive/v%{version}/criu-%{version}.tar.gz

Patch1: 0001-criu-8-add-external-net-option.patch
Patch2: 0002-tcp-Skip-restoring-TCP-state-when-dumping-with-tcp-c.patch
Patch3: 0003-zdtm-Dumping-restoring-with-tcp-close-on-TCP_CLOSE-s.patch
Patch4: 0004-criu-8-Add-more-detailed-description-about-tcp-close.patch
Patch5: 0005-Add-support-for-python3-in-criu-coredump.patch
Patch6: 0006-Add-new-files-for-running-criu-coredump-via-python-2.patch
Patch7: 0007-coredump-remove-unused-import.patch
Patch8: 0008-coredump-sort-imports.patch
Patch9: 0009-coredump-convert-indentation-to-spaces.patch
Patch10: 0010-python-replace-equality-with-identity-test.patch
Patch11: 0011-coredump-drop-unused-variable.patch
Patch12: 0012-coredump-drop-exec-permission.patch
Patch13: 0013-coredump-lint-fix-for-block-comments.patch
Patch14: 0014-coredump-fix-missing-whitespace-around-operator.patch
Patch15: 0015-coredump-fix-too-many-blank-lines.patch
Patch16: 0016-coredump-fix-comparison-to-true.patch
Patch17: 0017-coredump-lint-fix-visually-indented-line.patch
Patch18: 0018-test-coredump-fix-shellcheck-errors.patch
Patch19: 0019-make-enable-lint-for-coredump.patch
Patch20: 0020-ci-enable-coredump-tests.patch
Patch21: 0021-pie-restorer-remove-excess-hash-printf-specifier.patch
Patch22: 0022-tty-fix-the-null-pointer-of-get_tty_driver.patch
Patch23: 0023-util-use-nftw-in-rmrf-helper.patch
Patch24: 0024-criu-ns-make-pidns-init-first-do-setsid.patch
Patch25: 0025-net-optimize-restore_rule-to-not-open-the-CR_FD_RULE.patch
Patch26: 0026-ci-replace-deprecated-codecov-bash-uploader.patch
Patch27: 0027-ci-fix-userfaultfd-test-failures.patch
Patch28: 0028-ci-use-Fedora-34-for-lint-CI-runs.patch
Patch29: 0029-tests-improve-the-image-streamer-process-control.patch
Patch30: 0030-sockets-don-t-call-sk_setbufs-asyncronously.patch
Patch31: 0031-kerndat-check-for-set-getsockopt-SO_BUF_LOCK-availab.patch
Patch32: 0032-sockets-c-r-bufer-size-locks.patch
Patch33: 0033-zdtm-add-test-for-socket-buffer-size-locks.patch
Patch34: 0034-zdtm-make-sock_opts02-also-check-lock-change-by-SO_-.patch
Patch35: 0035-clang-format-enable-AlignTrailingComments.patch
Patch36: 0036-clang-format-do-several-manual-comment-fixups.patch
Patch37: 0037-clang-format-do-automatic-comment-fixups.patch
Patch38: 0038-cr-dump-fail-dumping-when-zombie-process-with-sid-0.patch
Patch39: 0039-clang-format-make-x86_ins_capability_mask-human-read.patch
Patch40: 0040-ci-disable-socket-raw-test-on-centos8.patch
Patch41: 0041-zdtm.py-make-tests-with-link_remap-exclusive.patch
Patch42: 0042-tests-improve-the-deterministic-behavior-of-the-test.patch
Patch43: 0043-clang-format-zdtm-fix-clang-complains-about-strange-.patch
Patch44: 0044-seize-restore-cgroup-freezer-to-right-state.patch
Patch45: 0045-ci-Use-latest-Fedora-for-lint-ci-runs-again.patch
Patch46: 0046-crtools-ignore-SIGPIPE-in-swrk-mode.patch
Patch47: 0047-ci-switch-to-centos-stream-8.patch
Patch48: 0048-check-cleanup-child-processes.patch
Patch49: 0049-files-reg-fix-error-handling-in-open_path.patch
Patch50: 0050-files-reg-fix-error-handling-of-rm_parent_dirs.patch
Patch51: 0051-ghost-mount-allocate-remounted_rw-in-shmem-to-get-in.patch
Patch52: 0052-files-reg-temporary-remount-writable-the-mount-we-do.patch
Patch53: 0053-zdtm-add-ro-mount-check-after-c-r-to-mntns_ghost01.patch
Patch54: 0054-clang-format-disable-wrong-struct-pointer-declaratio.patch
Patch55: 0055-ci-Run-cross-compile-on-debian-stable.patch
Patch56: 0056-ci-Run-cross-compile-with-debian-testing.patch
Patch57: 0057-make-Explicitly-enable-FPU-on-ARMv7-builds.patch
Patch58: 0058-ci-disable-broken-tests-until-fixed.patch
Patch59: 0059-test-do-not-use-keep-going-for-single-zdtm-tests.patch
Patch60: 0060-files-reg-try-dump_ghost_remap-if-link-remap-failed-.patch
Patch61: 0061-util-make-page-server-IPv6-safe.patch
Patch62: 0062-sk-unix-Fix-TCP_ESTABLISHED-checks-in-unix-sockets.patch
Patch63: 0063-ci-Enable-disabled-unix-socket-related-tests.patch
Patch64: 0064-ci-install-procps-in-Alpine.patch
Patch65: 0065-test-another-try-to-correctly-fix-the-kernel-version.patch
Patch66: 0066-x86-compel-fault-inject-bound-xsave-features-set.patch
Patch67: 0067-x86-compel-fault-inject-print-the-initial-seed.patch
Patch68: 0068-ci-enable-x86-xsave-fault-injection-tests-back.patch
Patch69: 0069-Add-documentation-for-timeout-option.patch
Patch70: 0070-usernsd-UNS_FDOUT-should-not-require-an-input-descri.patch
Patch71: 0071-libcriu-add-setting-lsm-mount-context-to-libcriu.patch
Patch72: 0072-ci-use-unstable-release-for-cross-compile.patch
Patch73: 0073-ci-disable-glibc-rseq-support.patch
Patch74: 0074-libcriu-add-single-pre-dump-support.patch
Patch75: 0075-tests-added-test-for-single-pre-dump-support.patch
Patch76: 0076-zdtm.py-clean-up-MAKEFLAGS-env-variable-before-runni.patch
Patch77: 0077-zdtm-zdtm_ct-fix-compilation-error-with-strict-proto.patch
Patch78: 0078-zdtm-remove-mntns-deleted-dst-test-leftover-from-git.patch
Patch79: 0079-crtools-remove-excess-always-true-condition.patch
Patch80: 0080-crtools-rpc-export-current-criu-mode-to-opts.mode.patch
Patch81: 0081-crtools-use-new-opts.mode-in-image_dir_mode.patch
Patch82: 0082-crtools-check-that-cpuinfo-command-has-sub-command.patch
Patch83: 0083-sk-unix-Add-support-for-SOCK_SEQPACKET-unix-sockets.patch
Patch84: 0084-zdtm-Add-SOCK_SEQPACKET-variants-to-unix-socket-test.patch
Patch85: 0085-tls-fix-typo.patch
Patch86: 0086-tls-use-ssize_t-for-return-value.patch
Patch87: 0087-tls-add-more-comments.patch
Patch88: 0088-uffd-call-disconnect_from_page_server-to-shutdown-a-.patch
Patch89: 0089-tls-allow-to-terminate-connections-synchronously.patch
Patch90: 0090-page-xfer-stop-waiting-for-a-new-command-after-a-clo.patch
Patch91: 0091-ci-reenable-the-lazy-thp-test-in-the-lazy-remote-mod.patch
Patch92: 0092-test-log-testname.out.inprogress-if-a-test-has-faile.patch
Patch93: 0093-zdtm-print-tails-of-all-logs-if-a-test-has-failed.patch
Patch94: 0094-zdtm-static-uffd-events-add-more-log-messages.patch
Patch95: 0095-mount-split-check_mountpoint_fd-from-__open_mountpoi.patch
Patch96: 0096-mount-remove-mnt_fd-argument-of-__open_mountpoint.patch
Patch97: 0097-proc_parse-add-helper-to-resolve-sdev-from-fd.patch
Patch98: 0098-mount-btrfs-make-check_mountpoint_fd-fallback-to-get.patch
Patch99: 0099-ci-test-criu-image-streamer-with-all-tests.patch
Patch100: 0100-readme-add-docker-test-badge.patch
Patch101: 0101-contributing-remove-old-badges-and-logo.patch
Patch102: 0102-ci-update-to-latest-Vagrant-and-Fedora-images.patch
Patch103: 0103-ci-added-.lgtm.yml-file.patch
Patch104: 0104-lib-introduce-feature-check-in-libcriu.patch
Patch105: 0105-lib-added-tests-for-feature-check-in-libcriu.patch
Patch106: 0106-pagemap-tiny-fix-on-truncating-memory-image.patch
Patch107: 0107-zdtm-fix-zdtm-static-maps00-case-in-arm64.patch
Patch108: 0108-compel-fix-GCC-12-failure-out-of-bounds.patch
Patch109: 0109-criu-fix-configuration-file-scanner-with-GCC-12.patch
Patch110: 0110-compel-fix-parasite-with-GCC-12.patch
Patch111: 0111-ci-set-continue-on-error-for-cross-compile.patch
Patch112: 0112-test-autofs-fix-use-after-free.patch
Patch113: 0113-Fix-formatting-in-criu-documentation.patch
Patch114: 0114-ci-install-libbsd-dependency.patch
Patch115: 0115-pstree-when-updating-sid-for-shell-job-also-update-m.patch
Patch116: 0116-criu-ns-fix-exit-code-o-for-criu-dump.patch
Patch117: 0117-criu-ns-use-os.waitstatus_to_exitcode.patch
Patch118: 0118-restorer-Fix-sys_mmap-s-returned-value-check.patch
Patch119: 0119-compel-fix-how-PTRACE_GET_THREAD_AREA-errors-are-han.patch
Patch120: 0120-util-add-an-unique-ID-of-the-current-criu-run.patch
Patch121: 0121-files-generate-unique-transport-socket-names.patch
Patch122: 0122-check-Add-a-check-for-using-memfd-with-hugetlb.patch
Patch123: 0123-kerndat-Collect-hugetlb-device-numbers.patch
Patch124: 0124-ipc-Add-support-for-checkpoint-restore-hugetlb-Syste.patch
Patch125: 0125-memfd-shmem-Add-support-for-checkpoint-restore-memfd.patch
Patch126: 0126-proc_parse-files-Add-support-for-hugetlb-memory-mapp.patch
Patch127: 0127-mem-Skip-premapping-hugetlb-mapping.patch
Patch128: 0128-uffd-Skip-lazy-mode-restore-on-hugetlb-mappings.patch
Patch129: 0129-zdtm-Add-MAP_HUGETLB-memory-mapping-test.patch
Patch130: 0130-zdtm-Add-memfd-hugetlb-test.patch
Patch131: 0131-zdtm-Add-shm-hugetlb-test.patch
Patch132: 0132-zdtm-Add-MAP_HUGETLB-mappings-test-for-parent-child-.patch
Patch133: 0133-ci-skip-MAP_HUGETLB-tests-in-stream-test.patch
Patch134: 0134-bpfmap-handle-new-field-in-fdinfo.patch
Patch135: 0135-test-remove-test-for-LOCK_MAND-flock.patch
Patch136: 0136-test-disable-rseq-also-on-Archlinux.patch
Patch137: 0137-zdtm-fix-missplacement-of-err-True.patch
Patch138: 0138-compel-set-mxcsr-during-error-injection-to-zero.patch
Patch139: 0139-proc_smaps-remove-useless-nonlinear-check.patch
Patch140: 0140-mount-fix-e_str-leak-in-ext_mount_add.patch
Patch141: 0141-cr-dump-fix-cr_imgset-leak-in-dump_one_task.patch
Patch142: 0142-tun-fix-tun_link-leak-in-dump_tun_link.patch
Patch143: 0143-sk-unix-fix-uint32_t-id-variable-printf-format-speci.patch
Patch144: 0144-zdtm-refactor-main.patch
Patch145: 0145-zdtm-sort-import-lines.patch
Patch146: 0146-zdtm-use-long-form-cli-options.patch
Patch147: 0147-zdtm-add-criu-config-option.patch
Patch148: 0148-zdtm-drop-redundant-config_inotify_irmap-test.patch
Patch149: 0149-ci-run-criu-config-tests.patch
Patch150: 0150-config-fix-ns-leak-in-parse_join_ns.patch
Patch151: 0151-net-fix-e_str-leak-in-veth_pair_add.patch
Patch152: 0152-files-fix-inh-leak-in-inherit_fd_add.patch
Patch153: 0153-sk-unix-fix-e_str-leak-in-unix_sk_id_add.patch
Patch154: 0154-uffd-fix-__u64-print-format-specifier.patch
Patch155: 0155-zdtm-fix-mnt_ext_master-test-to-correspond-to-it-s-n.patch
Patch156: 0156-mount-add-mntinfo_add_list_before-helper-for-adding-.patch
Patch157: 0157-mount-do-not-detect-non-fsroot-mounts-as-device-exte.patch
Patch158: 0158-mount-mark-mounts-of-external-devices-external.patch
Patch159: 0159-mount-skip-fstype-and-source-checks-for-external-mou.patch
Patch160: 0160-mount-setup-mnt_bind-list-before-using-it-in-mnt_is_.patch
Patch161: 0161-util-add-get_relative_path-helper.patch
Patch162: 0162-unittest-add-some-tests-for-get_relative_path-helper.patch
Patch163: 0163-mount-add-mnt_bind_pick-helper-to-pick-the-desired-b.patch
Patch164: 0164-mount-split-mnt_is_external-_bind-and-can_receive_ma.patch
Patch165: 0165-mount-rework-skipping-external-mounts-in-dump_one_mo.patch
Patch166: 0166-mount-show-more-info-about-why-we-can-t-mount.patch
Patch167: 0167-mount-mount-external-mount-before-mounting-it-s-bind.patch
Patch168: 0168-zdtm-add-new-mnt_ext_root-test.patch
Patch169: 0169-mount-restrict-mp-external-mount-map-to-init-contain.patch
Patch170: 0170-zdtm-add-mnt_ext_collision-test.patch
Patch171: 0171-mount-add-mnt_is_root_bind-helper.patch
Patch172: 0172-mount-allow-nested-mount-namespaces-with-different-r.patch
Patch173: 0173-zdtm-add-mntns_pivot_root-test.patch
Patch174: 0174-mount-apply-superblock-flags-to-nested-ns-roots.patch
Patch175: 0175-zdtm-add-mntns_pivot_root_ro-test.patch
Patch176: 0176-mount-restore-create-auxiliary-binfmt_misc-mount-in-.patch
Patch177: 0177-mount-restore-leave-ns_mountpoint-NULL-for-aux-binfm.patch
Patch178: 0178-mount-replace-CRTIME_MNT_ID-with-HELPER_MNT_ID.patch
Patch179: 0179-mount-add-can_receive_master_from_root-helper.patch
Patch180: 0180-mount-put-external-slavery-mounts-to-separate-mnt_ex.patch
Patch181: 0181-mount-do-not-override-master_id-to-1-for-root-binds.patch
Patch182: 0182-mount-add-helper-mnt_get_external_bind_nodev.patch
Patch183: 0183-mount-prepare-is_overmounted-as-early-as-possible.patch
Patch184: 0184-mount-move-root-yard-tree-merge-as-early-as-possible.patch
Patch185: 0185-mount-fix-broken-remounted_rw-check.patch
Patch186: 0186-mount-make-general-place-for-shared-variables-on-mou.patch
Patch187: 0187-autofs-use-ns_mountpoint-in-autofs_create_dentries.patch
Patch188: 0188-mount-use-ns_mountpoint-in-mnt_is_overmounted.patch
Patch189: 0189-mount-skip-root-yard-children-from-mnt_needs_remap-c.patch
Patch190: 0190-mount-use-ns_mountpoint-in-validate_children_collisi.patch
Patch191: 0191-mount-use-ns_mountpoint-in-root_path_from_parent.patch
Patch192: 0192-mount-use-ns_mountpoint-for-children-overmount-check.patch
Patch193: 0193-path-simplify-mnt_get_sibling_path-via-get_relative_.patch
Patch194: 0194-mount-use-ns_mountpoint-in-collect_mntinfo.patch
Patch195: 0195-mount-use-ns_mountpoint-in-aufs_parse.patch
Patch196: 0196-mount-use-ns_mountpoint-in-mnt_depth.patch
Patch197: 0197-mount-use-ns_mountpoint-instead-of-mountpoint-where-.patch
Patch198: 0198-mount-add-service_mountpoint-getter-for-mountpoint.patch
Patch199: 0199-files-reg-split-create_ghost_dentry-out-of-create_gh.patch
Patch200: 0200-files-reg-teach-create_ghost-to-work-with-mount-v2.patch
Patch201: 0201-files-reg-teach-clean_one_remap-to-work-with-mount-v.patch
Patch202: 0202-kerndat-Check-for-MOVE_MOUNT_SET_GROUP-availability.patch
Patch203: 0203-compel-add-open_tree-syscall.patch
Patch204: 0204-kerndat-check-whether-the-openat2-syscall-is-support.patch
Patch205: 0205-util-add-resolve_mountpoint-helper.patch
Patch206: 0206-crtools-move-check_options-after-kerndat_init-and-lo.patch
Patch207: 0207-config-rpc-add-new-option-mntns-compat-mode-for-old-.patch
Patch208: 0208-mount-add-plain-mountpoints.patch
Patch209: 0209-files-reg-export-parent-dirs-helpers-for-mount-v2.patch
Patch210: 0210-mount-remove-double-ns_id-declaration.patch
Patch211: 0211-mount-export-common-defines-for-mount-v2.patch
Patch212: 0212-mount-export-several-functions-for-mount-v2.patch
Patch213: 0213-mount-export-global-variables-for-mount-v2.patch
Patch214: 0214-mount-add-new-mounts-v2-engine.patch
Patch215: 0215-zdtm-enable-mounts-compat-mode-on-restore-with-mntns.patch
Patch216: 0216-ci-run-tests-for-old-mount-engine.patch
Patch217: 0217-zdtm-add-new-mnt_ext_sharing-test-for-mount-v2.patch
Patch218: 0218-zdtm-add-mount_complex_sharing-test.patch
Patch219: 0219-zdtm-add-propagation-group-with-mount-flags-to-mount.patch
Patch220: 0220-zdtm-mount-v2-disable-mnt_tracefs-test.patch
Patch221: 0221-ci-make-others-mnt_ext_dev-also-run-for-old-mount-en.patch
Patch222: 0222-test-jenkins-test-for-old-mount-engine.patch
Patch223: 0223-zdtm-mount-v2-disable-pty-console-test.patch
Patch224: 0224-mount-v2-make-mount-engine-fallback-messages-logleve.patch
Patch225: 0225-mount-make-error-messages-differ-in-different-places.patch
Patch226: 0226-zdtm-use-unique-holder-for-cgroups.patch
Patch227: 0227-scripts-ci-mount-test-cgroups-once.patch
Patch228: 0228-criu-ns-add-a-helper-to-hold-a-pid-namespace.patch
Patch229: 0229-apparmor-Fix-Wfortify-source-for-Clang.patch
Patch230: 0230-style-delete-some-redundant-code.patch
Patch231: 0231-mount-fix-Wunused-but-set-variable-for-Clang-15.patch
Patch232: 0232-compel-add-rseq-syscall-into-compel-std-plugin-sysca.patch
Patch233: 0233-kerndat-check-for-rseq-syscall-support.patch
Patch234: 0234-util-move-fork_and_ptrace_attach-helper-from-cr-chec.patch
Patch235: 0235-cr-check-Add-ptrace-rseq-conf-dump-feature.patch
Patch236: 0236-rseq-initial-support.patch
Patch237: 0237-zdtm-add-basic-static-rseq00-test-for-rseq-C-R.patch
Patch238: 0238-Revert-ci-disable-glibc-rseq-support.patch
Patch239: 0239-ci-add-Fedora-Rawhide-based-test-on-Cirrus.patch
Patch240: 0240-include-add-thread_pointer.h-from-Glibc.patch
Patch241: 0241-clone-noasan-unregister-rseq-at-the-thread-start-for.patch
Patch242: 0242-zdtm-static-rseq00-fix-rseq-test-when-linking-with-a.patch
Patch243: 0243-compel-add-helpers-to-get-set-instruction-pointer.patch
Patch244: 0244-cr-dump-fixup-thread-IP-when-inside-rseq-cs.patch
Patch245: 0245-zdtm-add-transition-rseq01-test-for-amd64.patch
Patch246: 0246-Revert-test-disable-rseq-also-on-Archlinux.patch
Patch247: 0247-cr-dump-handle-rseq-flags-field.patch
Patch248: 0248-zdtm-add-rseq02-transition-test-with-NO_RESTART-CS-f.patch
Patch249: 0249-zdtm-temporary-disable-rseq02-test.patch

# Add protobuf-c as a dependency.
# We use this patch because the protobuf-c package name
# in RPM and DEB is different.
Patch299: criu.pc.patch

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
Patch300: aio-fix.patch
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

%patch1 -p1
%patch2 -p1
%patch3 -p1
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
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch143 -p1
%patch144 -p1
%patch145 -p1
%patch146 -p1
%patch147 -p1
%patch148 -p1
%patch149 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p1
%patch163 -p1
%patch164 -p1
%patch165 -p1
%patch166 -p1
%patch167 -p1
%patch168 -p1
%patch169 -p1
%patch170 -p1
%patch171 -p1
%patch172 -p1
%patch173 -p1
%patch174 -p1
%patch175 -p1
%patch176 -p1
%patch177 -p1
%patch178 -p1
%patch179 -p1
%patch180 -p1
%patch181 -p1
%patch182 -p1
%patch183 -p1
%patch184 -p1
%patch185 -p1
%patch186 -p1
%patch187 -p1
%patch188 -p1
%patch189 -p1
%patch190 -p1
%patch191 -p1
%patch192 -p1
%patch193 -p1
%patch194 -p1
%patch195 -p1
%patch196 -p1
%patch197 -p1
%patch198 -p1
%patch199 -p1
%patch200 -p1
%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206 -p1
%patch207 -p1
%patch208 -p1
%patch209 -p1
%patch210 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
%patch214 -p1
%patch215 -p1
%patch216 -p1
%patch217 -p1
%patch218 -p1
%patch219 -p1
%patch220 -p1
%patch221 -p1
%patch222 -p1
%patch223 -p1
%patch224 -p1
%patch225 -p1
%patch226 -p1
%patch227 -p1
%patch228 -p1
%patch229 -p1
%patch230 -p1
%patch231 -p1
%patch232 -p1
%patch233 -p1
%patch234 -p1
%patch235 -p1
%patch236 -p1
%patch237 -p1
%patch238 -p1
%patch239 -p1
%patch240 -p1
%patch241 -p1
%patch242 -p1
%patch243 -p1
%patch244 -p1
%patch245 -p1
%patch246 -p1
%patch247 -p1
%patch248 -p1
%patch249 -p1

%patch299 -p1

%if 0%{?rhel} && 0%{?rhel} <= 7
%patch300 -p1
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
* Tue Apr 5 2022 Radostin Stoyanov <rstoyanov@fedoraproject.org> - 3.16.1-12
- Update rseq patches

* Tue Apr 5 2022 Radostin Stoyanov <rstoyanov@fedoraproject.org> - 3.16.1-11
- Update rseq patches

* Tue Apr 5 2022 Radostin Stoyanov <rstoyanov@fedoraproject.org> - 3.16.1-10
- Update fixup patch

* Tue Apr 5 2022 Radostin Stoyanov <rstoyanov@fedoraproject.org> - 3.16.1-9
- Update rseq support patches

* Fri Feb 18 2022 Radostin Stoyanov <rstoyanov@fedoraproject.org> - 3.16.1-8
- rebuilt

* Tue Feb 8 2022 Radostin Stoyanov <radostin@redhat.com> - 3.16.1-7
- Drop global -ffreestanding

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
