Summary:	GeoLite IPASNum - IP to AS number translation database for GeoIP
Summary(pl.UTF-8):	GeoLite IPASNum - baza danych tłumaczeń adresów IP na numery AS dla GeoIP
Name:		GeoIP-db-IPASNum
# Updated every month:
Version:	2018.03.24
Release:	2
License:	CC 3.0 BY-SA
Group:		Applications/Databases
Source0:	http://download.maxmind.com/download/geoip/database/asnum/GeoIPASNum.dat.gz?/GeoIPASNum-%{version}.dat.gz
# Source0-md5:	25a61aba0974ff4e74e315f7dd3fa1b0
URL:		http://dev.maxmind.com/geoip/legacy/geolite/
Requires:	GeoIP-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains IPv4 to AS number translation database for
GeoIP.

License disclaimer: this product includes GeoLite data created by
MaxMind, available from <http://www.maxmind.com/>.

%description -l pl.UTF-8
Ten pakiet zawiera bazę danych tłumaczeń adresów IPv4 na numery AS dla
GeoIP.

Informacja licencyjna: ten produkt zawiera dane GeoLite stworzone
przez MaxMind, dostępne z <http://www.maxmind.com/>.

%prep
%setup -qcT
cp -p %{SOURCE0} GeoIPASNum.dat.gz
gunzip GeoIPASNum.dat.gz

ver=$(TZ=GMT stat -c '%y' GeoIPASNum.dat | awk '{print $1}' | tr - .)
if [ "$ver" != %{version} ]; then
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/GeoIP
cp -p GeoIPASNum.dat $RPM_BUILD_ROOT%{_datadir}/GeoIP

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/GeoIP/*.dat
