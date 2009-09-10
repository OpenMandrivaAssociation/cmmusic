Summary:	Console Mplayer Music
Name:	  	cmmusic
Version:	1.5
Release:	%mkrel 2
License:	GPLv2+
Group:		Sound
Source0: 	http://downloads.sourceforge.net/cmmusic/%name-%version-src.tar.gz
Patch0:		cmmusic-1.5-gcc43.patch
URL:		http://cmmusic.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ncursesw-devel
BuildRequires:	ncurses-devel
BuildRequires:	gtk+2-devel
Requires:	mplayer

%description
A front looks like xmms of mplayer which base on console user interface
for Linux. It may include control, list or event lirc panel and supports
keyboard and mouse.

%package gtk
Summary:	Console Mplayer Music - gtk plugin
Group:		Sound
Requires:	%name = %version

%description gtk
This package contains gtk plugin of cmmusic.

%prep
%setup -qc -n %name-%version
tar xfz %name-%version.tar.gz
tar xfz %name-plugin-%version.tar.gz
tar xfz %name-plugin-gtk-%version.tar.gz

cd %name-plugin-%version
%patch0 -p0
cd -

%build
pushd %name-%version
%configure2_5x
%make
popd

pushd %name-plugin-%version
%configure2_5x
%make
popd

pushd %name-plugin-gtk-%version
%configure2_5x
%make
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd %name-%version
%makeinstall_std
popd

pushd %name-plugin-%version
%makeinstall_std
popd

pushd %name-plugin-gtk-%version
%makeinstall_std
popd

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/*
%{_datadir}/%name
%exclude %{_datadir}/%name/plugins/proj1

%files gtk
%defattr(-, root, root)
%{_datadir}/%name/plugins/proj1
