#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.proxy
Version  : 4.3.0
Release  : 15
URL      : https://pypi.debian.net/zope.proxy/zope.proxy-4.3.0.tar.gz
Source0  : https://pypi.debian.net/zope.proxy/zope.proxy-4.3.0.tar.gz
Summary  : Generic Transparent Proxies
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.proxy-python3
Requires: zope.proxy-license
Requires: zope.proxy-python
Requires: Sphinx
Requires: setuptools
Requires: zope.interface
Requires: zope.security
Requires: zope.testrunner
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : zope.interface

%description
==============

%package dev
Summary: dev components for the zope.proxy package.
Group: Development
Provides: zope.proxy-devel

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
Requires: zope.proxy-python3

%description python
python components for the zope.proxy package.


%package python3
Summary: python3 components for the zope.proxy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.proxy package.


%prep
%setup -q -n zope.proxy-4.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530324804
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/zope.proxy
cp LICENSE.txt %{buildroot}/usr/share/doc/zope.proxy/LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/python3.7m/zope.proxy/proxy.h

%files license
%defattr(-,root,root,-)
/usr/share/doc/zope.proxy/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
