Summary:	AsmEdit - editor written in assembler
Summary(pl):	AsmEdit - edytor napisany w assemblerze
Name:		AsmEdit
Version:	0.9.2
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/asmedit/%{name}-%{version}.tar.gz
# Source0-md5:	6daef4f78eff08e4ba10abfa8a67ba86
URL:		http://asmedit.massmind.org/
BuildRequires:	nasm
BuildRequires:  sed >= 4.1.1
BuildArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AsmEdit is a full featured editor written in assembler. It does not
require any libraries. It works in console.

%description -l pl
AsmEdit jest obszernym edytorem napisanym w assemblerze. Nie wymaga
¿adnych bibliotek. Pracuje w konsoli.

%prep
%setup -q -n release
%{__sed} -i 's,~/bin,%{_bindir},' Makefile
%{__sed} -i 's,/bin/bash,%{___build_shell},' a.f* 

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
mv dir a.dir
install a a.dir $RPM_BUILD_ROOT%{_bindir}
install a.hlp $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc change.log bugs.log readme.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
