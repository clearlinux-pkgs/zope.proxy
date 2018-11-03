#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.proxy
Version  : 4.3.1
Release  : 19
URL      : https://files.pythonhosted.org/packages/7c/f5/e9ed65cdf8c93d24d7512ef89e21b241bc9ae75d90bc8608cc142f4c26f9/zope.proxy-4.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/7c/f5/e9ed65cdf8c93d24d7512ef89e21b241bc9ae75d90bc8608cc142f4c26f9/zope.proxy-4.3.1.tar.gz
Summary  : Generic Transparent Proxies
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.proxy-license = %{version}-%{release}
Requires: zope.proxy-python = %{version}-%{release}
Requires: zope.proxy-python3 = %{version}-%{release}
Requires: setuptools
Requires: zope.interface
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : zope.interface

%description
==============

%package dev
Summary: dev components for the zope.proxy package.
Group: Development
Provides: zope.proxy-devel = %{version}-%{release}

%description dev
dev components for the zope.proxy package.


%package license
Summary: license components for the zope.proxy package.
Group: Default

%description license
license components for the zope.proxy package.


%package python
Summary: python components for the zope.proxy package.
Group: Default
Requires: zope.proxy-python3 = %{version}-%{release}

%description python
python components for the zope.proxy package.


%package python3
Summary: python3 components for the zope.proxy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.proxy package.


%prep
%setup -q -n zope.proxy-4.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541281624
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.proxy
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.proxy/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/python3.7m/zope.proxy/proxy.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.proxy/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
