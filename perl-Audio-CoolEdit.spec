#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"

%define		pdir	Audio
%define		pnam	CoolEdit
Summary:	Audio::CoolEdit Perl module - reading/writing Syntrillium CoolEdit Pro .ses files
Summary(pl.UTF-8):	Moduł Perla Audio::CoolEdit - odczyt/zapis plików .ses programu CoolEdit Pro
Name:		perl-Audio-CoolEdit
Version:	0.01
Release:	6
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	76747b7256b59eed9454c2ba6838ef84
URL:		http://search.cpan.org/dist/Audio-CoolEdit/
BuildRequires:	perl-Audio-Tools
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl(Audio::Tools::ByteOrder)
BuildRequires:	perl-Audio-Tools
BuildRequires:	perl-Audio-Wav
%endif
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

%description -l pl.UTF-8
Program CoolEdit Pro firmy Syntrillium (http://www.syntrillium.com/)
jest wielościeżkowym edytorem dźwięku pod MS Windows. Ten moduł Perla
potrafi odczytywać i zapisywać pliki sesji tego programu (.ses),
pozwalając na umieszczanie wirtualnych ścieżek w podanym miejscu.
Moduł zapisujący jest bardziej rozwinięty od czytającego, ponieważ był
tworzony z myślą o używaniu łącznie z Audio::Mix.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
