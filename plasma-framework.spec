%define major 5
%define libname %mklibname KF5Plasma %{major}
%define devname %mklibname KF5Plasma -d
%define qlibname %mklibname KF5PlasmaQuick %{major}
%define qdevname %mklibname KF5PlasmaQuick -d
%define debug_package %{nil}

Name: plasma-framework
Version: 4.99.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: Plugin based UI runtime used to write primary user interfaces
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5Su)
BuildRequires: cmake(KDeclarative)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KdepimLibs)
BuildRequires: cmake(Gpgme)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(XCB)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(QCA2)
BuildRequires: cmake(DBusMenuQt)
BuildRequires: cmake(OpenGL)
BuildRequires: cmake(EGL)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
Plugin based UI runtime used to write primary user interfaces

%package -n %{libname}
Summary: Plugin based UI runtime used to write primary user interfaces
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Plugin based UI runtime used to write primary user interfaces

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Plasma-framework library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Plasma-framework library

%package -n %{qlibname}
Summary: Plugin based UI runtime used to write primary user interfaces with QML
Group: System/Libraries
Requires: %{libname} = %{EVRD}

%description -n %{qlibname}
Plugin based UI runtime used to write primary user interfaces with QML

%package -n %{qdevname}
Summary: Development files for PlasmaQuick
Group: Development/KDE and Qt
Requires: %{qlibname} = %{EVRD}
Requires: %{devname} = %{EVRD}

%description -n %{qdevname}
Development files for PlasmaQuick

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_bindir}/dpitest
%{_bindir}/plasmapkg2
%{_datadir}/plasma
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%{_libdir}/qml/org/kde/plasma
%{_libdir}/platformqml
%{_libdir}/plugins/*
%{_datadir}/dbus-1/*/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libKF5Plasma.so.%{major}
%{_libdir}/libKF5Plasma.so.%{version}

%files -n %{qlibname}
%{_libdir}/libKF5PlasmaQuick.so.%{major}
%{_libdir}/libKF5PlasmaQuick.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/libKF5Plasma.so
%{_libdir}/cmake/KF5Plasma

%files -n %{qdevname}
%{_libdir}/libKF5PlasmaQuick.so
%{_libdir}/cmake/KF5PlasmaQuick
