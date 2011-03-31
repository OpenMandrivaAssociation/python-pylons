%define	module		pylons
%define tarname		Pylons
%define name		python-%{module}
%define version		1.0
%define release		%mkrel 2

Summary:		Pylons web framework
Name:			%{name}
Version:		%{version}
Release:		%{release}
Source0:		%{tarname}-%{version}.tar.gz
License:		BSD
Group:			Development/Python
Url:			http://www.pylonshq.com/
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc CHANGELOG LICENSE README.txt
