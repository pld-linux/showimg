Summary:	Feature-rich image viewer, written for KDE 3.x
Summary(pl.UTF-8):	Bogata w możliwości przeglądarka plików graficznych dla KDE 3.x
Name:		showimg
Version:	0.9.5
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.jalix.org/projects/showimg/download/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	281c5f5e65ca14c69810d2099c43a4b8
Source1:	%{name}.desktop
Patch0:		kde-ac260.patch
Patch1:		kde-ac260-lt.patch
Patch2:		kde-am.patch
Patch3:		%{name}-link.patch
URL:		http://www.jalix.org/projects/showimg/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	digikam-devel
BuildRequires:	fam-devel
BuildRequires:	kdebase-devel >= 9:3.3
BuildRequires:	kdelibs-shared >= 9:3.3
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

%description -l pl.UTF-8
ShowImg jest bogatą w możliwości przeglądarką plików graficznych dla
KDE 3.x która potrafi wyświetlać wiele formatów, w tym JPEG, PNG, GIF
(animowany) i MNG. Posiada możliwość drzewiastego przeszukiwania
katalogów, podgląd plików z wielu katalogów i potrafi wyszukiwać
identyczne obrazki. Ponadto umożliwia prace w trybie pełnoekranowym,
powiększanie, sortowanie, operacje drag'n'drop i podgląd obrazków w
skompresowanych archiwach.

%package devel
Summary:        Header files for showimg
Summary(pl.UTF-8):      Pliki nagłówkowe showimg
Group:          Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description devel
Header files for showimg.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla showimg.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
	--enable-digiKam-plugin \
	--with-qt-libraries=%{_libdir} \
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
%attr(755,root,root) %{_bindir}/sidbtest
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/libshowimgcore.so.*.*.*
%attr(755,root,root) %{_libdir}/libshowimgkexidb.so.*.*.*
%attr(755,root,root) %{_libdir}/libshowimgkexidbparser.so.*.*.*
%attr(755,root,root) %{_libdir}/libshowimgkexisql2.*.*.*
%attr(755,root,root) %{_libdir}/libshowimgkexisql3.*.*.*
%attr(755,root,root) %{_libdir}/libshowimgkexiutils.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libshowimgcore.so.?
%attr(755,root,root) %ghost %{_libdir}/libshowimgkexidb.so.?
%attr(755,root,root) %ghost %{_libdir}/libshowimgkexidbparser.so.?
%attr(755,root,root) %ghost %{_libdir}/libshowimgkexisql2.so.?
%attr(755,root,root) %ghost %{_libdir}/libshowimgkexisql3.so.?
%attr(755,root,root) %ghost %{_libdir}/libshowimgkexiutils.so.?
%{_datadir}/apps/%{name}
%{_datadir}/mimelnk/image/*.desktop
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/apps/showimgpart
%{_datadir}/services/*.desktop
#%{_mandir}/man1/showimg.1*
%{_desktopdir}/kde/*.desktop
%{_datadir}/applnk/Graphics/showimg.desktop
%{_datadir}/servicetypes/showimg_kexidb_driver.desktop
%{_iconsdir}/hicolor/*/apps/*.png

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
