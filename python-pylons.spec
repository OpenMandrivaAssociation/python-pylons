%define	module		pylons
%define tarname		Pylons

Summary:		Pylons web framework
Name:			python-%{module}
Version:		1.0
Release:		4
Source0:		%{tarname}-%{version}.tar.gz
License:		BSD
Group:			Development/Python
Url:			https://www.pylonshq.com/
BuildArch:		noarch
BuildRequires:		python-setuptools
Requires:		python-beaker >= 1.3-0.dev.0
Requires:		python-decorator >= 2.3.2
Requires:		python-formencode >= 1.2.1
Requires:		python-mako >= 0.2.4
Requires:		python-nose >= 0.10.4
Requires:		python-paste >= 1.7.2
Requires:		python-pastedeploy >= 1.3.3
Requires:		python-pastescript >= 1.7.3
Requires:		python-routes >= 1.12
Requires:		python-simplejson >= 2.0.8
Requires:		python-tempita >= 0.2
Requires:		python-webob >= 0.9.6.1
Requires:		python-weberror >= 0.10.1
Requires:		python-webhelpers >= 0.6.4
Requires:		python-webtest >= 1.1
Suggests:		python-genshi >= 0.4.4
Suggests:		python-jinja2

%description
The Pylons web framework is aimed at making webapp and programmatic
website development in Python easy.

%prep
%setup -q -n %{tarname}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST
%doc CHANGELOG LICENSE README.txt


%changelog
* Fri Apr 01 2011 Lev Givon <lev@mandriva.org> 1.0-2mdv2011.0
+ Revision: 649520
- Add install dependencies.

* Tue Nov 09 2010 Lev Givon <lev@mandriva.org> 1.0-1mdv2011.0
+ Revision: 595334
- import python-pylons


