%bcond_without check

# https://github.com/cbednarski/hostess
%global goipath         github.com/cbednarski/hostess
Version:                0.5.2
%global tag             %{version}

%gometa

Name:           hostess
Release:        1%{?dist}
Summary:        Idempotent command-line utility for managing your /etc/hosts file.
License:        MIT
URL:            %{gourl}
Source:         https://github.com/cbednarski/hostess/archive/refs/tags/v%{version}.tar.gz

%description
Idempotent command-line utility for managing your /etc/hosts file.

%gopkg

%prep
%goprep

%build
%gobuild -o %gobuilddir/bin/hostess %goipath

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
	
%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%{_bindir}/hostess

%changelog
* Sun Apr 10 2022 Christian Rebischke <chris@shibumi.dev> 0.5.2-1
- new package built with tito





