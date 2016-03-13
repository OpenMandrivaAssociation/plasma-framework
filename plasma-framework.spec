%define major 5
%define libname %mklibname KF5Plasma %{major}
%define devname %mklibname KF5Plasma -d
%define qlibname %mklibname KF5PlasmaQuick %{major}
%define qdevname %mklibname KF5PlasmaQuick -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma-framework
Version: 5.20.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Plugin based UI runtime used to write primary user interfaces
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-composite)
BuildRequires: pkgconfig(xcb-damage)
BuildRequires: pkgconfig(xcb-render)
BuildRequires: pkgconfig(xcb-shape)
BuildRequires: pkgconfig(xcb-xfixes)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5Su)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5Package)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(dbusmenu-qt5)
Requires: %{libname} = %{EVRD}

%description
Plugin based UI runtime used to write primary user interfaces.

%package -n %{libname}
Summary: Plugin based UI runtime used to write primary user interfaces
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Plugin based UI runtime used to write primary user interfaces.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Plasma-framework library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}
Requires: %{qlibname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Plasma-framework library.

%package -n %{qlibname}
Summary: Plugin based UI runtime used to write primary user interfaces with QML
Group: System/Libraries
Requires: %{libname} = %{EVRD}

%description -n %{qlibname}
Plugin based UI runtime used to write primary user interfaces with QML.

%package -n %{qdevname}
Summary: Development files for PlasmaQuick
Group: Development/KDE and Qt
Requires: %{qlibname} = %{EVRD}
Requires: %{devname} = %{EVRD}

%description -n %{qdevname}
Development files for PlasmaQuick.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang libplasma5

%files -f libplasma5.lang
%{_bindir}/plasmapkg2
%{_datadir}/plasma
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%{_libdir}/qt5/qml/org/kde/plasma
%{_libdir}/qt5/qml/QtQuick/Controls/Styles/Plasma
%{_libdir}/qt5/plugins/*
%{_mandir}/man1/*
%lang(lt) %{_datadir}/locale/lt/LC_SCRIPTS/libplasma5

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
%{_datadir}/kdevappwizard/templates/*
