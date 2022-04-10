%bcond_without check

# https://github.com/sigstore/cosign
%global goipath         github.com/sigstore/cosign
Version:                1.7.2
%global tag             %{version}

%gometa

Name:           cosign
Release:        0%{?dist}
Summary:        Container Signing, Verification and Storage in an OCI registry
License:        Apache
URL:            %{gourl}
Source:         %{gosource}

%description
Container Signing, Verification and Storage in an OCI registry.
Cosign aims to make signatures invisible infrastructure.

%gopkg

%prep
%goprep

%build
%gobuild -o %gobuilddir/bin/cosign %goipath/cmd/cosign

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
%{_bindir}/cosign

%changelog


