%bcond_without check

# https://github.com/sigstore/cosign
%global goipath         github.com/sigstore/cosign
Version:                1.7.1
%global tag             %{version}

%gometa

Name:           cosign
Release:        0%{?dist}
Summary:        Container Signing, Verification and Storage in an OCI registry
License:        Apache
URL:            %{gourl}
Source:         https://github.com/sigstore/cosign/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang(cloud.google.com/go/storage)
BuildRequires:  golang(cuelang.org/go/cue/cuecontext)
BuildRequires:  golang(cuelang.org/go/cue/load)
BuildRequires:  golang(cuelang.org/go/encoding/json)
BuildRequires:  golang(github.com/armon/go-metrics)
BuildRequires:  golang(github.com/armon/go-radix)
BuildRequires:  golang(github.com/awslabs/amazon-ecr-credential-helper/ecr-login)
BuildRequires:  golang(github.com/cenkalti/backoff/v3)
BuildRequires:  golang(github.com/chrismellard/docker-credential-acr-env/pkg/credhelper)
BuildRequires:  golang(github.com/cyberphone/json-canonicalization/go/src/webpki.org/jsoncanonicalizer)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires:  golang(github.com/golang/snappy)
BuildRequires:  golang(github.com/google/certificate-transparency-go)
BuildRequires:  golang(github.com/google/certificate-transparency-go/ctutil)
BuildRequires:  golang(github.com/google/certificate-transparency-go/x509)
BuildRequires:  golang(github.com/google/certificate-transparency-go/x509util)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(github.com/google/go-containerregistry/cmd/crane/cmd)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/authn)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/authn/github)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/authn/k8schain)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/logs)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/name)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1/empty)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1/google)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1/layout)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1/mutate)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1/random)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1/remote)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1/remote/transport)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1/types)
BuildRequires:  golang(github.com/google/go-github/v42/github)
BuildRequires:  golang(github.com/google/trillian/merkle/logverifier)
BuildRequires:  golang(github.com/google/trillian/merkle/rfc6962)
BuildRequires:  golang(github.com/go-openapi/runtime)
BuildRequires:  golang(github.com/go-openapi/strfmt)
BuildRequires:  golang(github.com/go-openapi/swag)
BuildRequires:  golang(github.com/hashicorp/errwrap)
BuildRequires:  golang(github.com/hashicorp/go-cleanhttp)
BuildRequires:  golang(github.com/hashicorp/go-hclog)
BuildRequires:  golang(github.com/hashicorp/go-immutable-radix)
BuildRequires:  golang(github.com/hashicorp/golang-lru)
BuildRequires:  golang(github.com/hashicorp/golang-lru/simplelru)
BuildRequires:  golang(github.com/hashicorp/go-multierror)
BuildRequires:  golang(github.com/hashicorp/go-plugin)
BuildRequires:  golang(github.com/hashicorp/go-plugin/internal/plugin)
BuildRequires:  golang(github.com/hashicorp/go-retryablehttp)
BuildRequires:  golang(github.com/hashicorp/go-rootcerts)
BuildRequires:  golang(github.com/hashicorp/go-secure-stdlib/mlock)
BuildRequires:  golang(github.com/hashicorp/go-secure-stdlib/parseutil)
BuildRequires:  golang(github.com/hashicorp/go-secure-stdlib/strutil)
BuildRequires:  golang(github.com/hashicorp/go-sockaddr)
BuildRequires:  golang(github.com/hashicorp/go-uuid)
BuildRequires:  golang(github.com/hashicorp/go-version)
BuildRequires:  golang(github.com/hashicorp/hcl)
BuildRequires:  golang(github.com/hashicorp/hcl/hcl/ast)
BuildRequires:  golang(github.com/hashicorp/hcl/hcl/parser)
BuildRequires:  golang(github.com/hashicorp/hcl/hcl/scanner)
BuildRequires:  golang(github.com/hashicorp/hcl/hcl/strconv)
BuildRequires:  golang(github.com/hashicorp/hcl/hcl/token)
BuildRequires:  golang(github.com/hashicorp/hcl/json/parser)
BuildRequires:  golang(github.com/hashicorp/hcl/json/scanner)
BuildRequires:  golang(github.com/hashicorp/hcl/json/token)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/certutil)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/compressutil)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/consts)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/cryptoutil)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/errutil)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/hclutil)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/jsonutil)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/license)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/locksutil)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/logging)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/pathmanager)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/pluginutil)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/strutil)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/helper/wrapping)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/logical)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/physical)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/physical/inmem)
BuildRequires:  golang(github.com/hashicorp/vault/sdk/version)
BuildRequires:  golang(github.com/hashicorp/yamux)
BuildRequires:  golang(github.com/in-toto/in-toto-golang/in_toto)
BuildRequires:  golang(github.com/in-toto/in-toto-golang/in_toto/slsa_provenance/v0.2)
BuildRequires:  golang(github.com/kelseyhightower/envconfig)
BuildRequires:  golang(github.com/letsencrypt/boulder/core)
BuildRequires:  golang(github.com/letsencrypt/boulder/core/proto)
BuildRequires:  golang(github.com/letsencrypt/boulder/errors)
BuildRequires:  golang(github.com/letsencrypt/boulder/features)
BuildRequires:  golang(github.com/letsencrypt/boulder/identifier)
BuildRequires:  golang(github.com/letsencrypt/boulder/probs)
BuildRequires:  golang(github.com/letsencrypt/boulder/revocation)
BuildRequires:  golang(github.com/letsencrypt/boulder/sa/proto)
BuildRequires:  golang(github.com/mitchellh/copystructure)
BuildRequires:  golang(github.com/mitchellh/go-testing-interface)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/oklog/run)
BuildRequires:  golang(github.com/open-policy-agent/opa/rego)
BuildRequires:  golang(github.com/pierrec/lz4)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/ryanuber/go-glob)
BuildRequires:  golang(github.com/secure-systems-lab/go-securesystemslib/cjson)
BuildRequires:  golang(github.com/secure-systems-lab/go-securesystemslib/dsse)
BuildRequires:  golang(github.com/sigstore/fulcio/pkg/api)
BuildRequires:  golang(github.com/sigstore/rekor/pkg/client)
BuildRequires:  golang(github.com/sigstore/rekor/pkg/generated/client)
BuildRequires:  golang(github.com/sigstore/rekor/pkg/generated/client/entries)
BuildRequires:  golang(github.com/sigstore/rekor/pkg/generated/client/index)
BuildRequires:  golang(github.com/sigstore/rekor/pkg/generated/models)
BuildRequires:  golang(github.com/sigstore/rekor/pkg/types)
BuildRequires:  golang(github.com/sigstore/rekor/pkg/types/hashedrekord/v0.0.1)
BuildRequires:  golang(github.com/sigstore/rekor/pkg/types/intoto/v0.0.1)
BuildRequires:  golang(github.com/sigstore/rekor/pkg/types/rekord/v0.0.1)
BuildRequires:  golang(github.com/sigstore/sigstore/pkg/cryptoutils)
BuildRequires:  golang(github.com/sigstore/sigstore/pkg/oauthflow)
BuildRequires:  golang(github.com/sigstore/sigstore/pkg/signature)
BuildRequires:  golang(github.com/sigstore/sigstore/pkg/signature/dsse)
BuildRequires:  golang(github.com/sigstore/sigstore/pkg/signature/kms)
BuildRequires:  golang(github.com/sigstore/sigstore/pkg/signature/kms/aws)
BuildRequires:  golang(github.com/sigstore/sigstore/pkg/signature/kms/azure)
BuildRequires:  golang(github.com/sigstore/sigstore/pkg/signature/kms/fake)
BuildRequires:  golang(github.com/sigstore/sigstore/pkg/signature/kms/gcp)
BuildRequires:  golang(github.com/sigstore/sigstore/pkg/signature/kms/hashivault)
BuildRequires:  golang(github.com/sigstore/sigstore/pkg/signature/options)
BuildRequires:  golang(github.com/sigstore/sigstore/pkg/signature/payload)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/cobra/doc)
BuildRequires:  golang(github.com/spf13/viper)
BuildRequires:  golang(github.com/spiffe/go-spiffe/v2/svid/jwtsvid)
BuildRequires:  golang(github.com/spiffe/go-spiffe/v2/workloadapi)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/theupdateframework/go-tuf)
BuildRequires:  golang(github.com/theupdateframework/go-tuf/client)
BuildRequires:  golang(github.com/theupdateframework/go-tuf/client/leveldbstore)
BuildRequires:  golang(github.com/theupdateframework/go-tuf/data)
BuildRequires:  golang(github.com/theupdateframework/go-tuf/encrypted)
BuildRequires:  golang(github.com/theupdateframework/go-tuf/util)
BuildRequires:  golang(github.com/theupdateframework/go-tuf/verify)
BuildRequires:  golang(github.com/titanous/rocacheck)
BuildRequires:  golang(github.com/withfig/autocomplete-tools/packages/cobra)
BuildRequires:  golang(github.com/xanzy/go-gitlab)
BuildRequires:  golang(golang.org/x/crypto/blake2b)
BuildRequires:  golang(golang.org/x/crypto/cryptobyte)
BuildRequires:  golang(golang.org/x/crypto/cryptobyte/asn1)
BuildRequires:  golang(golang.org/x/crypto/ocsp)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/term)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(google.golang.org/api/idtoken)
BuildRequires:  golang(google.golang.org/api/impersonate)
BuildRequires:  golang(google.golang.org/api/option)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/health)
BuildRequires:  golang(google.golang.org/grpc/health/grpc_health_v1)
BuildRequires:  golang(google.golang.org/grpc/reflection)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires:  golang(google.golang.org/protobuf/types/known/emptypb)
BuildRequires:  golang(gopkg.in/square/go-jose.v2)
BuildRequires:  golang(gopkg.in/square/go-jose.v2/jwt)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(go.uber.org/atomic)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(k8s.io/api/apps/v1)
BuildRequires:  golang(k8s.io/api/batch/v1)
BuildRequires:  golang(k8s.io/api/batch/v1beta1)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/meta)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/resource)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
BuildRequires:  golang(k8s.io/apimachinery/pkg/labels)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/version)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/yaml)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/client-go/discovery)
BuildRequires:  golang(k8s.io/client-go/discovery/fake)
BuildRequires:  golang(k8s.io/client-go/dynamic)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/kubernetes/fake)
BuildRequires:  golang(k8s.io/client-go/kubernetes/scheme)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/core/v1)
BuildRequires:  golang(k8s.io/client-go/listers/core/v1)
BuildRequires:  golang(k8s.io/client-go/plugin/pkg/client/auth)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/testing)
BuildRequires:  golang(k8s.io/client-go/tools/cache)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/client-go/tools/record)
BuildRequires:  golang(k8s.io/client-go/util/flowcontrol)
BuildRequires:  golang(k8s.io/utils/pointer)
BuildRequires:  golang(knative.dev/hack/schema/commands)
BuildRequires:  golang(knative.dev/hack/schema/registry)
BuildRequires:  golang(knative.dev/pkg/apis)
BuildRequires:  golang(knative.dev/pkg/apis/duck)
BuildRequires:  golang(knative.dev/pkg/apis/duck/v1)
BuildRequires:  golang(knative.dev/pkg/client/injection/kube/client)
BuildRequires:  golang(knative.dev/pkg/client/injection/kube/client/fake)
BuildRequires:  golang(knative.dev/pkg/client/injection/kube/informers/core/v1/configmap/fake)
BuildRequires:  golang(knative.dev/pkg/configmap)
BuildRequires:  golang(knative.dev/pkg/configmap/testing)
BuildRequires:  golang(knative.dev/pkg/controller)
BuildRequires:  golang(knative.dev/pkg/injection)
BuildRequires:  golang(knative.dev/pkg/injection/clients/dynamicclient)
BuildRequires:  golang(knative.dev/pkg/injection/clients/dynamicclient/fake)
BuildRequires:  golang(knative.dev/pkg/injection/clients/namespacedkube/informers/core/v1/configmap)
BuildRequires:  golang(knative.dev/pkg/injection/clients/namespacedkube/informers/core/v1/configmap/fake)
BuildRequires:  golang(knative.dev/pkg/injection/clients/namespacedkube/informers/core/v1/secret)
BuildRequires:  golang(knative.dev/pkg/injection/clients/namespacedkube/informers/core/v1/secret/fake)
BuildRequires:  golang(knative.dev/pkg/injection/clients/namespacedkube/informers/factory/fake)
BuildRequires:  golang(knative.dev/pkg/injection/sharedmain)
BuildRequires:  golang(knative.dev/pkg/kmeta)
BuildRequires:  golang(knative.dev/pkg/logging)
BuildRequires:  golang(knative.dev/pkg/logging/logkey)
BuildRequires:  golang(knative.dev/pkg/logging/testing)
BuildRequires:  golang(knative.dev/pkg/pool)
BuildRequires:  golang(knative.dev/pkg/reconciler)
BuildRequires:  golang(knative.dev/pkg/reconciler/testing)
BuildRequires:  golang(knative.dev/pkg/signals)
BuildRequires:  golang(knative.dev/pkg/system)
BuildRequires:  golang(knative.dev/pkg/system/testing)
BuildRequires:  golang(knative.dev/pkg/tracker)
BuildRequires:  golang(knative.dev/pkg/webhook)
BuildRequires:  golang(knative.dev/pkg/webhook/certificates)
BuildRequires:  golang(knative.dev/pkg/webhook/resourcesemantics)
BuildRequires:  golang(knative.dev/pkg/webhook/resourcesemantics/defaulting)
BuildRequires:  golang(knative.dev/pkg/webhook/resourcesemantics/validation)
BuildRequires:  golang(sigs.k8s.io/release-utils/version)
BuildRequires:  golang(sigs.k8s.io/yaml)


%description
Container Signing, Verification and Storage in an OCI registry.
Cosign aims to make signatures invisible infrastructure.

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/cosign %{goipath}/cmd/cosign

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
