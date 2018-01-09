%define major 5
%define libname %mklibname KF5PimTextEdit %{major}
%define devname %mklibname KF5PimTextEdit -d

Name: kpimtextedit
Version: 17.12.1
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release: 1
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: Text editing library for KDE PIM
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Grantlee5)
BuildRequires: cmake(KF5Emoticons)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5SyntaxHighlighting)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Designer)
BuildRequires: cmake(KF5DesignerPlugin)
BuildRequires: cmake(Qt5UiPlugin)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Gui)
%if %mdvver > 3000000
BuildRequires: cmake(Qt5TextToSpeech)
%endif

%description
Text editing library for KDE PIM.

%package -n %{libname}
Summary: KDE PIM library for text editing
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE PIM library for text editing.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package designer-devel
Summary: Qt Designer integration for %{name}
Group: Development/KDE and Qt
Requires: %{devname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkpimtextedit

%files -f libkpimtextedit.lang
%{_sysconfdir}/xdg/kpimtextedit.categories

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files designer-devel
%{_libdir}/qt5/plugins/designer/kpimtexteditwidgets.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
