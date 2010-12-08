Summary:	GeoLite IPASNum - IP to AS number translation database for GeoIP
Summary(pl.UTF-8):	GeoLite IPASNum - baza danych tłumaczeń adresów IP na numery AS dla GeoIP
Name:		GeoIP-db-IPASNum
# Updated every month:
Version:	2010.12.05
Release:	1
License:	OPEN DATA LICENSE (see LICENSE.txt)
Group:		Applications/Databases
Source0:	http://www.maxmind.com/download/geoip/database/asnum/GeoIPASNum.dat.gz
# Source0-md5:	2cc667b6dd97c0d8166f1997ba3aa868
Source1:	http://www.maxmind.com/download/geoip/database/LICENSE.txt
# Source1-md5:	a1381bd1aa0a0c91dc31b3f1e847cf4a
URL:		http://www.maxmind.com/app/asnum
Requires:	GeoIP-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains IPv4 to AS number translation database for
GeoIP.

License disclaimer: this product includes GeoLite data created by
MaxMind, available from <http://www.maxmind.com/>.

%description -l pl.UTF-8
Ten pakiet zawiera bazę danych tłumaczeń adresów IPv4 na numery AS
dla GeoIP.

Informacja licencyjna: ten produkt zawiera dane GeoLite stworzone
przez MaxWind, dostępne z <http://www.maxwind.com/>.

%prep
%setup -qcT
cp -a %{SOURCE0} .
cp -a %{SOURCE1} .

gunzip GeoIPASNum.dat.gz

ver=$(stat -c '%y' GeoIPASNum.dat | awk '{print $1}' | tr - .)
if [ "$ver" != %{version} ]; then
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/GeoIP
cp -a GeoIPASNum.dat $RPM_BUILD_ROOT%{_datadir}/GeoIP

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_datadir}/GeoIP/*.dat
