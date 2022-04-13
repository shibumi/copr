%bcond_without check

# https://github.com/tektoncd/cli
%global goipath         github.com/tektoncd/cli
Version:                0.23.1
%global tag             %{version}

%gometa

Name:           tekton-cli
Release:        0%{?dist}
Summary:        Command line tool for interacting with Tekton
License:        Apache
URL:            %{gourl}
Source:         https://github.com/cbednarski/hostess/archive/refs/tags/v%{version}.tar.gz

%description
Command line tool for interacting with Tekton

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/tekton-cli %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/tekton-cli %{buildroot}%{_bindir}/
	
%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%{_bindir}/tekton-cli

%changelog
