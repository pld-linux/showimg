Summary:	Feature-rich image viewer, written for KDE 3.x
Summary(pl):	Bogata w mo¿liwo¶ci przegl±darka plików graficznych dla KDE 3.x
Name:		showimg
Version:	0.9.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.jalix.org/projects/%{name}/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	4f20944114d0f1f6e4d6588578ac823b
URL:		http://www.jalix.org/projects/showimg/
BuildRequires:	automake
BuildRequires:	digikam-devel
BuildRequires:	fam-devel
BuildRequires:	kdebase-devel >= 3.0
BuildRequires:	libart_lgpl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
ShowImg is a feature-rich image viewer, written for KDE3.x, which can
display numerous formats, including JPEG, PNG, GIF (animated) and MNG.
It can preview and display images from multiple directories and search
for identical images. ShowImg also features a full-screen mode,
zooming, sorting, drag'n'drop with Konqueror, and support for images
in compressed archives (.zip).

%description -l pl
ShowImg jest bogat± w mo¿liwo¶ci przegl±dark± plików graficznych dla
KDE 3.x która potrafi wy¶wietlaæ wiele formatów, w tym JPEG, PNG, GIF
(animowany) i MNG. Posiada mo¿liwo¶æ drzewiastego przeszukiwania
katalogów, podgl±d plików z wielu katalogów i potrafi wyszukiwaæ
identyczne obrazki. Ponadto umo¿liwia prace w trybie pe³noekranowym,
powiêkszanie, sortowanie, operacje drag'n'drop i podgl±d obrazków w
skompresowanych archiwach.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	--enable-digiKam-plugin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
mv $RPM_BUILD_ROOT/usr/share/applnk/Graphics/*.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde
echo 'Categories=Viewer;' >> $RPM_BUILD_ROOT%{_desktopdir}/kde/%{name}.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/apps/%{name}
%{_datadir}/mimelnk/image/*.desktop
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_mandir}/man1/showimg.1*
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png 
