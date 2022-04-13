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
Source:         https://github.com/tektoncd/cli/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang(github.com/AlecAivazis/survey/v2)
BuildRequires:  golang(github.com/AlecAivazis/survey/v2/core)
BuildRequires:  golang(github.com/AlecAivazis/survey/v2/terminal)
BuildRequires:  golang(github.com/armon/go-metrics)
BuildRequires:  golang(github.com/armon/go-radix)
BuildRequires:  golang(github.com/blang/semver)
BuildRequires:  golang(github.com/cenkalti/backoff/v3)
BuildRequires:  golang(github.com/cpuguy83/go-md2man/md2man)
BuildRequires:  golang(github.com/docker/cli/cli/config)
BuildRequires:  golang(github.com/docker/cli/cli/config/types)
BuildRequires:  golang(github.com/docker/docker/pkg/homedir)
BuildRequires:  golang(github.com/fatih/color)
BuildRequires:  golang(github.com/ghodss/yaml)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires:  golang(github.com/golang/snappy)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/authn)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/name)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/registry)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1/cache)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1/empty)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1/mutate)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1/remote)
BuildRequires:  golang(github.com/google/go-containerregistry/pkg/v1/tarball)
BuildRequires:  golang(github.com/hako/durafmt)
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
BuildRequires:  golang(github.com/hinshun/vt10x)
BuildRequires:  golang(github.com/jonboulle/clockwork)
BuildRequires:  golang(github.com/ktr0731/go-fuzzyfinder)
BuildRequires:  golang(github.com/mitchellh/copystructure)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(github.com/mitchellh/go-testing-interface)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/Netflix/go-expect)
BuildRequires:  golang(github.com/oklog/run)
BuildRequires:  golang(github.com/pierrec/lz4)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/ryanuber/go-glob)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/tektoncd/chains/pkg/chains)
BuildRequires:  golang(github.com/tektoncd/chains/pkg/chains/storage)
BuildRequires:  golang(github.com/tektoncd/chains/pkg/config)
BuildRequires:  golang(github.com/tektoncd/hub/api/pkg/cli/app)
BuildRequires:  golang(github.com/tektoncd/hub/api/pkg/cli/cmd)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/apis/config)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/apis/pipeline)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/apis/pipeline/v1alpha1)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/apis/pipeline/v1beta1)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/client/clientset/versioned)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/client/clientset/versioned/fake)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/client/clientset/versioned/scheme)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/client/clientset/versioned/typed/pipeline/v1alpha1)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/client/informers/externalversions)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/client/resource/clientset/versioned)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/client/resource/clientset/versioned/typed/resource/v1alpha1)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/names)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/reconciler/testing)
BuildRequires:  golang(github.com/tektoncd/pipeline/pkg/remote/oci)
BuildRequires:  golang(github.com/tektoncd/pipeline/test)
BuildRequires:  golang(github.com/tektoncd/pipeline/test/v1alpha1)
BuildRequires:  golang(github.com/tektoncd/triggers/pkg/apis/triggers)
BuildRequires:  golang(github.com/tektoncd/triggers/pkg/apis/triggers/v1beta1)
BuildRequires:  golang(github.com/tektoncd/triggers/pkg/client/clientset/versioned)
BuildRequires:  golang(github.com/tektoncd/triggers/test)
BuildRequires:  golang(golang.org/x/crypto/blake2b)
BuildRequires:  golang(golang.org/x/crypto/cryptobyte)
BuildRequires:  golang(golang.org/x/crypto/cryptobyte/asn1)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/term)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(golang.org/x/xerrors)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/health)
BuildRequires:  golang(google.golang.org/grpc/health/grpc_health_v1)
BuildRequires:  golang(google.golang.org/grpc/reflection)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(gopkg.in/square/go-jose.v2/jwt)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(gotest.tools/assert)
BuildRequires:  golang(gotest.tools/assert/cmp)
BuildRequires:  golang(gotest.tools/v3/assert)
BuildRequires:  golang(gotest.tools/v3/golden)
BuildRequires:  golang(gotest.tools/v3/icmd)
BuildRequires:  golang(go.uber.org/atomic)
BuildRequires:  golang(go.uber.org/multierr)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(k8s.io/api/apps/v1)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/resource)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
BuildRequires:  golang(k8s.io/apimachinery/pkg/fields)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/selection)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/rand)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/yaml)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/client-go/discovery)
BuildRequires:  golang(k8s.io/client-go/dynamic)
BuildRequires:  golang(k8s.io/client-go/dynamic/fake)
BuildRequires:  golang(k8s.io/client-go/informers)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/core/v1)
BuildRequires:  golang(k8s.io/client-go/plugin/pkg/client/auth)
BuildRequires:  golang(k8s.io/client-go/plugin/pkg/client/auth/gcp)
BuildRequires:  golang(k8s.io/client-go/plugin/pkg/client/auth/oidc)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/restmapper)
BuildRequires:  golang(k8s.io/client-go/testing)
BuildRequires:  golang(k8s.io/client-go/tools/cache)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/cli-runtime/pkg/genericclioptions)
BuildRequires:  golang(knative.dev/pkg/apis)
BuildRequires:  golang(knative.dev/pkg/apis/duck/v1)
BuildRequires:  golang(knative.dev/pkg/apis/duck/v1beta1)
BuildRequires:  golang(knative.dev/pkg/system)
BuildRequires:  golang(knative.dev/pkg/test)
BuildRequires:  golang(knative.dev/pkg/test/logging)
BuildRequires:  golang(sigs.k8s.io/yaml)

%description
Command line tool for interacting with Tekton

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/tkn %{goipath}/cmd/tkn/

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


