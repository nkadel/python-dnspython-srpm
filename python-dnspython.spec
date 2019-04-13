#
# spec file for package python-dnspython
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL does not include python3 by default
#%if 0%{?fedora} || 0%{?rhel} > 7
%if 0%{?fedora} || 0%{?rhel} > 6
%global with_python3 1
%else
%global with_python3 0
%endif

# Fedora > 28 no longer publishes python2 by default
%if 0%{?fedora} > 28
%global with_python2 0
%else
%global with_python2 1
%endif

# Use Python 3.6, not 3.4
%if 0%{?rhel} == 7
%global __python3 /usr/bin/python3.6
%endif

# Common SRPM package
Name:           python-dnspython
Version:        1.16.0
Release:        0%{?dist}
Url:            http://www.dnspython.org
Summary:        DNS toolkit
License:        BSD-like (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/d/dnspython/dnspython-%{version}.zip
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{with_python2}
%if 0%{?rhel}
# Use non-specific names for RHEL
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%else
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif # rhel
%endif # with_python2
%if 0%{with_python3}
%if 0%{?rhel} == 7
BuildRequires:  python36-devel
BuildRequires:  python36-setuptools
%else
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif # rhel == 7
%endif # with_python3

%if 0%{with_python2}
%package -n python2-dnspython
Version:        1.16.0
Release:        0%{?dist}
Url:            http://www.dnspython.org
Summary:        DNS toolkit
License:        BSD-like (FIXME:No SPDX)
%{?python_provide:%python_provide python2-dnspython}
# Added for RHEL with python-dnspython
Obsoletes: python-dnspython < %{version}-%{release}
%endif # with_python2

%if 0%{with_python3}
%package -n python3-dnspython
Version:        1.16.0
Release:        0%{?dist}
Url:            http://www.dnspython.org
Summary:        DNS toolkit
License:        BSD-like (FIXME:No SPDX)
# macro is broken for python3 and rhel 7
%if 0%{?rhel} != 7
%{?python_provide:%python_provide python3-dnspython}
%endif
%endif # with_python3

%description
dnspython is a DNS toolkit for Python. It supports almost all
record types. It can be used for queries, zone transfers, and dynamic
updates.  It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set.  The low level classes allow
direct manipulation of DNS zones, messages, names, and records.



%if 0%{with_python2}
%description -n python2-dnspython
dnspython is a DNS toolkit for Python. It supports almost all
record types. It can be used for queries, zone transfers, and dynamic
updates.  It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set.  The low level classes allow
direct manipulation of DNS zones, messages, names, and records.


%endif # with_python2

%if 0%{with_python3}
%description -n python3-dnspython
dnspython is a DNS toolkit for Python. It supports almost all
record types. It can be used for queries, zone transfers, and dynamic
updates.  It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set.  The low level classes allow
direct manipulation of DNS zones, messages, names, and records.


%endif # with_python3

%prep
%setup -q -n dnspython-%{version}

%build
%if 0%{with_python2}
%py2_build
%endif # with_python2
%if 0%{with_python3}
%py3_build
%endif # with_python3

%install
%if 0%{with_python2}
%py2_install
%if ! 0%{with_python3}
%endif # ! with_python3
%endif # with_python2
%if 0%{with_python3}

%py3_install
%endif # with_python3

%clean
rm -rf %{buildroot}

%if 0%{with_python2}
%files -n python2-dnspython
%defattr(-,root,root,-)
%{python2_sitelib}/*
%endif # with_python2

%if 0%{with_python3}
%files -n python3-dnspython
%defattr(-,root,root,-)
%{python3_sitelib}/*
%endif # with_python3

%changelog
* Sat Apr 13 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.16.0-0
- Create python2 and python3 RPMs with py2pack
- Add Obsolete line for old "python-" package on RHEL

