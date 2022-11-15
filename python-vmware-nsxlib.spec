%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name vmware-nsxlib
%global module vmware_nsxlib
# oslosphinx do not work with sphinx > 2
%global with_doc 0

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        A common library that interfaces with VMware NSX

License:        ASL 2.0
URL:            https://github.com/openstack/vmware-nsxlib
Source0:        https://tarballs.opendev.org/x/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.opendev.org/x/%{pypi_name}/%{pypi_name}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

%description
vmware-nsxlib is a common library that interfaces with VMware NSX

%package -n     python3-%{pypi_name}
Summary:        A common library that interfaces with VMware NSX
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  git-core
BuildRequires:  python3-fixtures
BuildRequires:  python3-setuptools
BuildRequires:  python3-subunit
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-devel
BuildRequires:  python3-hacking
BuildRequires:  python3-mock
BuildRequires:  python3-oslotest
BuildRequires:  python3-oslo-log
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-oslo-service
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-pbr
BuildRequires:  python3-sphinx
BuildRequires:  python3-tenacity
BuildRequires:  python3-testresources
Requires:       python3-pbr >= 4.0.0
Requires:       python3-eventlet >= 0.24.1
Requires:       python3-netaddr >= 0.7.18
Requires:       python3-tenacity >= 6.0.0
Requires:       python3-oslo-i18n >= 3.20.0
Requires:       python3-oslo-log >= 4.2.1
Requires:       python3-oslo-serialization >= 2.28.1
Requires:       python3-oslo-service >= 1.31.0
Requires:       python3-oslo-utils >= 4.4.0
Requires:       python3-pyOpenSSL
Requires:       python3-cryptography

BuildRequires:  python3-requests-mock
BuildRequires:  python3-decorator
Requires:       python3-decorator

%description -n python3-%{pypi_name}
vmware-nsxlib is a common library that interfaces with VMware NSX


%package -n python3-%{pypi_name}-tests
Summary:    A common library that interfaces with VMware NSX - tests
Requires:   python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}-tests
A common library that interfaces with VMware NSX

This package contains the test files.


%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        vmware-nsxlib documentation

BuildRequires:  python3-oslo-sphinx
BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for vmware-nsxlib
%endif


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git
# Let's handle dependencies ourseleves
rm -f *requirements.txt
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{py3_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%check
stestr-3 run

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-*-py%{python3_version}.egg-info
%exclude %{python3_sitelib}/%{module}/tests

%files -n python3-%{pypi_name}-tests
%license LICENSE
%{python3_sitelib}/%{module}/tests

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html
%endif

%changelog
