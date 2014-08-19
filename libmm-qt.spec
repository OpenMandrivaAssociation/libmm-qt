%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define major 0
%define libname %mklibname ModemManagerQt %{major}
%define devname %mklibname -d ModemManagerQt

Summary:	Qt-only wrapper for ModemManager DBus API
Name:		libmm-qt
Version:	1.0.1
Release:	3
Epoch:		1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://projects.kde.org/projects/extragear/libs/libmm-qt
Source0:	ftp://ftp.kde.org/pub/kde/unstable/modemmanager-qt/1.0.0/src/%{name}-%{version}-1.tar.xz
BuildRequires:	cmake
BuildRequires:	pkgconfig(ModemManager)
BuildRequires:	pkgconfig(QtCore)

%description
Qt library for ModemManager.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Qt-only wrapper for ModemManager DBus API
Group:		System/Libraries
Conflicts:	%{_lib}mm-qt0 < 1:0.5.0
Obsoletes:	%{_lib}mm-qt0 < 1:0.5.0

%description -n %{libname}
Qt library for ModemManager.

%files -n %{libname}
%{_libdir}/libModemManagerQt.so.%{major}
%{_libdir}/libModemManagerQt.so.%{version}

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Requires:	pkgconfig(ModemManager)
Conflicts:	%{_lib}mm-qt-devel < 1:0.5.0
Obsoletes:	%{_lib}mm-qt-devel < 1:0.5.0

%description -n %{devname}
Qt libraries and headers for developing applications that use ModemManager.

%files -n %{devname}
%doc README
%{_libdir}/pkgconfig/ModemManagerQt.pc
%{_includedir}/ModemManagerQt/
%{_libdir}/libModemManagerQt.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

