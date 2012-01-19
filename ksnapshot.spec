%define		_state		stable
%define		orgname		ksnapshot
%define		qtver		4.8.0

Summary:	K Desktop Environment - Snap Shot
Summary(pl.UTF-8):	K Desktop Environment - Program do przechwytywania ekranu
Name:		ksnapshot
Version:	4.8.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	dfa82ee16987070b2150b9426dd2ac35
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libjpeg-devel
Obsoletes:	kde4-kdegraphics-ksnapshot < 4.6.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSnapshot is a simple application for taking screenshots. It is
capable of capturing images of either the whole desktop or just a
single window. The images can then be saved in a variety of formats.

%description -l pl.UTF-8
KSnapshot to prosta aplikacja do robienia zrzutów ekranu. Potrafi
przechwytywać obraz całego pulpitu lub tylko pojedynczego okna. Obrazy
mogą być następnie zapisane w wielu formatach.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksnapshot
%attr(755,root,root) %{_bindir}/kbackgroundsnapshot
%{_desktopdir}/kde4/ksnapshot.desktop
%{_iconsdir}/*/*/apps/ksnapshot.*
%{_datadir}/dbus-1/interfaces/org.kde.ksnapshot.xml
%{_kdedocdir}/en/ksnapshot
