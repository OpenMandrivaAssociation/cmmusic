Summary:	Console Mplayer Music
Name:	  	cmmusic
Version:	1.5
Release:	4
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

find . -name "*.cpp" -exec chmod a-x {} \;
find . -name "*.c" -exec chmod a-x {} \;
find . -name "*.h" -exec chmod a-x {} \;

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
pushd %name-%version
%makeinstall_std
popd

pushd %name-plugin-%version
%makeinstall_std
popd

pushd %name-plugin-gtk-%version
%makeinstall_std
popd

%files
%defattr(-, root, root)
%{_bindir}/*
%{_datadir}/%name
%exclude %{_datadir}/%name/plugins/proj1

%files gtk
%defattr(-, root, root)
%{_datadir}/%name/plugins/proj1


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5-3mdv2011.0
+ Revision: 617073
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.5-2mdv2010.0
+ Revision: 437058
- rebuild

* Mon Mar 23 2009 Funda Wang <fwang@mandriva.org> 1.5-1mdv2009.1
+ Revision: 360605
- import cmmusic


