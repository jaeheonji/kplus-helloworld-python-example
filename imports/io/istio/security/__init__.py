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


class AuthorizationPolicy(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistiosecurity.AuthorizationPolicy",
):
    '''
    :schema: AuthorizationPolicy
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["AuthorizationPolicySpec"] = None,
    ) -> None:
        '''Defines a "AuthorizationPolicy" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: Configuration for access control on workloads. See more details at: https://istio.io/docs/reference/config/security/authorization-policy.html
        '''
        props = AuthorizationPolicyProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["AuthorizationPolicySpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "AuthorizationPolicy".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: Configuration for access control on workloads. See more details at: https://istio.io/docs/reference/config/security/authorization-policy.html
        '''
        props = AuthorizationPolicyProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "AuthorizationPolicy".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistiosecurity.AuthorizationPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class AuthorizationPolicyProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["AuthorizationPolicySpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: Configuration for access control on workloads. See more details at: https://istio.io/docs/reference/config/security/authorization-policy.html

        :schema: AuthorizationPolicy
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = AuthorizationPolicySpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: AuthorizationPolicy#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["AuthorizationPolicySpec"]:
        '''Configuration for access control on workloads.

        See more details at: https://istio.io/docs/reference/config/security/authorization-policy.html

        :schema: AuthorizationPolicy#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["AuthorizationPolicySpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.AuthorizationPolicySpec",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "provider": "provider",
        "rules": "rules",
        "selector": "selector",
    },
)
class AuthorizationPolicySpec:
    def __init__(
        self,
        *,
        action: typing.Optional["AuthorizationPolicySpecAction"] = None,
        provider: typing.Optional["AuthorizationPolicySpecProvider"] = None,
        rules: typing.Optional[typing.Sequence["AuthorizationPolicySpecRules"]] = None,
        selector: typing.Optional["AuthorizationPolicySpecSelector"] = None,
    ) -> None:
        '''Configuration for access control on workloads.

        See more details at: https://istio.io/docs/reference/config/security/authorization-policy.html

        :param action: Optional.
        :param provider: Specifies detailed configuration of the CUSTOM action.
        :param rules: Optional.
        :param selector: Optional.

        :schema: AuthorizationPolicySpec
        '''
        if isinstance(provider, dict):
            provider = AuthorizationPolicySpecProvider(**provider)
        if isinstance(selector, dict):
            selector = AuthorizationPolicySpecSelector(**selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if provider is not None:
            self._values["provider"] = provider
        if rules is not None:
            self._values["rules"] = rules
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def action(self) -> typing.Optional["AuthorizationPolicySpecAction"]:
        '''Optional.

        :schema: AuthorizationPolicySpec#action
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional["AuthorizationPolicySpecAction"], result)

    @builtins.property
    def provider(self) -> typing.Optional["AuthorizationPolicySpecProvider"]:
        '''Specifies detailed configuration of the CUSTOM action.

        :schema: AuthorizationPolicySpec#provider
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional["AuthorizationPolicySpecProvider"], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List["AuthorizationPolicySpecRules"]]:
        '''Optional.

        :schema: AuthorizationPolicySpec#rules
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List["AuthorizationPolicySpecRules"]], result)

    @builtins.property
    def selector(self) -> typing.Optional["AuthorizationPolicySpecSelector"]:
        '''Optional.

        :schema: AuthorizationPolicySpec#selector
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional["AuthorizationPolicySpecSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistiosecurity.AuthorizationPolicySpecAction")
class AuthorizationPolicySpecAction(enum.Enum):
    '''Optional.

    :schema: AuthorizationPolicySpecAction
    '''

    ALLOW = "ALLOW"
    '''ALLOW.'''
    DENY = "DENY"
    '''DENY.'''
    AUDIT = "AUDIT"
    '''AUDIT.'''
    CUSTOM = "CUSTOM"
    '''CUSTOM.'''


@jsii.data_type(
    jsii_type="ioistiosecurity.AuthorizationPolicySpecProvider",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class AuthorizationPolicySpecProvider:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''Specifies detailed configuration of the CUSTOM action.

        :param name: Specifies the name of the extension provider.

        :schema: AuthorizationPolicySpecProvider
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the extension provider.

        :schema: AuthorizationPolicySpecProvider#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.AuthorizationPolicySpecRules",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to", "when": "when"},
)
class AuthorizationPolicySpecRules:
    def __init__(
        self,
        *,
        from_: typing.Optional[typing.Sequence["AuthorizationPolicySpecRulesFrom"]] = None,
        to: typing.Optional[typing.Sequence["AuthorizationPolicySpecRulesTo"]] = None,
        when: typing.Optional[typing.Sequence["AuthorizationPolicySpecRulesWhen"]] = None,
    ) -> None:
        '''
        :param from_: Optional.
        :param to: Optional.
        :param when: Optional.

        :schema: AuthorizationPolicySpecRules
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to
        if when is not None:
            self._values["when"] = when

    @builtins.property
    def from_(self) -> typing.Optional[typing.List["AuthorizationPolicySpecRulesFrom"]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRules#from
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[typing.List["AuthorizationPolicySpecRulesFrom"]], result)

    @builtins.property
    def to(self) -> typing.Optional[typing.List["AuthorizationPolicySpecRulesTo"]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRules#to
        '''
        result = self._values.get("to")
        return typing.cast(typing.Optional[typing.List["AuthorizationPolicySpecRulesTo"]], result)

    @builtins.property
    def when(self) -> typing.Optional[typing.List["AuthorizationPolicySpecRulesWhen"]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRules#when
        '''
        result = self._values.get("when")
        return typing.cast(typing.Optional[typing.List["AuthorizationPolicySpecRulesWhen"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.AuthorizationPolicySpecRulesFrom",
    jsii_struct_bases=[],
    name_mapping={"source": "source"},
)
class AuthorizationPolicySpecRulesFrom:
    def __init__(
        self,
        *,
        source: typing.Optional["AuthorizationPolicySpecRulesFromSource"] = None,
    ) -> None:
        '''
        :param source: Source specifies the source of a request.

        :schema: AuthorizationPolicySpecRulesFrom
        '''
        if isinstance(source, dict):
            source = AuthorizationPolicySpecRulesFromSource(**source)
        self._values: typing.Dict[str, typing.Any] = {}
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def source(self) -> typing.Optional["AuthorizationPolicySpecRulesFromSource"]:
        '''Source specifies the source of a request.

        :schema: AuthorizationPolicySpecRulesFrom#source
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional["AuthorizationPolicySpecRulesFromSource"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecRulesFrom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.AuthorizationPolicySpecRulesFromSource",
    jsii_struct_bases=[],
    name_mapping={
        "ip_blocks": "ipBlocks",
        "namespaces": "namespaces",
        "not_ip_blocks": "notIpBlocks",
        "not_namespaces": "notNamespaces",
        "not_principals": "notPrincipals",
        "not_remote_ip_blocks": "notRemoteIpBlocks",
        "not_request_principals": "notRequestPrincipals",
        "principals": "principals",
        "remote_ip_blocks": "remoteIpBlocks",
        "request_principals": "requestPrincipals",
    },
)
class AuthorizationPolicySpecRulesFromSource:
    def __init__(
        self,
        *,
        ip_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_ip_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_remote_ip_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_request_principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        remote_ip_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        request_principals: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Source specifies the source of a request.

        :param ip_blocks: Optional.
        :param namespaces: Optional.
        :param not_ip_blocks: Optional.
        :param not_namespaces: Optional.
        :param not_principals: Optional.
        :param not_remote_ip_blocks: Optional.
        :param not_request_principals: Optional.
        :param principals: Optional.
        :param remote_ip_blocks: Optional.
        :param request_principals: Optional.

        :schema: AuthorizationPolicySpecRulesFromSource
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ip_blocks is not None:
            self._values["ip_blocks"] = ip_blocks
        if namespaces is not None:
            self._values["namespaces"] = namespaces
        if not_ip_blocks is not None:
            self._values["not_ip_blocks"] = not_ip_blocks
        if not_namespaces is not None:
            self._values["not_namespaces"] = not_namespaces
        if not_principals is not None:
            self._values["not_principals"] = not_principals
        if not_remote_ip_blocks is not None:
            self._values["not_remote_ip_blocks"] = not_remote_ip_blocks
        if not_request_principals is not None:
            self._values["not_request_principals"] = not_request_principals
        if principals is not None:
            self._values["principals"] = principals
        if remote_ip_blocks is not None:
            self._values["remote_ip_blocks"] = remote_ip_blocks
        if request_principals is not None:
            self._values["request_principals"] = request_principals

    @builtins.property
    def ip_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#ipBlocks
        '''
        result = self._values.get("ip_blocks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#namespaces
        '''
        result = self._values.get("namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_ip_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#notIpBlocks
        '''
        result = self._values.get("not_ip_blocks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#notNamespaces
        '''
        result = self._values.get("not_namespaces")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#notPrincipals
        '''
        result = self._values.get("not_principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_remote_ip_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#notRemoteIpBlocks
        '''
        result = self._values.get("not_remote_ip_blocks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_request_principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#notRequestPrincipals
        '''
        result = self._values.get("not_request_principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#principals
        '''
        result = self._values.get("principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def remote_ip_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#remoteIpBlocks
        '''
        result = self._values.get("remote_ip_blocks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def request_principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesFromSource#requestPrincipals
        '''
        result = self._values.get("request_principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecRulesFromSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.AuthorizationPolicySpecRulesTo",
    jsii_struct_bases=[],
    name_mapping={"operation": "operation"},
)
class AuthorizationPolicySpecRulesTo:
    def __init__(
        self,
        *,
        operation: typing.Optional["AuthorizationPolicySpecRulesToOperation"] = None,
    ) -> None:
        '''
        :param operation: Operation specifies the operation of a request.

        :schema: AuthorizationPolicySpecRulesTo
        '''
        if isinstance(operation, dict):
            operation = AuthorizationPolicySpecRulesToOperation(**operation)
        self._values: typing.Dict[str, typing.Any] = {}
        if operation is not None:
            self._values["operation"] = operation

    @builtins.property
    def operation(self) -> typing.Optional["AuthorizationPolicySpecRulesToOperation"]:
        '''Operation specifies the operation of a request.

        :schema: AuthorizationPolicySpecRulesTo#operation
        '''
        result = self._values.get("operation")
        return typing.cast(typing.Optional["AuthorizationPolicySpecRulesToOperation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecRulesTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.AuthorizationPolicySpecRulesToOperation",
    jsii_struct_bases=[],
    name_mapping={
        "hosts": "hosts",
        "methods": "methods",
        "not_hosts": "notHosts",
        "not_methods": "notMethods",
        "not_paths": "notPaths",
        "not_ports": "notPorts",
        "paths": "paths",
        "ports": "ports",
    },
)
class AuthorizationPolicySpecRulesToOperation:
    def __init__(
        self,
        *,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_ports: typing.Optional[typing.Sequence[builtins.str]] = None,
        paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        ports: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Operation specifies the operation of a request.

        :param hosts: Optional.
        :param methods: Optional.
        :param not_hosts: Optional.
        :param not_methods: Optional.
        :param not_paths: Optional.
        :param not_ports: Optional.
        :param paths: Optional.
        :param ports: Optional.

        :schema: AuthorizationPolicySpecRulesToOperation
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if hosts is not None:
            self._values["hosts"] = hosts
        if methods is not None:
            self._values["methods"] = methods
        if not_hosts is not None:
            self._values["not_hosts"] = not_hosts
        if not_methods is not None:
            self._values["not_methods"] = not_methods
        if not_paths is not None:
            self._values["not_paths"] = not_paths
        if not_ports is not None:
            self._values["not_ports"] = not_ports
        if paths is not None:
            self._values["paths"] = paths
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#hosts
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#methods
        '''
        result = self._values.get("methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#notHosts
        '''
        result = self._values.get("not_hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#notMethods
        '''
        result = self._values.get("not_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#notPaths
        '''
        result = self._values.get("not_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_ports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#notPorts
        '''
        result = self._values.get("not_ports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#paths
        '''
        result = self._values.get("paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesToOperation#ports
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecRulesToOperation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.AuthorizationPolicySpecRulesWhen",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "not_values": "notValues", "values": "values"},
)
class AuthorizationPolicySpecRulesWhen:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        not_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The name of an Istio attribute.
        :param not_values: Optional.
        :param values: Optional.

        :schema: AuthorizationPolicySpecRulesWhen
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if not_values is not None:
            self._values["not_values"] = not_values
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The name of an Istio attribute.

        :schema: AuthorizationPolicySpecRulesWhen#key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def not_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesWhen#notValues
        '''
        result = self._values.get("not_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        :schema: AuthorizationPolicySpecRulesWhen#values
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecRulesWhen(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.AuthorizationPolicySpecSelector",
    jsii_struct_bases=[],
    name_mapping={"match_labels": "matchLabels"},
)
class AuthorizationPolicySpecSelector:
    def __init__(
        self,
        *,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Optional.

        :param match_labels: 

        :schema: AuthorizationPolicySpecSelector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: AuthorizationPolicySpecSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationPolicySpecSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PeerAuthentication(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistiosecurity.PeerAuthentication",
):
    '''
    :schema: PeerAuthentication
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["PeerAuthenticationSpec"] = None,
    ) -> None:
        '''Defines a "PeerAuthentication" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: PeerAuthentication defines how traffic will be tunneled (or not) to the sidecar.
        '''
        props = PeerAuthenticationProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["PeerAuthenticationSpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "PeerAuthentication".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: PeerAuthentication defines how traffic will be tunneled (or not) to the sidecar.
        '''
        props = PeerAuthenticationProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "PeerAuthentication".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistiosecurity.PeerAuthenticationProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class PeerAuthenticationProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["PeerAuthenticationSpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: PeerAuthentication defines how traffic will be tunneled (or not) to the sidecar.

        :schema: PeerAuthentication
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = PeerAuthenticationSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: PeerAuthentication#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["PeerAuthenticationSpec"]:
        '''PeerAuthentication defines how traffic will be tunneled (or not) to the sidecar.

        :schema: PeerAuthentication#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["PeerAuthenticationSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PeerAuthenticationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.PeerAuthenticationSpec",
    jsii_struct_bases=[],
    name_mapping={
        "mtls": "mtls",
        "port_level_mtls": "portLevelMtls",
        "selector": "selector",
    },
)
class PeerAuthenticationSpec:
    def __init__(
        self,
        *,
        mtls: typing.Optional["PeerAuthenticationSpecMtls"] = None,
        port_level_mtls: typing.Optional[typing.Mapping[builtins.str, "PeerAuthenticationSpecPortLevelMtls"]] = None,
        selector: typing.Optional["PeerAuthenticationSpecSelector"] = None,
    ) -> None:
        '''PeerAuthentication defines how traffic will be tunneled (or not) to the sidecar.

        :param mtls: Mutual TLS settings for workload.
        :param port_level_mtls: Port specific mutual TLS settings.
        :param selector: The selector determines the workloads to apply the ChannelAuthentication on.

        :schema: PeerAuthenticationSpec
        '''
        if isinstance(mtls, dict):
            mtls = PeerAuthenticationSpecMtls(**mtls)
        if isinstance(selector, dict):
            selector = PeerAuthenticationSpecSelector(**selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if mtls is not None:
            self._values["mtls"] = mtls
        if port_level_mtls is not None:
            self._values["port_level_mtls"] = port_level_mtls
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def mtls(self) -> typing.Optional["PeerAuthenticationSpecMtls"]:
        '''Mutual TLS settings for workload.

        :schema: PeerAuthenticationSpec#mtls
        '''
        result = self._values.get("mtls")
        return typing.cast(typing.Optional["PeerAuthenticationSpecMtls"], result)

    @builtins.property
    def port_level_mtls(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "PeerAuthenticationSpecPortLevelMtls"]]:
        '''Port specific mutual TLS settings.

        :schema: PeerAuthenticationSpec#portLevelMtls
        '''
        result = self._values.get("port_level_mtls")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "PeerAuthenticationSpecPortLevelMtls"]], result)

    @builtins.property
    def selector(self) -> typing.Optional["PeerAuthenticationSpecSelector"]:
        '''The selector determines the workloads to apply the ChannelAuthentication on.

        :schema: PeerAuthenticationSpec#selector
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional["PeerAuthenticationSpecSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PeerAuthenticationSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.PeerAuthenticationSpecMtls",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode"},
)
class PeerAuthenticationSpecMtls:
    def __init__(
        self,
        *,
        mode: typing.Optional["PeerAuthenticationSpecMtlsMode"] = None,
    ) -> None:
        '''Mutual TLS settings for workload.

        :param mode: Defines the mTLS mode used for peer authentication.

        :schema: PeerAuthenticationSpecMtls
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def mode(self) -> typing.Optional["PeerAuthenticationSpecMtlsMode"]:
        '''Defines the mTLS mode used for peer authentication.

        :schema: PeerAuthenticationSpecMtls#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["PeerAuthenticationSpecMtlsMode"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PeerAuthenticationSpecMtls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistiosecurity.PeerAuthenticationSpecMtlsMode")
class PeerAuthenticationSpecMtlsMode(enum.Enum):
    '''Defines the mTLS mode used for peer authentication.

    :schema: PeerAuthenticationSpecMtlsMode
    '''

    UNSET = "UNSET"
    '''UNSET.'''
    DISABLE = "DISABLE"
    '''DISABLE.'''
    PERMISSIVE = "PERMISSIVE"
    '''PERMISSIVE.'''
    STRICT = "STRICT"
    '''STRICT.'''


@jsii.data_type(
    jsii_type="ioistiosecurity.PeerAuthenticationSpecPortLevelMtls",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode"},
)
class PeerAuthenticationSpecPortLevelMtls:
    def __init__(
        self,
        *,
        mode: typing.Optional["PeerAuthenticationSpecPortLevelMtlsMode"] = None,
    ) -> None:
        '''
        :param mode: Defines the mTLS mode used for peer authentication.

        :schema: PeerAuthenticationSpecPortLevelMtls
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def mode(self) -> typing.Optional["PeerAuthenticationSpecPortLevelMtlsMode"]:
        '''Defines the mTLS mode used for peer authentication.

        :schema: PeerAuthenticationSpecPortLevelMtls#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["PeerAuthenticationSpecPortLevelMtlsMode"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PeerAuthenticationSpecPortLevelMtls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistiosecurity.PeerAuthenticationSpecPortLevelMtlsMode")
class PeerAuthenticationSpecPortLevelMtlsMode(enum.Enum):
    '''Defines the mTLS mode used for peer authentication.

    :schema: PeerAuthenticationSpecPortLevelMtlsMode
    '''

    UNSET = "UNSET"
    '''UNSET.'''
    DISABLE = "DISABLE"
    '''DISABLE.'''
    PERMISSIVE = "PERMISSIVE"
    '''PERMISSIVE.'''
    STRICT = "STRICT"
    '''STRICT.'''


@jsii.data_type(
    jsii_type="ioistiosecurity.PeerAuthenticationSpecSelector",
    jsii_struct_bases=[],
    name_mapping={"match_labels": "matchLabels"},
)
class PeerAuthenticationSpecSelector:
    def __init__(
        self,
        *,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''The selector determines the workloads to apply the ChannelAuthentication on.

        :param match_labels: 

        :schema: PeerAuthenticationSpecSelector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: PeerAuthenticationSpecSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PeerAuthenticationSpecSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RequestAuthentication(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistiosecurity.RequestAuthentication",
):
    '''
    :schema: RequestAuthentication
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["RequestAuthenticationSpec"] = None,
    ) -> None:
        '''Defines a "RequestAuthentication" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: RequestAuthentication defines what request authentication methods are supported by a workload.
        '''
        props = RequestAuthenticationProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["RequestAuthenticationSpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "RequestAuthentication".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: RequestAuthentication defines what request authentication methods are supported by a workload.
        '''
        props = RequestAuthenticationProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "RequestAuthentication".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistiosecurity.RequestAuthenticationProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class RequestAuthenticationProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["RequestAuthenticationSpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: RequestAuthentication defines what request authentication methods are supported by a workload.

        :schema: RequestAuthentication
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = RequestAuthenticationSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: RequestAuthentication#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["RequestAuthenticationSpec"]:
        '''RequestAuthentication defines what request authentication methods are supported by a workload.

        :schema: RequestAuthentication#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["RequestAuthenticationSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequestAuthenticationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.RequestAuthenticationSpec",
    jsii_struct_bases=[],
    name_mapping={"jwt_rules": "jwtRules", "selector": "selector"},
)
class RequestAuthenticationSpec:
    def __init__(
        self,
        *,
        jwt_rules: typing.Optional[typing.Sequence["RequestAuthenticationSpecJwtRules"]] = None,
        selector: typing.Optional["RequestAuthenticationSpecSelector"] = None,
    ) -> None:
        '''RequestAuthentication defines what request authentication methods are supported by a workload.

        :param jwt_rules: Define the list of JWTs that can be validated at the selected workloads' proxy.
        :param selector: Optional.

        :schema: RequestAuthenticationSpec
        '''
        if isinstance(selector, dict):
            selector = RequestAuthenticationSpecSelector(**selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if jwt_rules is not None:
            self._values["jwt_rules"] = jwt_rules
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def jwt_rules(
        self,
    ) -> typing.Optional[typing.List["RequestAuthenticationSpecJwtRules"]]:
        '''Define the list of JWTs that can be validated at the selected workloads' proxy.

        :schema: RequestAuthenticationSpec#jwtRules
        '''
        result = self._values.get("jwt_rules")
        return typing.cast(typing.Optional[typing.List["RequestAuthenticationSpecJwtRules"]], result)

    @builtins.property
    def selector(self) -> typing.Optional["RequestAuthenticationSpecSelector"]:
        '''Optional.

        :schema: RequestAuthenticationSpec#selector
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional["RequestAuthenticationSpecSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequestAuthenticationSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.RequestAuthenticationSpecJwtRules",
    jsii_struct_bases=[],
    name_mapping={
        "audiences": "audiences",
        "forward_original_token": "forwardOriginalToken",
        "from_headers": "fromHeaders",
        "from_params": "fromParams",
        "issuer": "issuer",
        "jwks": "jwks",
        "jwks_uri": "jwksUri",
        "output_payload_to_header": "outputPayloadToHeader",
    },
)
class RequestAuthenticationSpecJwtRules:
    def __init__(
        self,
        *,
        audiences: typing.Optional[typing.Sequence[builtins.str]] = None,
        forward_original_token: typing.Optional[builtins.bool] = None,
        from_headers: typing.Optional[typing.Sequence["RequestAuthenticationSpecJwtRulesFromHeaders"]] = None,
        from_params: typing.Optional[typing.Sequence[builtins.str]] = None,
        issuer: typing.Optional[builtins.str] = None,
        jwks: typing.Optional[builtins.str] = None,
        jwks_uri: typing.Optional[builtins.str] = None,
        output_payload_to_header: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audiences: 
        :param forward_original_token: If set to true, the original token will be kept for the upstream request.
        :param from_headers: List of header locations from which JWT is expected.
        :param from_params: List of query parameters from which JWT is expected.
        :param issuer: Identifies the issuer that issued the JWT.
        :param jwks: JSON Web Key Set of public keys to validate signature of the JWT.
        :param jwks_uri: 
        :param output_payload_to_header: 

        :schema: RequestAuthenticationSpecJwtRules
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if audiences is not None:
            self._values["audiences"] = audiences
        if forward_original_token is not None:
            self._values["forward_original_token"] = forward_original_token
        if from_headers is not None:
            self._values["from_headers"] = from_headers
        if from_params is not None:
            self._values["from_params"] = from_params
        if issuer is not None:
            self._values["issuer"] = issuer
        if jwks is not None:
            self._values["jwks"] = jwks
        if jwks_uri is not None:
            self._values["jwks_uri"] = jwks_uri
        if output_payload_to_header is not None:
            self._values["output_payload_to_header"] = output_payload_to_header

    @builtins.property
    def audiences(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: RequestAuthenticationSpecJwtRules#audiences
        '''
        result = self._values.get("audiences")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def forward_original_token(self) -> typing.Optional[builtins.bool]:
        '''If set to true, the original token will be kept for the upstream request.

        :schema: RequestAuthenticationSpecJwtRules#forwardOriginalToken
        '''
        result = self._values.get("forward_original_token")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def from_headers(
        self,
    ) -> typing.Optional[typing.List["RequestAuthenticationSpecJwtRulesFromHeaders"]]:
        '''List of header locations from which JWT is expected.

        :schema: RequestAuthenticationSpecJwtRules#fromHeaders
        '''
        result = self._values.get("from_headers")
        return typing.cast(typing.Optional[typing.List["RequestAuthenticationSpecJwtRulesFromHeaders"]], result)

    @builtins.property
    def from_params(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of query parameters from which JWT is expected.

        :schema: RequestAuthenticationSpecJwtRules#fromParams
        '''
        result = self._values.get("from_params")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def issuer(self) -> typing.Optional[builtins.str]:
        '''Identifies the issuer that issued the JWT.

        :schema: RequestAuthenticationSpecJwtRules#issuer
        '''
        result = self._values.get("issuer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jwks(self) -> typing.Optional[builtins.str]:
        '''JSON Web Key Set of public keys to validate signature of the JWT.

        :schema: RequestAuthenticationSpecJwtRules#jwks
        '''
        result = self._values.get("jwks")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jwks_uri(self) -> typing.Optional[builtins.str]:
        '''
        :schema: RequestAuthenticationSpecJwtRules#jwksUri
        '''
        result = self._values.get("jwks_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_payload_to_header(self) -> typing.Optional[builtins.str]:
        '''
        :schema: RequestAuthenticationSpecJwtRules#outputPayloadToHeader
        '''
        result = self._values.get("output_payload_to_header")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequestAuthenticationSpecJwtRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.RequestAuthenticationSpecJwtRulesFromHeaders",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "prefix": "prefix"},
)
class RequestAuthenticationSpecJwtRulesFromHeaders:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The HTTP header name.
        :param prefix: The prefix that should be stripped before decoding the token.

        :schema: RequestAuthenticationSpecJwtRulesFromHeaders
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The HTTP header name.

        :schema: RequestAuthenticationSpecJwtRulesFromHeaders#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix that should be stripped before decoding the token.

        :schema: RequestAuthenticationSpecJwtRulesFromHeaders#prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequestAuthenticationSpecJwtRulesFromHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiosecurity.RequestAuthenticationSpecSelector",
    jsii_struct_bases=[],
    name_mapping={"match_labels": "matchLabels"},
)
class RequestAuthenticationSpecSelector:
    def __init__(
        self,
        *,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Optional.

        :param match_labels: 

        :schema: RequestAuthenticationSpecSelector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: RequestAuthenticationSpecSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequestAuthenticationSpecSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AuthorizationPolicy",
    "AuthorizationPolicyProps",
    "AuthorizationPolicySpec",
    "AuthorizationPolicySpecAction",
    "AuthorizationPolicySpecProvider",
    "AuthorizationPolicySpecRules",
    "AuthorizationPolicySpecRulesFrom",
    "AuthorizationPolicySpecRulesFromSource",
    "AuthorizationPolicySpecRulesTo",
    "AuthorizationPolicySpecRulesToOperation",
    "AuthorizationPolicySpecRulesWhen",
    "AuthorizationPolicySpecSelector",
    "PeerAuthentication",
    "PeerAuthenticationProps",
    "PeerAuthenticationSpec",
    "PeerAuthenticationSpecMtls",
    "PeerAuthenticationSpecMtlsMode",
    "PeerAuthenticationSpecPortLevelMtls",
    "PeerAuthenticationSpecPortLevelMtlsMode",
    "PeerAuthenticationSpecSelector",
    "RequestAuthentication",
    "RequestAuthenticationProps",
    "RequestAuthenticationSpec",
    "RequestAuthenticationSpecJwtRules",
    "RequestAuthenticationSpecJwtRulesFromHeaders",
    "RequestAuthenticationSpecSelector",
]

publication.publish()
