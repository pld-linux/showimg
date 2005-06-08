Summary:	Feature-rich image viewer, written for KDE 3.x
Summary(pl):	Bogata w mo¿liwo¶ci przegl±darka plików graficznych dla KDE 3.x
Name:		showimg
%define	ver	0.9.4-1
%define	rver	%(echo %{ver} | tr - .)
Version:	%{rver}
Release:	0.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.jalix.org/projects/showimg/download/%{ver}/%{name}-%{ver}.tar.bz2
# Source0-md5:	d6cebe9a627aaa4f0ec57e95f403d5fa
Source1:	%{name}.desktop
Patch0:		%{name}-qslider.patch
URL:		http://www.jalix.org/projects/showimg/
BuildRequires:	automake
BuildRequires:	digikam-devel
BuildRequires:	fam-devel
BuildRequires:	kdebase-devel >= 3.0
BuildRequires:	libart_lgpl-devel
BuildRequires:	libkexif-devel >= 0.2
BuildRequires:	libkipi-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -n %{name}-%{ver}
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	--enable-digiKam-plugin \
	--with-qt-libraries=%{_libdir} \
	--enable-final \
	--disable-debug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/kde/%{name}.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_datadir}/apps/%{name}
%{_datadir}/mimelnk/image/*.desktop
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/apps/showimgpart
%{_datadir}/services/*.desktop
%{_mandir}/man1/showimg.1*
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
