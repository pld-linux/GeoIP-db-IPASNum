Summary:	GeoLite IPASNum - IP to AS number translation database for GeoIP
Summary(pl.UTF-8):	GeoLite IPASNum - baza danych tłumaczeń adresów IP na numery AS dla GeoIP
Name:		GeoIP-db-IPASNum
# Updated every month:
Version:	2007.05.15
Release:	1
License:	OPEN DATA LICENSE (see LICENSE.txt)
Group:		Applications/Databases
Source0:	http://www.maxmind.com/download/geoip/database/asnum/GeoIPASNum.dat.gz
# Source0-md5:	27d7e96a9bf3f04acd71e674119f3601
Source1:	http://www.maxmind.com/download/geoip/database/LICENSE.txt
# Source1-md5:	8c0bc6e8ebe6ec3bc1580021edb4bba1
URL:		http://www.maxmind.com/app/asnum
Requires:	GeoIP-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GeoIP is a C library that enables the user to find the country that
any IP address or hostname originates from. It uses a file based
database that is accurate as of March 2003. This database simply
contains IP blocks as keys, and countries as values. This database
should be more complete and accurate than using reverse DNS lookups.

This package contains IPv4 to AS number translation database for
GeoIP.

License disclaimer: this product includes GeoLite data created by
MaxMind, available from <http://www.maxmind.com/>.

%description -l pl.UTF-8
GeoIP jest biblioteką napisaną w C umożliwiającą użytkownikowi
odnalezienie państwa, z którego pochodzi dany adres IP lub domena.
Używa do tego zapisanej w pliku bazy danych (z marca 2003). W bazie
tej adresy IP są kluczami, a państwa wartościami. Powinna ona być
dokładniejsza niż sprawdzanie odwrotnego DNS. 

Ten pakiet zawiera bazę danych tłumaczeń adresów IPv4 na numery AS
dla GeoIP.

Informacja licencyjna: ten produkt zawiera dane GeoLite stworzone
przez MaxWind, dostępne z <http://www.maxwind.com/>.

%prep
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

gunzip GeoIPASNum.dat.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/GeoIP

install GeoIPASNum.dat $RPM_BUILD_ROOT%{_datadir}/GeoIP

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_datadir}/GeoIP/*.dat
