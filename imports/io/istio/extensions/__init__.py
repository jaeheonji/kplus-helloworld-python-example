import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import cdk8s
import constructs


class WasmPlugin(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistioextensions.WasmPlugin",
):
    '''
    :schema: WasmPlugin
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["WasmPluginSpec"] = None,
    ) -> None:
        '''Defines a "WasmPlugin" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: Extend the functionality provided by the Istio proxy through WebAssembly filters. See more details at: https://istio.io/docs/reference/config/proxy_extensions/wasm-plugin.html
        '''
        props = WasmPluginProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["WasmPluginSpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "WasmPlugin".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: Extend the functionality provided by the Istio proxy through WebAssembly filters. See more details at: https://istio.io/docs/reference/config/proxy_extensions/wasm-plugin.html
        '''
        props = WasmPluginProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "WasmPlugin".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistioextensions.WasmPluginProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class WasmPluginProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["WasmPluginSpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: Extend the functionality provided by the Istio proxy through WebAssembly filters. See more details at: https://istio.io/docs/reference/config/proxy_extensions/wasm-plugin.html

        :schema: WasmPlugin
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = WasmPluginSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: WasmPlugin#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["WasmPluginSpec"]:
        '''Extend the functionality provided by the Istio proxy through WebAssembly filters.

        See more details at: https://istio.io/docs/reference/config/proxy_extensions/wasm-plugin.html

        :schema: WasmPlugin#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["WasmPluginSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WasmPluginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistioextensions.WasmPluginSpec",
    jsii_struct_bases=[],
    name_mapping={
        "image_pull_policy": "imagePullPolicy",
        "image_pull_secret": "imagePullSecret",
        "phase": "phase",
        "plugin_config": "pluginConfig",
        "plugin_name": "pluginName",
        "priority": "priority",
        "selector": "selector",
        "sha256": "sha256",
        "url": "url",
        "verification_key": "verificationKey",
        "vm_config": "vmConfig",
    },
)
class WasmPluginSpec:
    def __init__(
        self,
        *,
        image_pull_policy: typing.Optional["WasmPluginSpecImagePullPolicy"] = None,
        image_pull_secret: typing.Optional[builtins.str] = None,
        phase: typing.Optional["WasmPluginSpecPhase"] = None,
        plugin_config: typing.Any = None,
        plugin_name: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        selector: typing.Optional["WasmPluginSpecSelector"] = None,
        sha256: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        verification_key: typing.Optional[builtins.str] = None,
        vm_config: typing.Optional["WasmPluginSpecVmConfig"] = None,
    ) -> None:
        '''Extend the functionality provided by the Istio proxy through WebAssembly filters.

        See more details at: https://istio.io/docs/reference/config/proxy_extensions/wasm-plugin.html

        :param image_pull_policy: 
        :param image_pull_secret: Credentials to use for OCI image pulling.
        :param phase: Determines where in the filter chain this ``WasmPlugin`` is to be injected.
        :param plugin_config: The configuration that will be passed on to the plugin.
        :param plugin_name: 
        :param priority: Determines ordering of ``WasmPlugins`` in the same ``phase``.
        :param selector: 
        :param sha256: SHA256 checksum that will be used to verify Wasm module or OCI container.
        :param url: URL of a Wasm module or OCI container.
        :param verification_key: 
        :param vm_config: Configuration for a Wasm VM.

        :schema: WasmPluginSpec
        '''
        if isinstance(selector, dict):
            selector = WasmPluginSpecSelector(**selector)
        if isinstance(vm_config, dict):
            vm_config = WasmPluginSpecVmConfig(**vm_config)
        self._values: typing.Dict[str, typing.Any] = {}
        if image_pull_policy is not None:
            self._values["image_pull_policy"] = image_pull_policy
        if image_pull_secret is not None:
            self._values["image_pull_secret"] = image_pull_secret
        if phase is not None:
            self._values["phase"] = phase
        if plugin_config is not None:
            self._values["plugin_config"] = plugin_config
        if plugin_name is not None:
            self._values["plugin_name"] = plugin_name
        if priority is not None:
            self._values["priority"] = priority
        if selector is not None:
            self._values["selector"] = selector
        if sha256 is not None:
            self._values["sha256"] = sha256
        if url is not None:
            self._values["url"] = url
        if verification_key is not None:
            self._values["verification_key"] = verification_key
        if vm_config is not None:
            self._values["vm_config"] = vm_config

    @builtins.property
    def image_pull_policy(self) -> typing.Optional["WasmPluginSpecImagePullPolicy"]:
        '''
        :schema: WasmPluginSpec#imagePullPolicy
        '''
        result = self._values.get("image_pull_policy")
        return typing.cast(typing.Optional["WasmPluginSpecImagePullPolicy"], result)

    @builtins.property
    def image_pull_secret(self) -> typing.Optional[builtins.str]:
        '''Credentials to use for OCI image pulling.

        :schema: WasmPluginSpec#imagePullSecret
        '''
        result = self._values.get("image_pull_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def phase(self) -> typing.Optional["WasmPluginSpecPhase"]:
        '''Determines where in the filter chain this ``WasmPlugin`` is to be injected.

        :schema: WasmPluginSpec#phase
        '''
        result = self._values.get("phase")
        return typing.cast(typing.Optional["WasmPluginSpecPhase"], result)

    @builtins.property
    def plugin_config(self) -> typing.Any:
        '''The configuration that will be passed on to the plugin.

        :schema: WasmPluginSpec#pluginConfig
        '''
        result = self._values.get("plugin_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def plugin_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: WasmPluginSpec#pluginName
        '''
        result = self._values.get("plugin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Determines ordering of ``WasmPlugins`` in the same ``phase``.

        :schema: WasmPluginSpec#priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def selector(self) -> typing.Optional["WasmPluginSpecSelector"]:
        '''
        :schema: WasmPluginSpec#selector
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional["WasmPluginSpecSelector"], result)

    @builtins.property
    def sha256(self) -> typing.Optional[builtins.str]:
        '''SHA256 checksum that will be used to verify Wasm module or OCI container.

        :schema: WasmPluginSpec#sha256
        '''
        result = self._values.get("sha256")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''URL of a Wasm module or OCI container.

        :schema: WasmPluginSpec#url
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verification_key(self) -> typing.Optional[builtins.str]:
        '''
        :schema: WasmPluginSpec#verificationKey
        '''
        result = self._values.get("verification_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vm_config(self) -> typing.Optional["WasmPluginSpecVmConfig"]:
        '''Configuration for a Wasm VM.

        :schema: WasmPluginSpec#vmConfig
        '''
        result = self._values.get("vm_config")
        return typing.cast(typing.Optional["WasmPluginSpecVmConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WasmPluginSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistioextensions.WasmPluginSpecImagePullPolicy")
class WasmPluginSpecImagePullPolicy(enum.Enum):
    '''
    :schema: WasmPluginSpecImagePullPolicy
    '''

    UNSPECIFIED_POLICY = "UNSPECIFIED_POLICY"
    '''UNSPECIFIED_POLICY.'''
    IF_NOT_PRESENT = "IF_NOT_PRESENT"
    '''IfNotPresent.'''
    ALWAYS = "ALWAYS"
    '''Always.'''


@jsii.enum(jsii_type="ioistioextensions.WasmPluginSpecPhase")
class WasmPluginSpecPhase(enum.Enum):
    '''Determines where in the filter chain this ``WasmPlugin`` is to be injected.

    :schema: WasmPluginSpecPhase
    '''

    UNSPECIFIED_PHASE = "UNSPECIFIED_PHASE"
    '''UNSPECIFIED_PHASE.'''
    AUTHN = "AUTHN"
    '''AUTHN.'''
    AUTHZ = "AUTHZ"
    '''AUTHZ.'''
    STATS = "STATS"
    '''STATS.'''


@jsii.data_type(
    jsii_type="ioistioextensions.WasmPluginSpecSelector",
    jsii_struct_bases=[],
    name_mapping={"match_labels": "matchLabels"},
)
class WasmPluginSpecSelector:
    def __init__(
        self,
        *,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_labels: 

        :schema: WasmPluginSpecSelector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: WasmPluginSpecSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WasmPluginSpecSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistioextensions.WasmPluginSpecVmConfig",
    jsii_struct_bases=[],
    name_mapping={"env": "env"},
)
class WasmPluginSpecVmConfig:
    def __init__(
        self,
        *,
        env: typing.Optional[typing.Sequence["WasmPluginSpecVmConfigEnv"]] = None,
    ) -> None:
        '''Configuration for a Wasm VM.

        :param env: Specifies environment variables to be injected to this VM.

        :schema: WasmPluginSpecVmConfig
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if env is not None:
            self._values["env"] = env

    @builtins.property
    def env(self) -> typing.Optional[typing.List["WasmPluginSpecVmConfigEnv"]]:
        '''Specifies environment variables to be injected to this VM.

        :schema: WasmPluginSpecVmConfig#env
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.List["WasmPluginSpecVmConfigEnv"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WasmPluginSpecVmConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistioextensions.WasmPluginSpecVmConfigEnv",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value", "value_from": "valueFrom"},
)
class WasmPluginSpecVmConfigEnv:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
        value_from: typing.Optional["WasmPluginSpecVmConfigEnvValueFrom"] = None,
    ) -> None:
        '''
        :param name: 
        :param value: Value for the environment variable.
        :param value_from: 

        :schema: WasmPluginSpecVmConfigEnv
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value
        if value_from is not None:
            self._values["value_from"] = value_from

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: WasmPluginSpecVmConfigEnv#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value for the environment variable.

        :schema: WasmPluginSpecVmConfigEnv#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value_from(self) -> typing.Optional["WasmPluginSpecVmConfigEnvValueFrom"]:
        '''
        :schema: WasmPluginSpecVmConfigEnv#valueFrom
        '''
        result = self._values.get("value_from")
        return typing.cast(typing.Optional["WasmPluginSpecVmConfigEnvValueFrom"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WasmPluginSpecVmConfigEnv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistioextensions.WasmPluginSpecVmConfigEnvValueFrom")
class WasmPluginSpecVmConfigEnvValueFrom(enum.Enum):
    '''
    :schema: WasmPluginSpecVmConfigEnvValueFrom
    '''

    INLINE = "INLINE"
    '''INLINE.'''
    HOST = "HOST"
    '''HOST.'''


__all__ = [
    "WasmPlugin",
    "WasmPluginProps",
    "WasmPluginSpec",
    "WasmPluginSpecImagePullPolicy",
    "WasmPluginSpecPhase",
    "WasmPluginSpecSelector",
    "WasmPluginSpecVmConfig",
    "WasmPluginSpecVmConfigEnv",
    "WasmPluginSpecVmConfigEnvValueFrom",
]

publication.publish()
