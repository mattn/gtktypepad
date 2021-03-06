Name:           gtktypepad
Version:        0.0.1
Release:        1%{?dist}
Summary:        A TypePad client for Linux which using GTK
Group:          Applications/Network
License:        GPL
URL:            http://mattn.kaoriya.net
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gtk2-devel >= 2.4 libxml >= 2.6 curl-devel desktop-file-utils
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
A lightweight TypePad client for Linux written in GTK.

%prep
%setup -q -n %{name}-%{version}

%build
aclocal
automake -a
autoheader 
autoconf
chmod +x configure
%configure
make %{?_smp_mflags}
cat>>%{name}.desktop<<EOF
[Desktop Entry]
Encoding=UTF-8
Exec=%{name}
Icon=%{_datadir}/%{name}/logo.png
Type=Application
Terminal=false
Name=GtkTypePad
Categories=Application;Network;
EOF

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
cp data/logo.png $RPM_BUILD_ROOT%{_datadir}/gtktypepad/logo.png
desktop-file-install --vendor=fedora \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category X-Fedora \
  --add-category GTK \
  --delete-original \
  %{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
update-desktop-database

%postun
update-desktop-database

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/gtktypepad/logo.png
%{_datadir}/gtktypepad/typepad.png
%{_datadir}/gtktypepad/loading.gif
%{_datadir}/gtktypepad/reload.png
%{_datadir}/gtktypepad/home.png
%{_datadir}/gtktypepad/post.png
%{_datadir}/gtktypepad/config.png

%changelog
- Initial RPM release.
