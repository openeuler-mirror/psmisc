Name: psmisc
Version: 23.3
Release: 3
Summary: Utilities for managing processes on your system
License: GPLv2+
URL: https://gitlab.com/psmisc/psmisc
Source0: https://sourceforge.net/projects/%{name}/files/%{name}/%{name}-%{version}.tar.xz
BuildRequires: libselinux-devel gettext ncurses-devel autoconf automake gcc git

Patch0000: backport-0001-pstree-do-not-crash-on-missing-proc-xxxx-directory.patch
Patch0001: backport-0002-pstree-additional-for-do-not-crash-on-missing-proces.patch
Patch0002: backport-0003-killall-minor-str-length-changes.patch
Patch0003: backport-0004-pstree-minor-snprintf-fix.patch
Patch0004: backport-0005-peekfd-Check-return-value-of-malloc.patch
Patch0005: backport-0006-fuser-free-local-port-before-return.patch
Patch0006: backport-0007-peekfd-exit-after-perror.patch
Patch0007: backport-0008-pstree-consecutive-NULs-in-cmdline-args-wrongly-pars.patch
Patch0008: backport-0009-fuser-Less-confused-about-duplicate-dev_id.patch
Patch0009: backport-0010-fuser-Check-pathname-only-on-non-block-devices.patch

Patch9001: bugfix-fix-pstree-coredump-due-pid-reuse.patch

%description
This PSmisc package is a set of some small useful utilities that use the proc
filesystem. We're not about changing the world, but providing the system
administrator with some help in common tasks.

%prep
%autosetup -n %{name}-%{version} -p1 -Sgit

%build
%configure --prefix=%{_prefix} --enable-selinux
%make_build

%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mv $RPM_BUILD_ROOT%{_bindir}/fuser $RPM_BUILD_ROOT%{_sbindir}
%find_lang %name

%files -f %{name}.lang
%{_sbindir}/fuser
%{_bindir}/*
%{_mandir}/man1/*
%license COPYING
%doc AUTHORS ChangeLog README

%changelog
* Mon Feb 8 2021 xinghe <xinghe1@huawei.com> - 23.3-3
- rebuild package

* Thu Nov 03 2020 xinghe <xinghe1@huawei.com> - 23.3-2
- sync patchs

* Fri Apr 17 2020 chenmingmin <chenmingmin@huawei.com> - 23.3-1
- Type:enhancement
- ID:NA
- SUG:restart
- DESC:upgrade to 23.3

* Wed May 8 2019 xiashuang <xiashuang1@huawei.com> - 23.1-5
- Type:bugfix
- ID:NA
- SUG:restart
- DESC:fix adapt patch error

* Tue Jan 22 2019 xiashuang <xiashuang1@huawei.com> - 23.1-4
- Type:bugfix
- ID:NA
- SUG:restart
- DESC:adapt patches from 7.3

* Mon Sep 10 2018 openEuler Buildteam <buildteam@openeuler.org> - 23.1-3
- Package init
