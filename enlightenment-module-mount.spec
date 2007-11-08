%define		_module_name	mount
%define		_snap	20060419
Summary:	Enlightenment DR17 module: mount
Summary(pl.UTF-8):	Moduł Enlightenmenta DR17: mount
Name:		enlightenment-module-%{_module_name}
Version:	0.0.7
Release:	0.%{_snap}_1
License:	BSD
Group:		X11/Window Managers/Tools
#Source0:	http://www.get-e.org/Resources/Modules/_files/%{_module_name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e_modules/%{_module_name}-%{_snap}.tar.bz2
# Source0-md5:	1ea6c7e90ac62b84605755692b58411d
URL:		http://www.get-e.org/Resources/Modules/
Patch0:		%{name}-nfs.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	enlightenment-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
Requires:	enlightenment
Requires:	fonts-TTF-bitstream-vera
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mount module for Enlightenment DR17 makes easy mounting file systems
with "user" option in /etc/fstab.

%description -l pl.UTF-8
Moduł mount dla Enlightenmenta DR17 ułatwia montowanie systemów plików
z opcją "user" w /etc/fstab.

%prep
%setup -q -n %{_module_name}
%patch0 -p1
sed -e 's|$MOUNT|/bin/mount|'	\
    -e 's|$UMOUNT|/bin/umount|'	\
    -e 's|$EJECT|%{_bindir}/eject|'	\
    -e 's|datadir=.*|datadir="`enlightenment-config --module-dir`/${PACKAGE}"|' \
    -e '/PACKAGE_DATA_DIR/s|"[^"]*"|"`enlightenment-config --module-dir`/${PACKAGE}"|' \
    -i configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_datadir}/fonts/TTF/VeraBd.ttf \
	$RPM_BUILD_ROOT%{_libdir}/enlightenment/modules_extra/%{_module_name}/VeraBd.ttf

%find_lang mount

%clean
rm -rf $RPM_BUILD_ROOT

%files -f mount.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*/module.so
# violates FHS
%{_libdir}/enlightenment/modules_extra/%{_module_name}/VeraBd.ttf
%{_libdir}/enlightenment/modules_extra/%{_module_name}/%{_module_name}.*
%{_libdir}/enlightenment/modules_extra/%{_module_name}/*.png
