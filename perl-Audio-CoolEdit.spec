#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	CoolEdit
Summary:	Audio::CoolEdit Perl module - reading/writing Syntrillium CoolEdit Pro .ses files
Summary(pl):	Modu� Perla Audio::CoolEdit - odczyt/zapis plik�w .ses programu CoolEdit Pro
Name:		perl-Audio-CoolEdit
Version:	0.01
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Audio-Tools
%{!?_without_tests:BuildRequires:	perl-Audio-Wav}
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
jest wielo�cie�kowym edytorem d�wi�ku pod MS Windows. Ten modu� Perla
potrafi odczytywa� i zapisywa� pliki sesji tego programu (.ses),
pozwalaj�c na umieszczanie wirtualnych �cie�ek w podanym miejscu.
Modu� zapisuj�cy jest bardziej rozwini�ty od czytaj�cego, poniewa� by�
tworzony z my�l� o u�ywaniu ��cznie z Audio::Mix.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
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
%{perl_sitelib}/Audio/CoolEdit.pm
%{perl_sitelib}/Audio/CoolEdit
%{_mandir}/man3/*
