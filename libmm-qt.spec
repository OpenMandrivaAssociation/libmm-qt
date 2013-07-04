%define git_commit c5920e0
%define snapshot 20130613

%define major 0
%define libname %mklibname mm-qt %{major}
%define devname %mklibname -d mm-qt

Summary:	Qt-only wrapper for ModemManager DBus API
Name:		libmm-qt
Version:	0.6.0
Release:	3.%{snapshot}.1
Group:		System/Libraries
License:	LGPLv2+
Url:		https://projects.kde.org/projects/extragear/libs/libmm-qt
# Package from git snapshots, create example:
# git clone git://anongit.kde.org/libmm-qt.git
# cd libmm-qt
# git archive --prefix=libmm-qt-%{version}/ master | bzip2 > ../%{name}-%{version}-git%{git_commit}.tar.bz2
Source0:	%{name}-%{version}-git%{git_commit}.tar.bz2
BuildRequires:	cmake
BuildRequires:	pkgconfig(QtCore)

%description
Qt library for ModemManager.

%package -n %{libname}
Summary:	Qt-only wrapper for ModemManager DBus API
Group:		System/Libraries

%description -n %{libname}
Qt library for ModemManager.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Qt libraries and headers for developing applications that use ModemManager.

%prep
%setup -qn %{name}-%{version}-git%{git_commit}

%build
%cmake
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/libModemManagerQt.so.%{major}*

%files -n %{devname}
%doc README
%{_libdir}/pkgconfig/ModemManagerQt.pc
%{_includedir}/ModemManagerQt/
%{_libdir}/libModemManagerQt.so

