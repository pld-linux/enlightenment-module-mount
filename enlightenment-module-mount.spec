%define		_module_name	mount

Summary:	Enlightenment DR17 module: mount
Summary(pl):	Modu³ Enlightenmenta DR17: mount
Name:		enlightenment-module-%{_module_name}
Version:	0.0.6
Release:	1
License:	BSD
Group:		X11/Window Managers/Tools
Source0:	http://www.get-e.org/Resources/Modules/_files/%{_module_name}-%{version}.tar.gz
# Source0-md5:	c9860d2dd415746487f181250e44539e
URL:		http://www.get-e.org/Resources/Modules/
BuildRequires:	edje
BuildRequires:	enlightenmentDR17-devel
BuildRequires:	sed >= 4.0
Requires:	enlightenmentDR17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mount module for Enlightenment DR17 makes easy mounting file systems
with "user" option in /etc/fstab.

%description -l pl
Modu³ mount dla Enlightenmenta DR17 u³atwia montowanie systemów plików
z opcj± "user" w /etc/fstab.

%prep
%setup -q -n %{_module_name}
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*/module.so
# violates FHS
%{_libdir}/enlightenment/modules_extra/%{_module_name}/%{_module_name}.*
%{_libdir}/enlightenment/modules_extra/%{_module_name}/module_icon.png
