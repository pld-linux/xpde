
%define 	snapdate	20030506
%define		xpdedir		%{_datadir}/xpde

Summary:	XP-like desktop environment
Summary(pl.UTF-8):	Środowisko graficzne podobne do XP
Name:		xpde
Version:	0.5.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xpde.com/releases/%{name}-%{version}.tar.gz
# Source0-md5:	d75bbfa3949f9de30a525d6c785e6a53
Source1:	startxpde
#Patch0:		%{name}-paths.patch
Patch1:		%{name}-ns.patch
URL:		http://www.xpde.com/
BuildRequires:	kylix >= 3
BuildRequires:	patchutils
Requires:	kylix3_open-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's a desktop environment (XPde) and a window manager (XPwm) for
Linux. It tries to recreate the Windows XP interface to-the-pixel
point. Nothing more, no clipboard compatibility between Gtk and Qt
applications, no emulation of Windows applications, no unification on
the widgets of X applications, just a desktop environment and a window
manager.

%description -l pl.UTF-8
Jest to środowisko graficzne (XPde) oraz zarządca okien (XPwm) dla
Linuksa. Próbuje on odtworzyć interfejs Windows XP na poziomie
pikseli. Nie zawiera nic więcej: brak zgodności schowka pomiędzy
aplikacjami Gtk i Qt, nie emuluje aplikacji Windows, nie unifikuje
kontrolek aplikacji X. Po prostu środowisko graficzne i zarządca
okien.

%prep
%setup -q -n xpde
#%patch0 -p1
#%patch1 -p1
#cp %{PATCH1} xpde-ns.patch
#splitdiff -a xpde-ns.patch
#P=`ls xpde-ns.patch.part*`
#for F in $P
#do
#	F2P=`cat $F | head -n 1 | awk -F "\\t" '{ gsub("^.*xpde.orig/", ""); print $1 }'`
#	patch -p1 "$F2P" $F
#done

%build
KLX=/usr/share/kylix3_open
export KLX

OUT=$RPM_BUILD_DIR/xpde/out
mkdir -p $OUT
rm -f $OUT/*
LD_LIBRARY_PATH=$OUT
export LD_LIBRARY_PATH

COMP="-LUrtl:visualclx:XPRegistry:XPCommon:XPAPI:XPMenus:XPTrayIcon:XPStyle:XPColorSelect:XPShellControls:XPCommctrls"

build_prj() {
OLDPATH=`pwd`
DIR=`dirname $1`
PRJ=`basename $1`
shift

cd $DIR
OPTS="-B -LE$OUT -LN$OUT -O$OUT -E$OUT -N$OUT -U$OUT:$KLX/lib $@"
dcc $PRJ $OPTS
cp -f *.xfm $OUT ||:

cd $OLDPATH
}

build_prj src/components/XPRegistry/XPRegistry.dpk
build_prj xpde/src/common/XPCommon.dpk
build_prj xpde/src/components/menu/XPMenus.dpk
build_prj xpde/src/components/style/XPStyle.dpk
build_prj xpde/src/components/colorselect/XPColorSelect.dpk
build_prj xpde/src/components/commctrls/XPCommctrls.dpk
build_prj xpde/src/components/toolsapi/XPAPI.dpk
build_prj xpde/src/components/shellcontrols/XPShellControls.dpk
build_prj xpde/src/components/trayicon/XPTrayIcon.dpk

build_prj xpde/src/core/xpde/XPde.dpr $COMP
build_prj xpde/src/core/xpwm/XPwm.dpr $COMP
build_prj xpde/src/applets/DateTimeProps/DateTimeProps.dpr $COMP
build_prj xpde/src/applets/INetDial/INetDial.dpr $COMP
build_prj xpde/src/applets/desk/desk.dpr $COMP
build_prj xpde/src/applets/keyboard/keyboard.dpr $COMP
build_prj xpde/src/applets/mouse/mouse.dpr $COMP
build_prj xpde/src/applets/regional/regional.dpr $COMP
build_prj xpde/src/applets/xpsu/xpsu.dpr $COMP
build_prj xpde/src/applets/xpuser/xpuser.dpr $COMP
build_prj xpde/src/apps/appexec/appexec.dpr $COMP
build_prj xpde/src/apps/calculator/calculator.dpr $COMP
build_prj xpde/src/apps/fileexplorer/fileexplorer.dpr $COMP
build_prj xpde/src/apps/networkproperties/networkproperties.dpr $COMP
build_prj xpde/src/apps/networkstatus/networkstatus.dpr $COMP
build_prj xpde/src/apps/notepad/notepad.dpr $COMP
build_prj xpde/src/apps/taskmanager/taskmanager.dpr $COMP
build_prj xpde/src/components/trayicon/demo/traydemo.dpr $COMP
build_prj xpde/src/setup/XPdesetup.dpr $COMP
build_prj xpde/src/tools/resourceeditor/ResourceEditor.dpr $COMP
build_prj xpde/src/tools/translator/Translator.dpr $COMP
build_prj xpuser/xpuser.dpr $COMP

%install
rm -rf $RPM_BUILD_ROOT

OUT=$RPM_BUILD_DIR/xpde/out

install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{xpdedir}/{fonts,icons}
install -d $RPM_BUILD_ROOT%{xpdedir}/defaultdesktop/Desktop

cp -r xpde/themes $RPM_BUILD_ROOT%{xpdedir}
cp -r xpde/defaultdesktop $RPM_BUILD_ROOT%{xpdedir}

cp $OUT/*.so* $RPM_BUILD_ROOT%{_libdir}
APPS=`ls $OUT/* | grep -v "\."`
cp $APPS $RPM_BUILD_ROOT%{_bindir}

cp %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/startxpde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc xpde/doc/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{xpdedir}
