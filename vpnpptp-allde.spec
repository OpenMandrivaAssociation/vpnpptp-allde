%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Tools for setup and control VPN via PPTP/L2TP/OpenL2TP
Name:		vpnpptp-allde
Version:	0.3.9
Release:	3
License:	GPL2+
Group:		System/Configuration/Networking
Url:		https://sourceforge.net/projects/vpnpptp/files/

Source0:	https://downloads.sourceforge.net/project/vpnpptp/vpnpptp-src-%{version}.tar.gz
Source1:	vpnpptp.pm
Source2:	vpnmandriva.pm
Patch1:		oxygen-gtk.patch

BuildRequires:	fpc-src >= 2.6.0
BuildRequires:	fpc >= 2.6.0
BuildRequires:	lazarus >= 0.9.30
# Do not require xroot because main DEs have their own su GUIs
# that can be used by vpnpptp and ponoff
# Requires:	xroot
Requires:	pptp-linux
Requires:	xl2tpd >= 1.2.7
Requires:	openl2tp

%description
Tools for easy and quick setup and control VPN via PPTP/L2TP/OpenL2TP.

%prep
%setup -q -n vpnpptp-src-%{version}
%autopatch -p1

%build
./compile.sh

%install
mkdir -p %{buildroot}%{_datadir}/vpnpptp
mkdir -p %{buildroot}%{_datadir}/vpnpptp/scripts
mkdir -p %{buildroot}%{_datadir}/vpnpptp/wiki
mkdir -p %{buildroot}%{_datadir}/vpnpptp/lang
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}/lib/libDrakX/network/connection

cp -f ./vpnpptp/vpnpptp %{buildroot}%{_bindir}
cp -f ./ponoff/ponoff %{buildroot}%{_bindir}
cp -f ./vpnmandriva/vpnmandriva %{buildroot}%{_bindir}
cp -f ./ponoff.png %{buildroot}%{_datadir}/pixmaps/
cp -f ./vpnpptp.png %{buildroot}%{_datadir}/pixmaps/
chmod 0644 %{buildroot}%{_datadir}/pixmaps/ponoff.png
chmod 0644 %{buildroot}%{_datadir}/pixmaps/vpnpptp.png
cp -f ./*.ico %{buildroot}%{_datadir}/vpnpptp
cp -f ./vpnlinux %{buildroot}%{_bindir}
cp -rf ./scripts %{buildroot}%{_datadir}/vpnpptp/
cp -rf ./wiki %{buildroot}%{_datadir}/vpnpptp/
cp -rf ./lang %{buildroot}%{_datadir}/vpnpptp/

install -dm 755 %{buildroot}%{_datadir}/applications

cat > ponoff.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
GenericName=VPN PPTP/L2TP/OpenL2TP Control
GenericName[ru]=Управление соединением VPN PPTP/L2TP/OpenL2TP
GenericName[uk]=Керування з'єднанням VPN PPTP/L2TP/OpenL2TP
Name=ponoff
Name[ru]=ponoff
Name[uk]=ponoff
Exec=/usr/bin/ponoff
Comment=Control VPN via PPTP/L2TP/OpenL2TP
Comment[ru]=Управление соединением VPN через PPTP/L2TP/OpenL2TP
Comment[uk]=Керування з'єднанням VPN через PPTP/L2TP/OpenL2TP
Icon=/usr/share/pixmaps/ponoff.png
Type=Application
Categories=GTK;System;Monitor;X-MandrivaLinux-CrossDesktop;
X-KDE-autostart-after=kdesktop
StartupNotify=false
EOF

install -m 0644 ponoff.desktop \
%{buildroot}%{_datadir}/applications/ponoff.desktop

cat > vpnpptp.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
GenericName=VPN PPTP/L2TP/OpenL2TP Setup
GenericName[ru]=Настройка соединения VPN PPTP/L2TP/OpenL2TP
GenericName[uk]=Налаштування з’єднання VPN PPTP/L2TP/OpenL2TP
Name=vpnpptp
Name[ru]=vpnpptp
Name[uk]=vpnpptp
Exec=/usr/bin/vpnpptp
Comment=Setup VPN via PPTP/L2TP/OpenL2TP
Comment[ru]=Настройка соединения VPN PPTP/L2TP/OpenL2TP
Comment[uk]=Налаштування з’єднання VPN PPTP/L2TP/OpenL2TP
Icon=/usr/share/pixmaps/vpnpptp.png
Type=Application
Categories=GTK;System;Monitor;X-MandrivaLinux-CrossDesktop;
StartupNotify=false
EOF

install -m 0644 vpnpptp.desktop \
%{buildroot}%{_datadir}/applications/vpnpptp.desktop

install -pm0644 -D %{SOURCE1} %{buildroot}/usr/lib/libDrakX/network/vpn/vpnpptp.pm
install -pm0644 -D %{SOURCE2} %{buildroot}/usr/lib/libDrakX/network/vpn/vpnmandriva.pm

%files
%{_bindir}/vpnpptp
%{_bindir}/ponoff
%{_bindir}/vpnlinux
%{_bindir}/vpnmandriva
%{_datadir}/vpnpptp/lang
%{_datadir}/pixmaps/ponoff.png
%{_datadir}/pixmaps/vpnpptp.png
%{_datadir}/vpnpptp/*.ico
%{_datadir}/vpnpptp/scripts
%{_datadir}/vpnpptp/wiki
%{_datadir}/applications/ponoff.desktop
%{_datadir}/applications/vpnpptp.desktop
%{_prefix}/lib/libDrakX/network/vpn/vpnpptp.pm
%{_prefix}/lib/libDrakX/network/vpn/vpnmandriva.pm

