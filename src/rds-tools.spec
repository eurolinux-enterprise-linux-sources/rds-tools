Summary: RDS support tools 
Name: rds-tools
Version: 1.5
Release: 1
License: GPL/BSD
Group: Applications/Internet
URL: http://oss.oracle.com/projects/rds/
Source: rds-tools-%{version}-%{release}.tar.gz
BuildRoot: /var/tmp/rds-tools-%{version}-%{release}

%description
rds-tools is a collection of support tools for the RDS socket API.

%prep
%setup -n rds-tools-%{version}-%{release}
 
%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*
%{_includedir}/*

%changelog
* Sun Nov 25 2007 Vladimir Sokolovsky <vlad@mellanox.co.il>
- Use DESTDIR
* Mon Oct 27 2006 Zach Brown <zach.brown@oracle.com>
- initial version
