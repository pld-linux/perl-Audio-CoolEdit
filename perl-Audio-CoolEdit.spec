#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	CoolEdit
Summary:	Audio::CoolEdit Perl module - reading/writing Syntrillium CoolEdit Pro .ses files
Summary(pl):	Modu³ Perla Audio::CoolEdit - odczyt/zapis plików .ses programu CoolEdit Pro
Name:		perl-Audio-CoolEdit
Version:	0.01
Release:	3
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	76747b7256b59eed9454c2ba6838ef84
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Audio-Tools
%{!?_without_tests:BuildRequires:	perl-Audio-Wav}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Audio::Wav)'

%description
Syntrillium's CoolEdit Pro (http://www.syntrillium.com/) is a MSWin32
based multitrack capable sound editor. This module reads/writes the
.ses (session) file format enabling you to place audio files in a
virtual track at a given offset. The write module is a lot more
developed than the read module as this has been developed to be used
with Audio::Mix.

%description -l pl
Program CoolEdit Pro firmy Syntrillium (http://www.syntrillium.com/)
jest wielo¶cie¿kowym edytorem d¼wiêku pod MS Windows. Ten modu³ Perla
potrafi odczytywaæ i zapisywaæ pliki sesji tego programu (.ses),
pozwalaj±c na umieszczanie wirtualnych ¶cie¿ek w podanym miejscu.
Modu³ zapisuj±cy jest bardziej rozwiniêty od czytaj±cego, poniewa¿ by³
tworzony z my¶l± o u¿ywaniu ³±cznie z Audio::Mix.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Audio/CoolEdit.pm
%{perl_vendorlib}/Audio/CoolEdit
%{_mandir}/man3/*
