%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

# TODO(jpena): There is no python3-neutron-lib yet, so let's skip python3 for now
%if 0%{?fedora} >= 24
%global with_python3 0
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
BuildRequires:  python-fixtures
BuildRequires:  python-requests-mock
BuildRequires:  python-setuptools
BuildRequires:  python-subunit
BuildRequires:  python-testrepository
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools
BuildRequires:  python-coverage
BuildRequires:  python2-devel
BuildRequires:  python-hacking
BuildRequires:  python-mock
BuildRequires:  python-neutron-lib
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-oslotest
BuildRequires:  python-pbr
BuildRequires:  python-reno
BuildRequires:  python-sphinx
BuildRequires:  python-tenacity
BuildRequires:  python-testresources
BuildRequires:  python-sphinx
Requires:       python-pbr >= 1.8
Requires:       python-eventlet >= 0.18.2
Requires:       python-netaddr >= 0.7.13
Requires:       python-tenacity >= 3.2.1
Requires:       python-six >= 1.9.0
Requires:       python-neutron-lib >= 1.1.0
Requires:       python-oslo-i18n >= 2.1.0
Requires:       python-oslo-log >= 3.11.0
Requires:       python-oslo-serialization >= 1.10.0
Requires:       python-oslo-service >= 1.10.0
Requires:       python-oslo-utils >= 3.18.0
Requires:       pyOpenSSL >= 0.14
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
BuildRequires:  python3-coverage
BuildRequires:  python3-devel
BuildRequires:  python3-hacking
BuildRequires:  python3-mock
BuildRequires:  python3-neutron-lib
BuildRequires:  python3-oslo-sphinx
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-reno
BuildRequires:  python3-sphinx
BuildRequires:  python3-tenacity
BuildRequires:  python3-testresources
Requires:       python3-pbr >= 1.8
Requires:       python3-eventlet >= 0.18.2
Requires:       python3-netaddr >= 0.7.13
Requires:       python3-tenacity >= 3.2.1
Requires:       python3-six >= 1.9.0
Requires:       python3-neutron-lib >= 1.1.0
Requires:       python3-oslo-i18n >= 2.1.0
Requires:       python3-oslo-log >= 3.11.0
Requires:       python3-oslo-serialization >= 1.10.0
Requires:       python3-oslo-service >= 1.10.0
Requires:       python3-oslo-utils >= 3.18.0
Requires:       python3-pyOpenSSL >= 0.14
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
