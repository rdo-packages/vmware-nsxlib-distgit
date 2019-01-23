# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name vmware-nsxlib
%global module vmware_nsxlib

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        A common library that interfaces with VMware NSX

License:        ASL 2.0
URL:            https://github.com/openstack/vmware-nsxlib
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
vmware-nsxlib is a common library that interfaces with VMware NSX

%package -n     python%{pyver}-%{pypi_name}
Summary:        A common library that interfaces with VMware NSX
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}}

BuildRequires:  git
BuildRequires:  python%{pyver}-decorator
BuildRequires:  python%{pyver}-fixtures
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-subunit
BuildRequires:  python%{pyver}-stestr
BuildRequires:  python%{pyver}-testscenarios
BuildRequires:  python%{pyver}-testtools
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-hacking
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-oslo-sphinx
BuildRequires:  python%{pyver}-oslotest
BuildRequires:  python%{pyver}-oslo-log
BuildRequires:  python%{pyver}-oslo-serialization
BuildRequires:  python%{pyver}-oslo-service
BuildRequires:  python%{pyver}-oslo-utils
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-tenacity
BuildRequires:  python%{pyver}-testresources
BuildRequires:  python%{pyver}-sphinx
Requires:       python%{pyver}-pbr >= 2.0.0
Requires:       python%{pyver}-decorator
Requires:       python%{pyver}-eventlet >= 0.18.2
Requires:       python%{pyver}-netaddr >= 0.7.18
Requires:       python%{pyver}-tenacity >= 4.4.0
Requires:       python%{pyver}-six >= 1.10.0
Requires:       python%{pyver}-oslo-i18n >= 3.15.3
Requires:       python%{pyver}-oslo-log >= 3.36.0
Requires:       python%{pyver}-oslo-serialization >= 2.18.0
Requires:       python%{pyver}-oslo-service >= 1.24.0
Requires:       python%{pyver}-oslo-utils >= 3.33.0
Requires:       python%{pyver}-pyOpenSSL >= 17.1.0

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python-requests-mock
Requires:       python-enum34
%else
BuildRequires:  python%{pyver}-requests-mock
%endif

%description -n python%{pyver}-%{pypi_name}
vmware-nsxlib is a common library that interfaces with VMware NSX


%package -n python%{pyver}-%{pypi_name}-tests
Summary:    A common library that interfaces with VMware NSX - tests
Requires:   python%{pyver}-%{pypi_name} = %{version}-%{release}

%description -n python%{pyver}-%{pypi_name}-tests
A common library that interfaces with VMware NSX

This package contains the test files.


%package -n python-%{pypi_name}-doc
Summary:        vmware-nsxlib documentation
%description -n python-%{pypi_name}-doc
Documentation for vmware-nsxlib


%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Let's handle dependencies ourseleves
rm -f *requirements.txt
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{pyver_build}

# generate html docs
sphinx-build-%{pyver} doc/source html
# remove the sphinx-build-%{pyver} leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{pyver_install}

%check
%{pyver_bin} setup.py test

%files -n python%{pyver}-%{pypi_name}
%license LICENSE
%doc README.rst
%{pyver_sitelib}/%{module}
%{pyver_sitelib}/%{module}-*-py?.?.egg-info
%exclude %{pyver_sitelib}/%{module}/tests

%files -n python%{pyver}-%{pypi_name}-tests
%license LICENSE
%{pyver_sitelib}/%{module}/tests

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html

%changelog
