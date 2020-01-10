Name:		rds-tools
Summary:	RDS support tools 
Version:	2.0.4
Release:	3%{?dist}
License:	GPLv2+ or BSD
Group:		Applications/System
URL:		http://oss.oracle.com/projects/rds/
# As per the rds site above, the RDS user space tools are distributed through
# the OpenFabrics Enterprise Distribution (OFED).  In order to get the
# current rds-tools tarball, you need to download the current OFED distribution,
# unpack it, install the rds-tools src rpm, then grab the tarball from your
# rpm SOURCES directory.  The OFED distribution can be downloaded from:
# http://www.openfabrics.org/downloads/OFED/
Source0:	rds-tools-%{version}.tar.gz
Source1:	rds-tools-modprobe.conf
Patch0:		rds-tools-1.5-pfhack.patch
Patch1:		rds-tools-make.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:	s390 s390x

%description
Various tools for support of the RDS (Reliable Datagram Socket) API.  RDS
is specific to InfiniBand and iWARP networks and does not work on non-RDMA
hardware.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
chmod 0755 %{buildroot}%{_bindir}/*
rm -fr %{buildroot}%{_includedir}
install -p -m 644 -D %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/modprobe.d/rds.conf


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README docs examples
%{_bindir}/*
%{_mandir}/*/*
%{_sysconfdir}/modprobe.d/rds.conf

%changelog
* Fri Feb 04 2011 Doug Ledford <dledford@redhat.com> - 2.0.4-3
- Update a few things for rpmdiff checks

* Thu Feb 03 2011 Doug Ledford <dledford@redhat.com> - 2.0.4-2
- Add a modprobe conf file to automatically load rds_tcp and rds_rdma when
  we load the base rds module
- Resolves: bz643113

* Thu Feb 03 2011 Doug Ledford <dledford@redhat.com> - 2.0.4-1
- Update to latest upstream version
- Resolves: bz636908

* Fri Feb 19 2010 Doug Ledford <dledford@redhat.com> - 1.5-2
- Remove include file as we don't provide a real devel environment
- Related: bz543948

* Tue Dec 22 2009 Doug Ledford <dledford@redhat.com> - 1.5-1
- Update to latest upstream version
- Related: bz518218

* Tue Jul 21 2009 Doug Ledford <dledford@redhat.com> - 1.4-2
- Enable debug output during build so debuginfo package isn't empty
- Resolves: bz500627

* Sat Apr 18 2009 Doug Ledford <dledford@redhat.com> - 1.4-1.el5
- Initial version for Red Hat Enterprise Linux 5
- Related: bz459652

