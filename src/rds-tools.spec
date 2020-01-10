Summary: RDS support tools 
Name: rds-tools
Version: 2.0.4
Release: 1
License: GPL/BSD
Group: Applications/Internet
URL: http://oss.oracle.com/projects/rds/
Source: rds-tools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
rds-tools is a collection of support tools for the RDS socket API.
It includes rds-stress, rds-info, and rds-ping.

%package -n rds-devel
Summary: Header files for RDS development
Group: Development/Libraries

%description -n rds-devel
Header file and manpages for rds and rds-rdma that describe
how to use the socket interface.

%prep
%setup -q
 
%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*

%files -n rds-devel
%{_includedir}/*
%{_mandir}/man7/*
%doc docs examples

%changelog
* Sun Nov 25 2007 Vladimir Sokolovsky <vlad@mellanox.co.il>
- Use DESTDIR
* Mon Oct 27 2006 Zach Brown <zach.brown@oracle.com>
- initial version
