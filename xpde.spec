# TODO: move kylix runtime into separate rpm (in kylix.spec)
#	fix FHS-incompliance (/usr/themes, /usr/bin/apps/*)
#	is it noarch (*.so???) or should be compiled???
#
%define subver 20030315
Summary:	XP-like desktop environment
Summary(pl):	¦rodowisko graficzne podobne do XP
Name:		xpde
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xpde.com/dist2/%{name}-%{version}-%{subver}.tar.gz
URL:		http://www.xpde.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's a desktop environment (XPde) and a window manager (XPwm) for
Linux. It tries to recreate the Windows XP interface to-the-pixel
point. Nothing more, no clipboard compatibility between Gtk and Qt
applications, no emulation of Windows applications, no unification on
the widgets of X applications, just a desktop environment and a window
manager.

%description -l pl
Jest to ¶rodowisko graficzne (XPde) oraz zarz±dca okien (XPwm) dla
Linuksa. Próbuje on odtworzyæ interfejs Windows XP na poziomie
pikseli. Nie zawiera nic wiêcej: brak zgodno¶ci schowka pomiêdzy
aplikacjami Gtk i Qt, nie emuluje aplikacji Windows, nie unifikuje
kontrolek aplikacji X. Po prostu ¶rodowisko graficzne i zarz±dca
okien.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_bindir}

#install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/apps
#install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/applets

install -d $RPM_BUILD_ROOT%{_bindir}/apps
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/applets
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/doc
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/icons
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/themes

# FIXME: wrong location
install -d $RPM_BUILD_ROOT/usr/themes

#mkdir "/opt/xpde"
#mkdir "/opt/xpde/bin"
#mkdir "/opt/xpde/bin/apps"
#mkdir "/opt/xpde/bin/applets"
#
#mkdir "/opt/xpde/share"
#mkdir "/opt/xpde/share/apps"
#mkdir "/opt/xpde/share/applets"
#mkdir "/opt/xpde/share/doc"
#mkdir "/opt/xpde/share/fonts"
#mkdir "/opt/xpde/share/icons"
#
#mkdir "/opt/xpde/themes"

# FIXME: wrong location
cp -r themes $RPM_BUILD_ROOT/usr
cp -r defaultdesktop $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r doc/* $RPM_BUILD_ROOT%{_datadir}/%{name}/doc
cp *.so* $RPM_BUILD_ROOT%{_libdir}
cp XPde $RPM_BUILD_ROOT%{_bindir}
cp XPwm $RPM_BUILD_ROOT%{_bindir}

cp DateTimeProps $RPM_BUILD_ROOT%{_datadir}/%{name}/applets
cp appexec $RPM_BUILD_ROOT%{_datadir}/%{name}/applets
cp networkstatus $RPM_BUILD_ROOT%{_datadir}/%{name}/applets
cp networkproperties $RPM_BUILD_ROOT%{_datadir}/%{name}/applets
cp xpsu $RPM_BUILD_ROOT%{_datadir}/%{name}/applets
cp mouse $RPM_BUILD_ROOT%{_datadir}/%{name}/applets
cp keyboard $RPM_BUILD_ROOT%{_datadir}/%{name}/applets
cp regional $RPM_BUILD_ROOT%{_datadir}/%{name}/applets
cp desk $RPM_BUILD_ROOT%{_datadir}/%{name}/applets

# FIXME: wrong location
cp taskmanager $RPM_BUILD_ROOT%{_bindir}/apps
cp notepad $RPM_BUILD_ROOT%{_bindir}/apps
cp calculator $RPM_BUILD_ROOT%{_bindir}/apps
cp fileexplorer $RPM_BUILD_ROOT%{_bindir}/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc
# FIXME: wrong location
%attr(755,root,root) %{_bindir}/apps/*
%attr(755,root,root) %{_bindir}/XP*
%attr(755,root,root) %{_libdir}/*

%{_datadir}/%{name}
# FIXME: wrong location
/usr/themes
