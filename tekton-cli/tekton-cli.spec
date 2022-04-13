%bcond_without check

# https://github.com/tektoncd/cli
%global goipath         github.com/tektoncd/cli
Version:                0.23.1
%global tag             %{version}

%gometa

Name:           tekton-cli
Release:        3%{?dist}
Summary:        Command line tool for interacting with Tekton
License:        Apache
URL:            %{gourl}
Source:         https://github.com/tektoncd/cli/archive/refs/tags/v%{version}.tar.gz

%description
Command line tool for interacting with Tekton

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/tkn %{goipath}/cmd/tkn/main.go

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/tkn %{buildroot}%{_bindir}/
	
%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%{_bindir}/tkn

%changelog
* Wed Apr 13 2022 Christian Rebischke <chris@shibumi.dev> 0.23.1-3
- fix: executable name (chris@shibumi.dev)

* Wed Apr 13 2022 Christian Rebischke <chris@shibumi.dev> 0.23.1-2
- fix: tekton source (chris@shibumi.dev)

* Wed Apr 13 2022 Christian Rebischke <chris@shibumi.dev> 0.23.1-1
- new package built with tito

