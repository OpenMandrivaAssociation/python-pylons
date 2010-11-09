%define	module		pylons
%define tarname		Pylons
%define name		python-%{module}
%define version		1.0
%define release		%mkrel 1

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
