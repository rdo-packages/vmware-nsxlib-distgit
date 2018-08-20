%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

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

%package -n     python2-%{pypi_name}
Summary:        A common library that interfaces with VMware NSX
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  git
BuildRequires:  python2-fixtures
BuildRequires:  python-requests-mock
BuildRequires:  python2-setuptools
BuildRequires:  python2-subunit
BuildRequires:  python2-testrepository
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python2-devel
BuildRequires:  python2-hacking
BuildRequires:  python2-mock
BuildRequires:  python2-oslo-sphinx
BuildRequires:  python2-oslotest
BuildRequires:  python2-oslo-log
BuildRequires:  python2-oslo-serialization
BuildRequires:  python2-oslo-utils
BuildRequires:  python2-pbr
BuildRequires:  python2-sphinx
BuildRequires:  python2-tenacity
BuildRequires:  python2-testresources
BuildRequires:  python2-sphinx
Requires:       python2-pbr >= 2.0.0
Requires:       python2-eventlet >= 0.18.2
Requires:       python2-netaddr >= 0.7.18
Requires:       python2-tenacity >= 4.4.0
Requires:       python2-six >= 1.10.0
Requires:       python2-oslo-i18n >= 3.15.3
Requires:       python2-oslo-log >= 3.36.0
Requires:       python2-oslo-serialization >= 2.18.0
Requires:       python2-oslo-service >= 1.24.0
Requires:       python2-oslo-utils >= 3.33.0
Requires:       python2-pyOpenSSL >= 17.1.0
Requires:       python-enum34

%description -n python2-%{pypi_name}
vmware-nsxlib is a common library that interfaces with VMware NSX


%package -n python2-%{pypi_name}-tests
Summary:    A common library that interfaces with VMware NSX - tests
Requires:   python2-%{pypi_name} = %{version}-%{release}

%description -n python2-%{pypi_name}-tests
A common library that interfaces with VMware NSX

This package contains the test files.


%package -n python-%{pypi_name}-doc
Summary:        vmware-nsxlib documentation
%description -n python-%{pypi_name}-doc
Documentation for vmware-nsxlib


%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        A common library that interfaces with VMware NSX
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-fixtures
BuildRequires:  python3-requests-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-subunit
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-devel
BuildRequires:  python3-hacking
BuildRequires:  python3-mock
BuildRequires:  python3-oslo-sphinx
BuildRequires:  python3-oslotest
BuildRequires:  python3-oslo-log
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-pbr
BuildRequires:  python3-sphinx
BuildRequires:  python3-tenacity
BuildRequires:  python3-testresources
Requires:       python3-pbr >= 2.0.0
Requires:       python3-eventlet >= 0.18.2
Requires:       python3-netaddr >= 0.7.18
Requires:       python3-tenacity >= 4.4.0
Requires:       python3-six >= 1.10.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-log >= 3.36.0
Requires:       python3-oslo-serialization >= 2.18.0
Requires:       python3-oslo-service >= 1.24.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-pyOpenSSL >= 17.1.0
%description -n python3-%{pypi_name}
vmware-nsxlib is a common library that interfaces with VMware NSX

%package -n python3-%{pypi_name}-tests
Summary:    A common library that interfaces with VMware NSX - tests
Requires:   python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}-tests
A common library that interfaces with VMware NSX

This package contains the test files.
%endif # with_python3

%description
vmware-nsxlib is a common library that interfaces with VMware NSX


%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Let's handle dependencies ourseleves
rm -f *requirements.txt
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install

%check
%if 0%{?with_python3}
%{__python3} setup.py test
rm -rf .testrepository
%endif
%{__python2} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{module}
%{python2_sitelib}/%{module}-*-py?.?.egg-info
%exclude %{python2_sitelib}/%{module}/tests

%files -n python2-%{pypi_name}-tests
%license LICENSE
%{python2_sitelib}/%{module}/tests

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-*-py?.?.egg-info
%exclude %{python3_sitelib}/%{module}/tests

%files -n python3-%{pypi_name}-tests
%license LICENSE
%{python3_sitelib}/%{module}/tests
%endif

%changelog
