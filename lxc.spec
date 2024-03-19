#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lxc
Version  : 5.0.3
Release  : 15
URL      : https://linuxcontainers.org
Source0  : https://linuxcontainers.org/downloads/lxc/lxc-%{version}.tar.gz
Source1  : lxc.tmpfiles
Summary  : Linux Containers userspace tools
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: lxc-bin
Requires: lxc-python
Requires: lxc-config
Requires: lxc-lib
Requires: lxc-doc
Requires: lxc-data
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : doxygen
BuildRequires : gettext-bin
BuildRequires : gnutls-dev
BuildRequires : graphviz
BuildRequires : libcap-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(libseccomp)
BuildRequires : python3-dev
BuildRequires : sed
#Patch1: CVE-2015-1335.patch

%description
Containers are insulated areas inside a system, which have their own namespace
for filesystem, network, PID, IPC, CPU and memory allocation and which can be
created using the Control Group and Namespace features included in the Linux
kernel.

This package provides the lxc-* tools, which can be used to start a single
daemon in a container, or to boot an entire "containerized" system, and to
manage and debug your containers.

%package bin
Summary: bin components for the lxc package.
Group: Binaries
Requires: lxc-data
Requires: lxc-config

%description bin
bin components for the lxc package.


%package config
Summary: config components for the lxc package.
Group: Default

%description config
config components for the lxc package.


%package data
Summary: data components for the lxc package.
Group: Data

%description data
data components for the lxc package.


%package dev
Summary: dev components for the lxc package.
Group: Development
Requires: lxc-lib
Requires: lxc-bin
Requires: lxc-data
Provides: lxc-devel

%description dev
dev components for the lxc package.


%package doc
Summary: doc components for the lxc package.
Group: Documentation

%description doc
doc components for the lxc package.


%package lib
Summary: lib components for the lxc package.
Group: Libraries
Requires: lxc-data
Requires: lxc-config

%description lib
lib components for the lxc package.


%package python
Summary: python components for the lxc package.
Group: Default

%description python
python components for the lxc package.


%prep
%setup -q -n lxc-%{version}
#%%patch1 -p1

%build
%reconfigure --disable-static --with-systemdsystemunitdir=/usr/lib/systemd/system \
--with-init-script=systemd
make V=1  %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/lxc.conf

%files
%defattr(-,root,root,-)
/usr/lib64/lxc/rootfs/README

%files bin
%defattr(-,root,root,-)
/usr/bin/init.lxc
/usr/bin/lxc-attach
/usr/bin/lxc-autostart
/usr/bin/lxc-cgroup
/usr/bin/lxc-checkconfig
/usr/bin/lxc-checkpoint
/usr/bin/lxc-clone
/usr/bin/lxc-config
/usr/bin/lxc-console
/usr/bin/lxc-create
/usr/bin/lxc-destroy
/usr/bin/lxc-device
/usr/bin/lxc-execute
/usr/bin/lxc-freeze
/usr/bin/lxc-info
/usr/bin/lxc-ls
/usr/bin/lxc-monitor
/usr/bin/lxc-snapshot
/usr/bin/lxc-start
/usr/bin/lxc-start-ephemeral
/usr/bin/lxc-stop
/usr/bin/lxc-top
/usr/bin/lxc-unfreeze
/usr/bin/lxc-unshare
/usr/bin/lxc-usernsexec
/usr/bin/lxc-wait
/usr/libexec/lxc/lxc-apparmor-load
/usr/libexec/lxc/lxc-containers
/usr/libexec/lxc/lxc-devsetup
/usr/libexec/lxc/lxc-monitord
/usr/libexec/lxc/lxc-net
/usr/libexec/lxc/lxc-user-nic

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/lxc-net.service
/usr/lib/systemd/system/lxc.service
/usr/lib/tmpfiles.d/lxc.conf

%files data
%defattr(-,root,root,-)
/usr/share/lxc/config/archlinux.common.conf
/usr/share/lxc/config/archlinux.userns.conf
/usr/share/lxc/config/centos.common.conf
/usr/share/lxc/config/centos.userns.conf
/usr/share/lxc/config/common.conf
/usr/share/lxc/config/common.conf.d/README
/usr/share/lxc/config/common.seccomp
/usr/share/lxc/config/debian.common.conf
/usr/share/lxc/config/debian.userns.conf
/usr/share/lxc/config/fedora.common.conf
/usr/share/lxc/config/fedora.userns.conf
/usr/share/lxc/config/gentoo.common.conf
/usr/share/lxc/config/gentoo.moresecure.conf
/usr/share/lxc/config/gentoo.userns.conf
/usr/share/lxc/config/opensuse.common.conf
/usr/share/lxc/config/opensuse.userns.conf
/usr/share/lxc/config/openwrt.common.conf
/usr/share/lxc/config/oracle.common.conf
/usr/share/lxc/config/oracle.userns.conf
/usr/share/lxc/config/plamo.common.conf
/usr/share/lxc/config/plamo.userns.conf
/usr/share/lxc/config/ubuntu-cloud.common.conf
/usr/share/lxc/config/ubuntu-cloud.lucid.conf
/usr/share/lxc/config/ubuntu-cloud.userns.conf
/usr/share/lxc/config/ubuntu.common.conf
/usr/share/lxc/config/ubuntu.lucid.conf
/usr/share/lxc/config/ubuntu.userns.conf
/usr/share/lxc/config/userns.conf
/usr/share/lxc/hooks/clonehostname
/usr/share/lxc/hooks/mountecryptfsroot
/usr/share/lxc/hooks/squid-deb-proxy-client
/usr/share/lxc/hooks/ubuntu-cloud-prep
/usr/share/lxc/lxc-patch.py
/usr/share/lxc/lxc-patch.pyc
/usr/share/lxc/lxc-patch.pyo
/usr/share/lxc/lxc.functions
/usr/share/lxc/selinux/lxc.if
/usr/share/lxc/selinux/lxc.te
/usr/share/lxc/templates/lxc-alpine
/usr/share/lxc/templates/lxc-altlinux
/usr/share/lxc/templates/lxc-archlinux
/usr/share/lxc/templates/lxc-busybox
/usr/share/lxc/templates/lxc-centos
/usr/share/lxc/templates/lxc-cirros
/usr/share/lxc/templates/lxc-debian
/usr/share/lxc/templates/lxc-download
/usr/share/lxc/templates/lxc-fedora
/usr/share/lxc/templates/lxc-gentoo
/usr/share/lxc/templates/lxc-openmandriva
/usr/share/lxc/templates/lxc-opensuse
/usr/share/lxc/templates/lxc-oracle
/usr/share/lxc/templates/lxc-plamo
/usr/share/lxc/templates/lxc-sshd
/usr/share/lxc/templates/lxc-ubuntu
/usr/share/lxc/templates/lxc-ubuntu-cloud

%files dev
%defattr(-,root,root,-)
/usr/include/lxc/attach_options.h
/usr/include/lxc/lxccontainer.h
/usr/include/lxc/version.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/lxc/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

#based on https://github.com/clearlinux-pkgs/lxc/blob/master/lxc.spec
