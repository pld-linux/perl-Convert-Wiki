#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	Wiki
Summary:	Convert::Wiki - Convert HTML/POD/txt from/to Wiki code
#Summary(pl):	
Name:		perl-Convert-Wiki
Version:	0.05
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b8f25323a46cbaacf85e32f3923bc2e8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::Differences) >= 0.47
BuildRequires:	perl(Text::Format) >= 0.52
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::Wiki converts from various formats to various Wiki formats.

Input can come as HTML, POD or plain TXT (like it is written in many READMEs).
The data will be converted to an internal, node based format and can then be
converted to Wikicode as used by many wikis like the Wikipedia.



# %description -l pl
# TODO

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%{perl_vendorlib}/Convert/*.pm
%{perl_vendorlib}/Convert/Wiki
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
