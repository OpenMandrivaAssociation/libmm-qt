%define         git_commit c5920e0

Name:           libmm-qt
Version:        0.6.0
Release:        2.20130613git%{git_commit}%{?dist}
Summary:        Qt-only wrapper for ModemManager DBus API
Group:          System/Libraries
License:        LGPLv2+
URL:            https://projects.kde.org/projects/extragear/libs/libmm-qt
# Package from git snapshots, create example:
# git clone git://anongit.kde.org/libmm-qt.git
# cd libmm-qt
# git archive --prefix=libmm-qt-%{version}/ master | bzip2 > ../%{name}-%{version}-git%{git_commit}.tar.bz2
Source0:        %{name}-%{version}-git%{git_commit}.tar.bz2

BuildRequires:  cmake >= 2.6
BuildRequires:  pkgconfig(QtCore)

Requires:  ModemManager >= 0.6.0

%description
Qt library for ModemManager

%package devel
Summary: Development files for %{name}
Group:   Development/C++
Requires: %{name} = %{version}-%{release}

%description devel
Qt libraries and header files for developing applications that use ModemManager

%prep
%setup -qn %{name}-%{version}-git%{git_commit}

%build
%cmake
%make

%install
make install/fast  DESTDIR=%{buildroot} -C build

%files
%doc README
%{_libdir}/libModemManagerQt.so.0*


%files devel
%{_libdir}/pkgconfig/ModemManagerQt.pc
%{_includedir}/ModemManagerQt/
%{_libdir}/libModemManagerQt.so

