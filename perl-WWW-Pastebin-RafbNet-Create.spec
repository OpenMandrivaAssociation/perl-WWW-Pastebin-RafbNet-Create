
%define realname   WWW-Pastebin-RafbNet-Create
%define version    0.001
%define release    6

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    create new pastes on http://rafb.net/
Source:     http://www.cpan.org/modules/by-module/WWW/%{realname}-%{version}.tar.gz
Url:        https://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Data::Accessor)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildRequires: perl(overload)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

%description

The module provides means to create new pastes on the http://rafb.net/
manpage paste site.

The the WWW::Rafb manpage module offers a similiar functionality. However,
it does not pass the test suite, and the author does not seem to care (last
update was close to a year ago). As well, the module seems to have a bit of
an "uncomfortable" interface, including not being able to paste text from a
scalar easily.



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*





%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.001-4mdv2011.0
+ Revision: 658427
- rebuild for updates rpm-setup

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.001-3mdv2010.0
+ Revision: 430660
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.001-2mdv2009.0
+ Revision: 268879
- rebuild early 2009.0 package (before pixel changes)

* Sat Apr 12 2008 Olivier Thauvin <nanardon@mandriva.org> 0.001-1mdv2009.0
+ Revision: 192633
- import perl-WWW-Pastebin-RafbNet-Create


