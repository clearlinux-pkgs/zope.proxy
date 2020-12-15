#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.proxy
Version  : 4.3.5
Release  : 35
URL      : https://files.pythonhosted.org/packages/ab/37/26899cb231ecfa04822a17a669eac6df7ef0c2a86e2b78001db0cd3edd46/zope.proxy-4.3.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/ab/37/26899cb231ecfa04822a17a669eac6df7ef0c2a86e2b78001db0cd3edd46/zope.proxy-4.3.5.tar.gz
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
================
``zope.proxy``
================
.. image:: https://img.shields.io/pypi/v/zope.proxy.svg
:target: https://pypi.python.org/pypi/zope.proxy/
:alt: Latest Version

%package dev
Summary: dev components for the zope.proxy package.
Group: Development
Provides: zope.proxy-devel = %{version}-%{release}
Requires: zope.proxy = %{version}-%{release}
Requires: zope.proxy = %{version}-%{release}

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
Provides: pypi(zope.proxy)
Requires: pypi(setuptools)
Requires: pypi(zope.interface)

%description python3
python3 components for the zope.proxy package.


%prep
%setup -q -n zope.proxy-4.3.5
cd %{_builddir}/zope.proxy-4.3.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584378847
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.proxy
cp %{_builddir}/zope.proxy-4.3.5/LICENSE.txt %{buildroot}/usr/share/package-licenses/zope.proxy/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/python3.8/zope.proxy/proxy.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.proxy/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
