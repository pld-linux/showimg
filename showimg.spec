Summary:	Feature-rich image viewer, written for KDE 3.x
Summary(pl):	Bogata w mo�liwo�ci przegl�darka plik�w graficznych dla KDE 3.x
Name:		showimg
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.jalix.org/projects/%{name}/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	68444224f8b2c44766a89116e62d554b
URL:		http://www.jalix.org/projects/showimg/
BuildRequires:  digikam-devel
BuildRequires:	fam-devel
BuildRequires:	kdebase-devel >= 3.0
BuildRequires:  libart_lgpl-devel
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
ShowImg jest bogat� w mo�liwo�ci przegl�dark� plik�w graficznych dla
KDE 3.x kt�ra potrafi wy�wietla� wiele format�w, w tym JPEG, PNG, GIF
(animowany) i MNG. Posiada mo�liwo�� drzewiastego przeszukiwania
katalog�w, podgl�d plik�w z wielu katalog�w i potrafi wyszukiwa�
identyczne obrazki. Ponadto umo�liwia prace w trybie pe�noekranowym,
powi�kszanie, sortowanie, operacje drag'n'drop i podgl�d obrazk�w w
skompresowanych archiwach.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
%configure \
    --enable-digiKam-plugin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
mv $RPM_BUILD_ROOT/usr/share/applnk/Graphics/*.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde

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
%{_desktopdir}/kde/*desktop
%{_iconsdir}/hicolor/*/apps/*.png 
