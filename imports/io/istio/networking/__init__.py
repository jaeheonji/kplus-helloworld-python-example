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


class DestinationRule(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistionetworking.DestinationRule",
):
    '''
    :schema: DestinationRule
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["DestinationRuleSpec"] = None,
    ) -> None:
        '''Defines a "DestinationRule" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: Configuration affecting load balancing, outlier detection, etc. See more details at: https://istio.io/docs/reference/config/networking/destination-rule.html
        '''
        props = DestinationRuleProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["DestinationRuleSpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "DestinationRule".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: Configuration affecting load balancing, outlier detection, etc. See more details at: https://istio.io/docs/reference/config/networking/destination-rule.html
        '''
        props = DestinationRuleProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "DestinationRule".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class DestinationRuleProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["DestinationRuleSpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: Configuration affecting load balancing, outlier detection, etc. See more details at: https://istio.io/docs/reference/config/networking/destination-rule.html

        :schema: DestinationRule
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = DestinationRuleSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: DestinationRule#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["DestinationRuleSpec"]:
        '''Configuration affecting load balancing, outlier detection, etc.

        See more details at: https://istio.io/docs/reference/config/networking/destination-rule.html

        :schema: DestinationRule#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["DestinationRuleSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpec",
    jsii_struct_bases=[],
    name_mapping={
        "export_to": "exportTo",
        "host": "host",
        "subsets": "subsets",
        "traffic_policy": "trafficPolicy",
        "workload_selector": "workloadSelector",
    },
)
class DestinationRuleSpec:
    def __init__(
        self,
        *,
        export_to: typing.Optional[typing.Sequence[builtins.str]] = None,
        host: typing.Optional[builtins.str] = None,
        subsets: typing.Optional[typing.Sequence["DestinationRuleSpecSubsets"]] = None,
        traffic_policy: typing.Optional["DestinationRuleSpecTrafficPolicy"] = None,
        workload_selector: typing.Optional["DestinationRuleSpecWorkloadSelector"] = None,
    ) -> None:
        '''Configuration affecting load balancing, outlier detection, etc.

        See more details at: https://istio.io/docs/reference/config/networking/destination-rule.html

        :param export_to: A list of namespaces to which this destination rule is exported.
        :param host: The name of a service from the service registry.
        :param subsets: 
        :param traffic_policy: 
        :param workload_selector: 

        :schema: DestinationRuleSpec
        '''
        if isinstance(traffic_policy, dict):
            traffic_policy = DestinationRuleSpecTrafficPolicy(**traffic_policy)
        if isinstance(workload_selector, dict):
            workload_selector = DestinationRuleSpecWorkloadSelector(**workload_selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if export_to is not None:
            self._values["export_to"] = export_to
        if host is not None:
            self._values["host"] = host
        if subsets is not None:
            self._values["subsets"] = subsets
        if traffic_policy is not None:
            self._values["traffic_policy"] = traffic_policy
        if workload_selector is not None:
            self._values["workload_selector"] = workload_selector

    @builtins.property
    def export_to(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of namespaces to which this destination rule is exported.

        :schema: DestinationRuleSpec#exportTo
        '''
        result = self._values.get("export_to")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The name of a service from the service registry.

        :schema: DestinationRuleSpec#host
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subsets(self) -> typing.Optional[typing.List["DestinationRuleSpecSubsets"]]:
        '''
        :schema: DestinationRuleSpec#subsets
        '''
        result = self._values.get("subsets")
        return typing.cast(typing.Optional[typing.List["DestinationRuleSpecSubsets"]], result)

    @builtins.property
    def traffic_policy(self) -> typing.Optional["DestinationRuleSpecTrafficPolicy"]:
        '''
        :schema: DestinationRuleSpec#trafficPolicy
        '''
        result = self._values.get("traffic_policy")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicy"], result)

    @builtins.property
    def workload_selector(
        self,
    ) -> typing.Optional["DestinationRuleSpecWorkloadSelector"]:
        '''
        :schema: DestinationRuleSpec#workloadSelector
        '''
        result = self._values.get("workload_selector")
        return typing.cast(typing.Optional["DestinationRuleSpecWorkloadSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsets",
    jsii_struct_bases=[],
    name_mapping={
        "labels": "labels",
        "name": "name",
        "traffic_policy": "trafficPolicy",
    },
)
class DestinationRuleSpecSubsets:
    def __init__(
        self,
        *,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        traffic_policy: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicy"] = None,
    ) -> None:
        '''
        :param labels: 
        :param name: Name of the subset.
        :param traffic_policy: Traffic policies that apply to this subset.

        :schema: DestinationRuleSpecSubsets
        '''
        if isinstance(traffic_policy, dict):
            traffic_policy = DestinationRuleSpecSubsetsTrafficPolicy(**traffic_policy)
        self._values: typing.Dict[str, typing.Any] = {}
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name
        if traffic_policy is not None:
            self._values["traffic_policy"] = traffic_policy

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: DestinationRuleSpecSubsets#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the subset.

        :schema: DestinationRuleSpecSubsets#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def traffic_policy(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicy"]:
        '''Traffic policies that apply to this subset.

        :schema: DestinationRuleSpecSubsets#trafficPolicy
        '''
        result = self._values.get("traffic_policy")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "load_balancer": "loadBalancer",
        "outlier_detection": "outlierDetection",
        "port_level_settings": "portLevelSettings",
        "tls": "tls",
        "tunnel": "tunnel",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicy:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPool"] = None,
        load_balancer: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer"] = None,
        outlier_detection: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection"] = None,
        port_level_settings: typing.Optional[typing.Sequence["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings"]] = None,
        tls: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyTls"] = None,
        tunnel: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyTunnel"] = None,
    ) -> None:
        '''Traffic policies that apply to this subset.

        :param connection_pool: 
        :param load_balancer: Settings controlling the load balancer algorithms.
        :param outlier_detection: 
        :param port_level_settings: Traffic policies specific to individual ports.
        :param tls: TLS related settings for connections to the upstream service.
        :param tunnel: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicy
        '''
        if isinstance(connection_pool, dict):
            connection_pool = DestinationRuleSpecSubsetsTrafficPolicyConnectionPool(**connection_pool)
        if isinstance(load_balancer, dict):
            load_balancer = DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer(**load_balancer)
        if isinstance(outlier_detection, dict):
            outlier_detection = DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection(**outlier_detection)
        if isinstance(tls, dict):
            tls = DestinationRuleSpecSubsetsTrafficPolicyTls(**tls)
        if isinstance(tunnel, dict):
            tunnel = DestinationRuleSpecSubsetsTrafficPolicyTunnel(**tunnel)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if port_level_settings is not None:
            self._values["port_level_settings"] = port_level_settings
        if tls is not None:
            self._values["tls"] = tls
        if tunnel is not None:
            self._values["tunnel"] = tunnel

    @builtins.property
    def connection_pool(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPool"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicy#connectionPool
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPool"], result)

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer"]:
        '''Settings controlling the load balancer algorithms.

        :schema: DestinationRuleSpecSubsetsTrafficPolicy#loadBalancer
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer"], result)

    @builtins.property
    def outlier_detection(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicy#outlierDetection
        '''
        result = self._values.get("outlier_detection")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection"], result)

    @builtins.property
    def port_level_settings(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings"]]:
        '''Traffic policies specific to individual ports.

        :schema: DestinationRuleSpecSubsetsTrafficPolicy#portLevelSettings
        '''
        result = self._values.get("port_level_settings")
        return typing.cast(typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings"]], result)

    @builtins.property
    def tls(self) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyTls"]:
        '''TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecSubsetsTrafficPolicy#tls
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyTls"], result)

    @builtins.property
    def tunnel(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyTunnel"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicy#tunnel
        '''
        result = self._values.get("tunnel")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyTunnel"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"http": "http", "tcp": "tcp"},
)
class DestinationRuleSpecSubsetsTrafficPolicyConnectionPool:
    def __init__(
        self,
        *,
        http: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp"] = None,
        tcp: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp"] = None,
    ) -> None:
        '''
        :param http: HTTP connection pool settings.
        :param tcp: Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPool
        '''
        if isinstance(http, dict):
            http = DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp(**http)
        if isinstance(tcp, dict):
            tcp = DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp(**tcp)
        self._values: typing.Dict[str, typing.Any] = {}
        if http is not None:
            self._values["http"] = http
        if tcp is not None:
            self._values["tcp"] = tcp

    @builtins.property
    def http(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp"]:
        '''HTTP connection pool settings.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPool#http
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp"], result)

    @builtins.property
    def tcp(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp"]:
        '''Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPool#tcp
        '''
        result = self._values.get("tcp")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp",
    jsii_struct_bases=[],
    name_mapping={
        "h2_upgrade_policy": "h2UpgradePolicy",
        "http1_max_pending_requests": "http1MaxPendingRequests",
        "http2_max_requests": "http2MaxRequests",
        "idle_timeout": "idleTimeout",
        "max_requests_per_connection": "maxRequestsPerConnection",
        "max_retries": "maxRetries",
        "use_client_protocol": "useClientProtocol",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp:
    def __init__(
        self,
        *,
        h2_upgrade_policy: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttpH2UpgradePolicy"] = None,
        http1_max_pending_requests: typing.Optional[jsii.Number] = None,
        http2_max_requests: typing.Optional[jsii.Number] = None,
        idle_timeout: typing.Optional[builtins.str] = None,
        max_requests_per_connection: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        use_client_protocol: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''HTTP connection pool settings.

        :param h2_upgrade_policy: Specify if http1.1 connection should be upgraded to http2 for the associated destination.
        :param http1_max_pending_requests: Maximum number of pending HTTP requests to a destination.
        :param http2_max_requests: Maximum number of requests to a backend.
        :param idle_timeout: The idle timeout for upstream connection pool connections.
        :param max_requests_per_connection: Maximum number of requests per connection to a backend.
        :param max_retries: 
        :param use_client_protocol: If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if h2_upgrade_policy is not None:
            self._values["h2_upgrade_policy"] = h2_upgrade_policy
        if http1_max_pending_requests is not None:
            self._values["http1_max_pending_requests"] = http1_max_pending_requests
        if http2_max_requests is not None:
            self._values["http2_max_requests"] = http2_max_requests
        if idle_timeout is not None:
            self._values["idle_timeout"] = idle_timeout
        if max_requests_per_connection is not None:
            self._values["max_requests_per_connection"] = max_requests_per_connection
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if use_client_protocol is not None:
            self._values["use_client_protocol"] = use_client_protocol

    @builtins.property
    def h2_upgrade_policy(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttpH2UpgradePolicy"]:
        '''Specify if http1.1 connection should be upgraded to http2 for the associated destination.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#h2UpgradePolicy
        '''
        result = self._values.get("h2_upgrade_policy")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttpH2UpgradePolicy"], result)

    @builtins.property
    def http1_max_pending_requests(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of pending HTTP requests to a destination.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#http1MaxPendingRequests
        '''
        result = self._values.get("http1_max_pending_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http2_max_requests(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of requests to a backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#http2MaxRequests
        '''
        result = self._values.get("http2_max_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def idle_timeout(self) -> typing.Optional[builtins.str]:
        '''The idle timeout for upstream connection pool connections.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#idleTimeout
        '''
        result = self._values.get("idle_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_requests_per_connection(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of requests per connection to a backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#maxRequestsPerConnection
        '''
        result = self._values.get("max_requests_per_connection")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#maxRetries
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def use_client_protocol(self) -> typing.Optional[builtins.bool]:
        '''If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp#useClientProtocol
        '''
        result = self._values.get("use_client_protocol")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttpH2UpgradePolicy"
)
class DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttpH2UpgradePolicy(
    enum.Enum,
):
    '''Specify if http1.1 connection should be upgraded to http2 for the associated destination.

    :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttpH2UpgradePolicy
    '''

    DEFAULT = "DEFAULT"
    '''DEFAULT.'''
    DO_NOT_UPGRADE = "DO_NOT_UPGRADE"
    '''DO_NOT_UPGRADE.'''
    UPGRADE = "UPGRADE"
    '''UPGRADE.'''


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp",
    jsii_struct_bases=[],
    name_mapping={
        "connect_timeout": "connectTimeout",
        "max_connections": "maxConnections",
        "tcp_keepalive": "tcpKeepalive",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp:
    def __init__(
        self,
        *,
        connect_timeout: typing.Optional[builtins.str] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        tcp_keepalive: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive"] = None,
    ) -> None:
        '''Settings common to both HTTP and TCP upstream connections.

        :param connect_timeout: TCP connection timeout.
        :param max_connections: Maximum number of HTTP1 /TCP connections to a destination host.
        :param tcp_keepalive: If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp
        '''
        if isinstance(tcp_keepalive, dict):
            tcp_keepalive = DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive(**tcp_keepalive)
        self._values: typing.Dict[str, typing.Any] = {}
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if max_connections is not None:
            self._values["max_connections"] = max_connections
        if tcp_keepalive is not None:
            self._values["tcp_keepalive"] = tcp_keepalive

    @builtins.property
    def connect_timeout(self) -> typing.Optional[builtins.str]:
        '''TCP connection timeout.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp#connectTimeout
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of HTTP1 /TCP connections to a destination host.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp#maxConnections
        '''
        result = self._values.get("max_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tcp_keepalive(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive"]:
        '''If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp#tcpKeepalive
        '''
        result = self._values.get("tcp_keepalive")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "probes": "probes", "time": "time"},
)
class DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive:
    def __init__(
        self,
        *,
        interval: typing.Optional[builtins.str] = None,
        probes: typing.Optional[jsii.Number] = None,
        time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :param interval: The time duration between keep-alive probes.
        :param probes: 
        :param time: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if interval is not None:
            self._values["interval"] = interval
        if probes is not None:
            self._values["probes"] = probes
        if time is not None:
            self._values["time"] = time

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''The time duration between keep-alive probes.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive#interval
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def probes(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive#probes
        '''
        result = self._values.get("probes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def time(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive#time
        '''
        result = self._values.get("time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "consistent_hash": "consistentHash",
        "locality_lb_setting": "localityLbSetting",
        "simple": "simple",
        "warmup_duration_secs": "warmupDurationSecs",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer:
    def __init__(
        self,
        *,
        consistent_hash: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash"] = None,
        locality_lb_setting: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting"] = None,
        simple: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerSimple"] = None,
        warmup_duration_secs: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Settings controlling the load balancer algorithms.

        :param consistent_hash: 
        :param locality_lb_setting: 
        :param simple: 
        :param warmup_duration_secs: Represents the warmup duration of Service.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer
        '''
        if isinstance(consistent_hash, dict):
            consistent_hash = DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash(**consistent_hash)
        if isinstance(locality_lb_setting, dict):
            locality_lb_setting = DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting(**locality_lb_setting)
        self._values: typing.Dict[str, typing.Any] = {}
        if consistent_hash is not None:
            self._values["consistent_hash"] = consistent_hash
        if locality_lb_setting is not None:
            self._values["locality_lb_setting"] = locality_lb_setting
        if simple is not None:
            self._values["simple"] = simple
        if warmup_duration_secs is not None:
            self._values["warmup_duration_secs"] = warmup_duration_secs

    @builtins.property
    def consistent_hash(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer#consistentHash
        '''
        result = self._values.get("consistent_hash")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash"], result)

    @builtins.property
    def locality_lb_setting(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer#localityLbSetting
        '''
        result = self._values.get("locality_lb_setting")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting"], result)

    @builtins.property
    def simple(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerSimple"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer#simple
        '''
        result = self._values.get("simple")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerSimple"], result)

    @builtins.property
    def warmup_duration_secs(self) -> typing.Optional[builtins.str]:
        '''Represents the warmup duration of Service.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer#warmupDurationSecs
        '''
        result = self._values.get("warmup_duration_secs")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash",
    jsii_struct_bases=[],
    name_mapping={
        "http_cookie": "httpCookie",
        "http_header_name": "httpHeaderName",
        "http_query_parameter_name": "httpQueryParameterName",
        "minimum_ring_size": "minimumRingSize",
        "use_source_ip": "useSourceIp",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash:
    def __init__(
        self,
        *,
        http_cookie: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie"] = None,
        http_header_name: typing.Optional[builtins.str] = None,
        http_query_parameter_name: typing.Optional[builtins.str] = None,
        minimum_ring_size: typing.Optional[jsii.Number] = None,
        use_source_ip: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param http_cookie: Hash based on HTTP cookie.
        :param http_header_name: Hash based on a specific HTTP header.
        :param http_query_parameter_name: Hash based on a specific HTTP query parameter.
        :param minimum_ring_size: 
        :param use_source_ip: Hash based on the source IP address.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash
        '''
        if isinstance(http_cookie, dict):
            http_cookie = DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie(**http_cookie)
        self._values: typing.Dict[str, typing.Any] = {}
        if http_cookie is not None:
            self._values["http_cookie"] = http_cookie
        if http_header_name is not None:
            self._values["http_header_name"] = http_header_name
        if http_query_parameter_name is not None:
            self._values["http_query_parameter_name"] = http_query_parameter_name
        if minimum_ring_size is not None:
            self._values["minimum_ring_size"] = minimum_ring_size
        if use_source_ip is not None:
            self._values["use_source_ip"] = use_source_ip

    @builtins.property
    def http_cookie(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie"]:
        '''Hash based on HTTP cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash#httpCookie
        '''
        result = self._values.get("http_cookie")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie"], result)

    @builtins.property
    def http_header_name(self) -> typing.Optional[builtins.str]:
        '''Hash based on a specific HTTP header.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash#httpHeaderName
        '''
        result = self._values.get("http_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_query_parameter_name(self) -> typing.Optional[builtins.str]:
        '''Hash based on a specific HTTP query parameter.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash#httpQueryParameterName
        '''
        result = self._values.get("http_query_parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_ring_size(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash#minimumRingSize
        '''
        result = self._values.get("minimum_ring_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def use_source_ip(self) -> typing.Optional[builtins.bool]:
        '''Hash based on the source IP address.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash#useSourceIp
        '''
        result = self._values.get("use_source_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "ttl": "ttl"},
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Hash based on HTTP cookie.

        :param name: Name of the cookie.
        :param path: Path to set for the cookie.
        :param ttl: Lifetime of the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if path is not None:
            self._values["path"] = path
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path to set for the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie#path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        '''Lifetime of the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie#ttl
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting",
    jsii_struct_bases=[],
    name_mapping={
        "distribute": "distribute",
        "enabled": "enabled",
        "failover": "failover",
        "failover_priority": "failoverPriority",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting:
    def __init__(
        self,
        *,
        distribute: typing.Optional[typing.Sequence["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute"]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        failover: typing.Optional[typing.Sequence["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover"]] = None,
        failover_priority: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param distribute: Optional: only one of distribute, failover or failoverPriority can be set.
        :param enabled: enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.
        :param failover: Optional: only one of distribute, failover or failoverPriority can be set.
        :param failover_priority: failoverPriority is an ordered list of labels used to sort endpoints to do priority based load balancing.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if distribute is not None:
            self._values["distribute"] = distribute
        if enabled is not None:
            self._values["enabled"] = enabled
        if failover is not None:
            self._values["failover"] = failover
        if failover_priority is not None:
            self._values["failover_priority"] = failover_priority

    @builtins.property
    def distribute(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute"]]:
        '''Optional: only one of distribute, failover or failoverPriority can be set.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting#distribute
        '''
        result = self._values.get("distribute")
        return typing.cast(typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute"]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def failover(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover"]]:
        '''Optional: only one of distribute, failover or failoverPriority can be set.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting#failover
        '''
        result = self._values.get("failover")
        return typing.cast(typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover"]], result)

    @builtins.property
    def failover_priority(self) -> typing.Optional[typing.List[builtins.str]]:
        '''failoverPriority is an ordered list of labels used to sort endpoints to do priority based load balancing.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting#failoverPriority
        '''
        result = self._values.get("failover_priority")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        '''
        :param from_: Originating locality, '/' separated, e.g.
        :param to: Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        '''Originating locality, '/' separated, e.g.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute#from
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def to(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute#to
        '''
        result = self._values.get("to")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param from_: Originating region.
        :param to: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        '''Originating region.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover#from
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def to(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover#to
        '''
        result = self._values.get("to")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerSimple"
)
class DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerSimple(enum.Enum):
    '''
    :schema: DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerSimple
    '''

    UNSPECIFIED = "UNSPECIFIED"
    '''UNSPECIFIED.'''
    LEAST_CONN = "LEAST_CONN"
    '''LEAST_CONN.'''
    RANDOM = "RANDOM"
    '''RANDOM.'''
    PASSTHROUGH = "PASSTHROUGH"
    '''PASSTHROUGH.'''
    ROUND_ROBIN = "ROUND_ROBIN"
    '''ROUND_ROBIN.'''
    LEAST_REQUEST = "LEAST_REQUEST"
    '''LEAST_REQUEST.'''


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection",
    jsii_struct_bases=[],
    name_mapping={
        "base_ejection_time": "baseEjectionTime",
        "consecutive5_xx_errors": "consecutive5XxErrors",
        "consecutive_errors": "consecutiveErrors",
        "consecutive_gateway_errors": "consecutiveGatewayErrors",
        "consecutive_local_origin_failures": "consecutiveLocalOriginFailures",
        "interval": "interval",
        "max_ejection_percent": "maxEjectionPercent",
        "min_health_percent": "minHealthPercent",
        "split_external_local_origin_errors": "splitExternalLocalOriginErrors",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection:
    def __init__(
        self,
        *,
        base_ejection_time: typing.Optional[builtins.str] = None,
        consecutive5_xx_errors: typing.Optional[jsii.Number] = None,
        consecutive_errors: typing.Optional[jsii.Number] = None,
        consecutive_gateway_errors: typing.Optional[jsii.Number] = None,
        consecutive_local_origin_failures: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[builtins.str] = None,
        max_ejection_percent: typing.Optional[jsii.Number] = None,
        min_health_percent: typing.Optional[jsii.Number] = None,
        split_external_local_origin_errors: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param base_ejection_time: Minimum ejection duration.
        :param consecutive5_xx_errors: Number of 5xx errors before a host is ejected from the connection pool.
        :param consecutive_errors: 
        :param consecutive_gateway_errors: Number of gateway errors before a host is ejected from the connection pool.
        :param consecutive_local_origin_failures: 
        :param interval: Time interval between ejection sweep analysis.
        :param max_ejection_percent: 
        :param min_health_percent: 
        :param split_external_local_origin_errors: Determines whether to distinguish local origin failures from external errors.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if base_ejection_time is not None:
            self._values["base_ejection_time"] = base_ejection_time
        if consecutive5_xx_errors is not None:
            self._values["consecutive5_xx_errors"] = consecutive5_xx_errors
        if consecutive_errors is not None:
            self._values["consecutive_errors"] = consecutive_errors
        if consecutive_gateway_errors is not None:
            self._values["consecutive_gateway_errors"] = consecutive_gateway_errors
        if consecutive_local_origin_failures is not None:
            self._values["consecutive_local_origin_failures"] = consecutive_local_origin_failures
        if interval is not None:
            self._values["interval"] = interval
        if max_ejection_percent is not None:
            self._values["max_ejection_percent"] = max_ejection_percent
        if min_health_percent is not None:
            self._values["min_health_percent"] = min_health_percent
        if split_external_local_origin_errors is not None:
            self._values["split_external_local_origin_errors"] = split_external_local_origin_errors

    @builtins.property
    def base_ejection_time(self) -> typing.Optional[builtins.str]:
        '''Minimum ejection duration.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#baseEjectionTime
        '''
        result = self._values.get("base_ejection_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consecutive5_xx_errors(self) -> typing.Optional[jsii.Number]:
        '''Number of 5xx errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#consecutive5xxErrors
        '''
        result = self._values.get("consecutive5_xx_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consecutive_errors(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#consecutiveErrors
        '''
        result = self._values.get("consecutive_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consecutive_gateway_errors(self) -> typing.Optional[jsii.Number]:
        '''Number of gateway errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#consecutiveGatewayErrors
        '''
        result = self._values.get("consecutive_gateway_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consecutive_local_origin_failures(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#consecutiveLocalOriginFailures
        '''
        result = self._values.get("consecutive_local_origin_failures")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''Time interval between ejection sweep analysis.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#interval
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_ejection_percent(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#maxEjectionPercent
        '''
        result = self._values.get("max_ejection_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_health_percent(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#minHealthPercent
        '''
        result = self._values.get("min_health_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def split_external_local_origin_errors(self) -> typing.Optional[builtins.bool]:
        '''Determines whether to distinguish local origin failures from external errors.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection#splitExternalLocalOriginErrors
        '''
        result = self._values.get("split_external_local_origin_errors")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "load_balancer": "loadBalancer",
        "outlier_detection": "outlierDetection",
        "port": "port",
        "tls": "tls",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool"] = None,
        load_balancer: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer"] = None,
        outlier_detection: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection"] = None,
        port: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort"] = None,
        tls: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls"] = None,
    ) -> None:
        '''
        :param connection_pool: 
        :param load_balancer: Settings controlling the load balancer algorithms.
        :param outlier_detection: 
        :param port: 
        :param tls: TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings
        '''
        if isinstance(connection_pool, dict):
            connection_pool = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool(**connection_pool)
        if isinstance(load_balancer, dict):
            load_balancer = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer(**load_balancer)
        if isinstance(outlier_detection, dict):
            outlier_detection = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection(**outlier_detection)
        if isinstance(port, dict):
            port = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort(**port)
        if isinstance(tls, dict):
            tls = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if port is not None:
            self._values["port"] = port
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def connection_pool(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings#connectionPool
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool"], result)

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer"]:
        '''Settings controlling the load balancer algorithms.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings#loadBalancer
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer"], result)

    @builtins.property
    def outlier_detection(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings#outlierDetection
        '''
        result = self._values.get("outlier_detection")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection"], result)

    @builtins.property
    def port(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort"], result)

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls"]:
        '''TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings#tls
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"http": "http", "tcp": "tcp"},
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool:
    def __init__(
        self,
        *,
        http: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp"] = None,
        tcp: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp"] = None,
    ) -> None:
        '''
        :param http: HTTP connection pool settings.
        :param tcp: Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool
        '''
        if isinstance(http, dict):
            http = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp(**http)
        if isinstance(tcp, dict):
            tcp = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp(**tcp)
        self._values: typing.Dict[str, typing.Any] = {}
        if http is not None:
            self._values["http"] = http
        if tcp is not None:
            self._values["tcp"] = tcp

    @builtins.property
    def http(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp"]:
        '''HTTP connection pool settings.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool#http
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp"], result)

    @builtins.property
    def tcp(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp"]:
        '''Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool#tcp
        '''
        result = self._values.get("tcp")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp",
    jsii_struct_bases=[],
    name_mapping={
        "h2_upgrade_policy": "h2UpgradePolicy",
        "http1_max_pending_requests": "http1MaxPendingRequests",
        "http2_max_requests": "http2MaxRequests",
        "idle_timeout": "idleTimeout",
        "max_requests_per_connection": "maxRequestsPerConnection",
        "max_retries": "maxRetries",
        "use_client_protocol": "useClientProtocol",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp:
    def __init__(
        self,
        *,
        h2_upgrade_policy: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"] = None,
        http1_max_pending_requests: typing.Optional[jsii.Number] = None,
        http2_max_requests: typing.Optional[jsii.Number] = None,
        idle_timeout: typing.Optional[builtins.str] = None,
        max_requests_per_connection: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        use_client_protocol: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''HTTP connection pool settings.

        :param h2_upgrade_policy: Specify if http1.1 connection should be upgraded to http2 for the associated destination.
        :param http1_max_pending_requests: Maximum number of pending HTTP requests to a destination.
        :param http2_max_requests: Maximum number of requests to a backend.
        :param idle_timeout: The idle timeout for upstream connection pool connections.
        :param max_requests_per_connection: Maximum number of requests per connection to a backend.
        :param max_retries: 
        :param use_client_protocol: If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if h2_upgrade_policy is not None:
            self._values["h2_upgrade_policy"] = h2_upgrade_policy
        if http1_max_pending_requests is not None:
            self._values["http1_max_pending_requests"] = http1_max_pending_requests
        if http2_max_requests is not None:
            self._values["http2_max_requests"] = http2_max_requests
        if idle_timeout is not None:
            self._values["idle_timeout"] = idle_timeout
        if max_requests_per_connection is not None:
            self._values["max_requests_per_connection"] = max_requests_per_connection
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if use_client_protocol is not None:
            self._values["use_client_protocol"] = use_client_protocol

    @builtins.property
    def h2_upgrade_policy(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"]:
        '''Specify if http1.1 connection should be upgraded to http2 for the associated destination.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#h2UpgradePolicy
        '''
        result = self._values.get("h2_upgrade_policy")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"], result)

    @builtins.property
    def http1_max_pending_requests(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of pending HTTP requests to a destination.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#http1MaxPendingRequests
        '''
        result = self._values.get("http1_max_pending_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http2_max_requests(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of requests to a backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#http2MaxRequests
        '''
        result = self._values.get("http2_max_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def idle_timeout(self) -> typing.Optional[builtins.str]:
        '''The idle timeout for upstream connection pool connections.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#idleTimeout
        '''
        result = self._values.get("idle_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_requests_per_connection(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of requests per connection to a backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#maxRequestsPerConnection
        '''
        result = self._values.get("max_requests_per_connection")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#maxRetries
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def use_client_protocol(self) -> typing.Optional[builtins.bool]:
        '''If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp#useClientProtocol
        '''
        result = self._values.get("use_client_protocol")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy(
    enum.Enum,
):
    '''Specify if http1.1 connection should be upgraded to http2 for the associated destination.

    :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy
    '''

    DEFAULT = "DEFAULT"
    '''DEFAULT.'''
    DO_NOT_UPGRADE = "DO_NOT_UPGRADE"
    '''DO_NOT_UPGRADE.'''
    UPGRADE = "UPGRADE"
    '''UPGRADE.'''


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp",
    jsii_struct_bases=[],
    name_mapping={
        "connect_timeout": "connectTimeout",
        "max_connections": "maxConnections",
        "tcp_keepalive": "tcpKeepalive",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp:
    def __init__(
        self,
        *,
        connect_timeout: typing.Optional[builtins.str] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        tcp_keepalive: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive"] = None,
    ) -> None:
        '''Settings common to both HTTP and TCP upstream connections.

        :param connect_timeout: TCP connection timeout.
        :param max_connections: Maximum number of HTTP1 /TCP connections to a destination host.
        :param tcp_keepalive: If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp
        '''
        if isinstance(tcp_keepalive, dict):
            tcp_keepalive = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive(**tcp_keepalive)
        self._values: typing.Dict[str, typing.Any] = {}
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if max_connections is not None:
            self._values["max_connections"] = max_connections
        if tcp_keepalive is not None:
            self._values["tcp_keepalive"] = tcp_keepalive

    @builtins.property
    def connect_timeout(self) -> typing.Optional[builtins.str]:
        '''TCP connection timeout.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp#connectTimeout
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of HTTP1 /TCP connections to a destination host.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp#maxConnections
        '''
        result = self._values.get("max_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tcp_keepalive(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive"]:
        '''If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp#tcpKeepalive
        '''
        result = self._values.get("tcp_keepalive")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "probes": "probes", "time": "time"},
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive:
    def __init__(
        self,
        *,
        interval: typing.Optional[builtins.str] = None,
        probes: typing.Optional[jsii.Number] = None,
        time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :param interval: The time duration between keep-alive probes.
        :param probes: 
        :param time: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if interval is not None:
            self._values["interval"] = interval
        if probes is not None:
            self._values["probes"] = probes
        if time is not None:
            self._values["time"] = time

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''The time duration between keep-alive probes.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive#interval
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def probes(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive#probes
        '''
        result = self._values.get("probes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def time(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive#time
        '''
        result = self._values.get("time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "consistent_hash": "consistentHash",
        "locality_lb_setting": "localityLbSetting",
        "simple": "simple",
        "warmup_duration_secs": "warmupDurationSecs",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer:
    def __init__(
        self,
        *,
        consistent_hash: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash"] = None,
        locality_lb_setting: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting"] = None,
        simple: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerSimple"] = None,
        warmup_duration_secs: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Settings controlling the load balancer algorithms.

        :param consistent_hash: 
        :param locality_lb_setting: 
        :param simple: 
        :param warmup_duration_secs: Represents the warmup duration of Service.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer
        '''
        if isinstance(consistent_hash, dict):
            consistent_hash = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash(**consistent_hash)
        if isinstance(locality_lb_setting, dict):
            locality_lb_setting = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting(**locality_lb_setting)
        self._values: typing.Dict[str, typing.Any] = {}
        if consistent_hash is not None:
            self._values["consistent_hash"] = consistent_hash
        if locality_lb_setting is not None:
            self._values["locality_lb_setting"] = locality_lb_setting
        if simple is not None:
            self._values["simple"] = simple
        if warmup_duration_secs is not None:
            self._values["warmup_duration_secs"] = warmup_duration_secs

    @builtins.property
    def consistent_hash(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer#consistentHash
        '''
        result = self._values.get("consistent_hash")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash"], result)

    @builtins.property
    def locality_lb_setting(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer#localityLbSetting
        '''
        result = self._values.get("locality_lb_setting")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting"], result)

    @builtins.property
    def simple(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerSimple"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer#simple
        '''
        result = self._values.get("simple")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerSimple"], result)

    @builtins.property
    def warmup_duration_secs(self) -> typing.Optional[builtins.str]:
        '''Represents the warmup duration of Service.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer#warmupDurationSecs
        '''
        result = self._values.get("warmup_duration_secs")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash",
    jsii_struct_bases=[],
    name_mapping={
        "http_cookie": "httpCookie",
        "http_header_name": "httpHeaderName",
        "http_query_parameter_name": "httpQueryParameterName",
        "minimum_ring_size": "minimumRingSize",
        "use_source_ip": "useSourceIp",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash:
    def __init__(
        self,
        *,
        http_cookie: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie"] = None,
        http_header_name: typing.Optional[builtins.str] = None,
        http_query_parameter_name: typing.Optional[builtins.str] = None,
        minimum_ring_size: typing.Optional[jsii.Number] = None,
        use_source_ip: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param http_cookie: Hash based on HTTP cookie.
        :param http_header_name: Hash based on a specific HTTP header.
        :param http_query_parameter_name: Hash based on a specific HTTP query parameter.
        :param minimum_ring_size: 
        :param use_source_ip: Hash based on the source IP address.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash
        '''
        if isinstance(http_cookie, dict):
            http_cookie = DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie(**http_cookie)
        self._values: typing.Dict[str, typing.Any] = {}
        if http_cookie is not None:
            self._values["http_cookie"] = http_cookie
        if http_header_name is not None:
            self._values["http_header_name"] = http_header_name
        if http_query_parameter_name is not None:
            self._values["http_query_parameter_name"] = http_query_parameter_name
        if minimum_ring_size is not None:
            self._values["minimum_ring_size"] = minimum_ring_size
        if use_source_ip is not None:
            self._values["use_source_ip"] = use_source_ip

    @builtins.property
    def http_cookie(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie"]:
        '''Hash based on HTTP cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#httpCookie
        '''
        result = self._values.get("http_cookie")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie"], result)

    @builtins.property
    def http_header_name(self) -> typing.Optional[builtins.str]:
        '''Hash based on a specific HTTP header.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#httpHeaderName
        '''
        result = self._values.get("http_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_query_parameter_name(self) -> typing.Optional[builtins.str]:
        '''Hash based on a specific HTTP query parameter.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#httpQueryParameterName
        '''
        result = self._values.get("http_query_parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_ring_size(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#minimumRingSize
        '''
        result = self._values.get("minimum_ring_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def use_source_ip(self) -> typing.Optional[builtins.bool]:
        '''Hash based on the source IP address.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#useSourceIp
        '''
        result = self._values.get("use_source_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "ttl": "ttl"},
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Hash based on HTTP cookie.

        :param name: Name of the cookie.
        :param path: Path to set for the cookie.
        :param ttl: Lifetime of the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if path is not None:
            self._values["path"] = path
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path to set for the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie#path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        '''Lifetime of the cookie.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie#ttl
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting",
    jsii_struct_bases=[],
    name_mapping={
        "distribute": "distribute",
        "enabled": "enabled",
        "failover": "failover",
        "failover_priority": "failoverPriority",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting:
    def __init__(
        self,
        *,
        distribute: typing.Optional[typing.Sequence["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute"]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        failover: typing.Optional[typing.Sequence["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover"]] = None,
        failover_priority: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param distribute: Optional: only one of distribute, failover or failoverPriority can be set.
        :param enabled: enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.
        :param failover: Optional: only one of distribute, failover or failoverPriority can be set.
        :param failover_priority: failoverPriority is an ordered list of labels used to sort endpoints to do priority based load balancing.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if distribute is not None:
            self._values["distribute"] = distribute
        if enabled is not None:
            self._values["enabled"] = enabled
        if failover is not None:
            self._values["failover"] = failover
        if failover_priority is not None:
            self._values["failover_priority"] = failover_priority

    @builtins.property
    def distribute(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute"]]:
        '''Optional: only one of distribute, failover or failoverPriority can be set.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#distribute
        '''
        result = self._values.get("distribute")
        return typing.cast(typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute"]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def failover(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover"]]:
        '''Optional: only one of distribute, failover or failoverPriority can be set.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#failover
        '''
        result = self._values.get("failover")
        return typing.cast(typing.Optional[typing.List["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover"]], result)

    @builtins.property
    def failover_priority(self) -> typing.Optional[typing.List[builtins.str]]:
        '''failoverPriority is an ordered list of labels used to sort endpoints to do priority based load balancing.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#failoverPriority
        '''
        result = self._values.get("failover_priority")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        '''
        :param from_: Originating locality, '/' separated, e.g.
        :param to: Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        '''Originating locality, '/' separated, e.g.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute#from
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def to(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute#to
        '''
        result = self._values.get("to")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param from_: Originating region.
        :param to: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        '''Originating region.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover#from
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def to(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover#to
        '''
        result = self._values.get("to")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerSimple"
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerSimple(
    enum.Enum,
):
    '''
    :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerSimple
    '''

    UNSPECIFIED = "UNSPECIFIED"
    '''UNSPECIFIED.'''
    LEAST_CONN = "LEAST_CONN"
    '''LEAST_CONN.'''
    RANDOM = "RANDOM"
    '''RANDOM.'''
    PASSTHROUGH = "PASSTHROUGH"
    '''PASSTHROUGH.'''
    ROUND_ROBIN = "ROUND_ROBIN"
    '''ROUND_ROBIN.'''
    LEAST_REQUEST = "LEAST_REQUEST"
    '''LEAST_REQUEST.'''


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection",
    jsii_struct_bases=[],
    name_mapping={
        "base_ejection_time": "baseEjectionTime",
        "consecutive5_xx_errors": "consecutive5XxErrors",
        "consecutive_errors": "consecutiveErrors",
        "consecutive_gateway_errors": "consecutiveGatewayErrors",
        "consecutive_local_origin_failures": "consecutiveLocalOriginFailures",
        "interval": "interval",
        "max_ejection_percent": "maxEjectionPercent",
        "min_health_percent": "minHealthPercent",
        "split_external_local_origin_errors": "splitExternalLocalOriginErrors",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection:
    def __init__(
        self,
        *,
        base_ejection_time: typing.Optional[builtins.str] = None,
        consecutive5_xx_errors: typing.Optional[jsii.Number] = None,
        consecutive_errors: typing.Optional[jsii.Number] = None,
        consecutive_gateway_errors: typing.Optional[jsii.Number] = None,
        consecutive_local_origin_failures: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[builtins.str] = None,
        max_ejection_percent: typing.Optional[jsii.Number] = None,
        min_health_percent: typing.Optional[jsii.Number] = None,
        split_external_local_origin_errors: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param base_ejection_time: Minimum ejection duration.
        :param consecutive5_xx_errors: Number of 5xx errors before a host is ejected from the connection pool.
        :param consecutive_errors: 
        :param consecutive_gateway_errors: Number of gateway errors before a host is ejected from the connection pool.
        :param consecutive_local_origin_failures: 
        :param interval: Time interval between ejection sweep analysis.
        :param max_ejection_percent: 
        :param min_health_percent: 
        :param split_external_local_origin_errors: Determines whether to distinguish local origin failures from external errors.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if base_ejection_time is not None:
            self._values["base_ejection_time"] = base_ejection_time
        if consecutive5_xx_errors is not None:
            self._values["consecutive5_xx_errors"] = consecutive5_xx_errors
        if consecutive_errors is not None:
            self._values["consecutive_errors"] = consecutive_errors
        if consecutive_gateway_errors is not None:
            self._values["consecutive_gateway_errors"] = consecutive_gateway_errors
        if consecutive_local_origin_failures is not None:
            self._values["consecutive_local_origin_failures"] = consecutive_local_origin_failures
        if interval is not None:
            self._values["interval"] = interval
        if max_ejection_percent is not None:
            self._values["max_ejection_percent"] = max_ejection_percent
        if min_health_percent is not None:
            self._values["min_health_percent"] = min_health_percent
        if split_external_local_origin_errors is not None:
            self._values["split_external_local_origin_errors"] = split_external_local_origin_errors

    @builtins.property
    def base_ejection_time(self) -> typing.Optional[builtins.str]:
        '''Minimum ejection duration.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#baseEjectionTime
        '''
        result = self._values.get("base_ejection_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consecutive5_xx_errors(self) -> typing.Optional[jsii.Number]:
        '''Number of 5xx errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#consecutive5xxErrors
        '''
        result = self._values.get("consecutive5_xx_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consecutive_errors(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#consecutiveErrors
        '''
        result = self._values.get("consecutive_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consecutive_gateway_errors(self) -> typing.Optional[jsii.Number]:
        '''Number of gateway errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#consecutiveGatewayErrors
        '''
        result = self._values.get("consecutive_gateway_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consecutive_local_origin_failures(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#consecutiveLocalOriginFailures
        '''
        result = self._values.get("consecutive_local_origin_failures")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''Time interval between ejection sweep analysis.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#interval
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_ejection_percent(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#maxEjectionPercent
        '''
        result = self._values.get("max_ejection_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_health_percent(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#minHealthPercent
        '''
        result = self._values.get("min_health_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def split_external_local_origin_errors(self) -> typing.Optional[builtins.bool]:
        '''Determines whether to distinguish local origin failures from external errors.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection#splitExternalLocalOriginErrors
        '''
        result = self._values.get("split_external_local_origin_errors")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param number: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort#number
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificates": "caCertificates",
        "client_certificate": "clientCertificate",
        "credential_name": "credentialName",
        "insecure_skip_verify": "insecureSkipVerify",
        "mode": "mode",
        "private_key": "privateKey",
        "sni": "sni",
        "subject_alt_names": "subjectAltNames",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls:
    def __init__(
        self,
        *,
        ca_certificates: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        credential_name: typing.Optional[builtins.str] = None,
        insecure_skip_verify: typing.Optional[builtins.bool] = None,
        mode: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTlsMode"] = None,
        private_key: typing.Optional[builtins.str] = None,
        sni: typing.Optional[builtins.str] = None,
        subject_alt_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''TLS related settings for connections to the upstream service.

        :param ca_certificates: 
        :param client_certificate: REQUIRED if mode is ``MUTUAL``.
        :param credential_name: 
        :param insecure_skip_verify: 
        :param mode: 
        :param private_key: REQUIRED if mode is ``MUTUAL``.
        :param sni: SNI string to present to the server during TLS handshake.
        :param subject_alt_names: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ca_certificates is not None:
            self._values["ca_certificates"] = ca_certificates
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if credential_name is not None:
            self._values["credential_name"] = credential_name
        if insecure_skip_verify is not None:
            self._values["insecure_skip_verify"] = insecure_skip_verify
        if mode is not None:
            self._values["mode"] = mode
        if private_key is not None:
            self._values["private_key"] = private_key
        if sni is not None:
            self._values["sni"] = sni
        if subject_alt_names is not None:
            self._values["subject_alt_names"] = subject_alt_names

    @builtins.property
    def ca_certificates(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#caCertificates
        '''
        result = self._values.get("ca_certificates")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#clientCertificate
        '''
        result = self._values.get("client_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credential_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#credentialName
        '''
        result = self._values.get("credential_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_skip_verify(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#insecureSkipVerify
        '''
        result = self._values.get("insecure_skip_verify")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def mode(
        self,
    ) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTlsMode"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTlsMode"], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#privateKey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sni(self) -> typing.Optional[builtins.str]:
        '''SNI string to present to the server during TLS handshake.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#sni
        '''
        result = self._values.get("sni")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_alt_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls#subjectAltNames
        '''
        result = self._values.get("subject_alt_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTlsMode"
)
class DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTlsMode(enum.Enum):
    '''
    :schema: DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTlsMode
    '''

    DISABLE = "DISABLE"
    '''DISABLE.'''
    SIMPLE = "SIMPLE"
    '''SIMPLE.'''
    MUTUAL = "MUTUAL"
    '''MUTUAL.'''
    ISTIO_MUTUAL = "ISTIO_MUTUAL"
    '''ISTIO_MUTUAL.'''


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyTls",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificates": "caCertificates",
        "client_certificate": "clientCertificate",
        "credential_name": "credentialName",
        "insecure_skip_verify": "insecureSkipVerify",
        "mode": "mode",
        "private_key": "privateKey",
        "sni": "sni",
        "subject_alt_names": "subjectAltNames",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyTls:
    def __init__(
        self,
        *,
        ca_certificates: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        credential_name: typing.Optional[builtins.str] = None,
        insecure_skip_verify: typing.Optional[builtins.bool] = None,
        mode: typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyTlsMode"] = None,
        private_key: typing.Optional[builtins.str] = None,
        sni: typing.Optional[builtins.str] = None,
        subject_alt_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''TLS related settings for connections to the upstream service.

        :param ca_certificates: 
        :param client_certificate: REQUIRED if mode is ``MUTUAL``.
        :param credential_name: 
        :param insecure_skip_verify: 
        :param mode: 
        :param private_key: REQUIRED if mode is ``MUTUAL``.
        :param sni: SNI string to present to the server during TLS handshake.
        :param subject_alt_names: 

        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ca_certificates is not None:
            self._values["ca_certificates"] = ca_certificates
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if credential_name is not None:
            self._values["credential_name"] = credential_name
        if insecure_skip_verify is not None:
            self._values["insecure_skip_verify"] = insecure_skip_verify
        if mode is not None:
            self._values["mode"] = mode
        if private_key is not None:
            self._values["private_key"] = private_key
        if sni is not None:
            self._values["sni"] = sni
        if subject_alt_names is not None:
            self._values["subject_alt_names"] = subject_alt_names

    @builtins.property
    def ca_certificates(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#caCertificates
        '''
        result = self._values.get("ca_certificates")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#clientCertificate
        '''
        result = self._values.get("client_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credential_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#credentialName
        '''
        result = self._values.get("credential_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_skip_verify(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#insecureSkipVerify
        '''
        result = self._values.get("insecure_skip_verify")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def mode(self) -> typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyTlsMode"]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["DestinationRuleSpecSubsetsTrafficPolicyTlsMode"], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#privateKey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sni(self) -> typing.Optional[builtins.str]:
        '''SNI string to present to the server during TLS handshake.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#sni
        '''
        result = self._values.get("sni")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_alt_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: DestinationRuleSpecSubsetsTrafficPolicyTls#subjectAltNames
        '''
        result = self._values.get("subject_alt_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyTlsMode"
)
class DestinationRuleSpecSubsetsTrafficPolicyTlsMode(enum.Enum):
    '''
    :schema: DestinationRuleSpecSubsetsTrafficPolicyTlsMode
    '''

    DISABLE = "DISABLE"
    '''DISABLE.'''
    SIMPLE = "SIMPLE"
    '''SIMPLE.'''
    MUTUAL = "MUTUAL"
    '''MUTUAL.'''
    ISTIO_MUTUAL = "ISTIO_MUTUAL"
    '''ISTIO_MUTUAL.'''


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecSubsetsTrafficPolicyTunnel",
    jsii_struct_bases=[],
    name_mapping={
        "protocol": "protocol",
        "target_host": "targetHost",
        "target_port": "targetPort",
    },
)
class DestinationRuleSpecSubsetsTrafficPolicyTunnel:
    def __init__(
        self,
        *,
        protocol: typing.Optional[builtins.str] = None,
        target_host: typing.Optional[builtins.str] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param protocol: Specifies which protocol to use for tunneling the downstream connection.
        :param target_host: Specifies a host to which the downstream connection is tunneled.
        :param target_port: Specifies a port to which the downstream connection is tunneled.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyTunnel
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_host is not None:
            self._values["target_host"] = target_host
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Specifies which protocol to use for tunneling the downstream connection.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyTunnel#protocol
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_host(self) -> typing.Optional[builtins.str]:
        '''Specifies a host to which the downstream connection is tunneled.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyTunnel#targetHost
        '''
        result = self._values.get("target_host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''Specifies a port to which the downstream connection is tunneled.

        :schema: DestinationRuleSpecSubsetsTrafficPolicyTunnel#targetPort
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecSubsetsTrafficPolicyTunnel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "load_balancer": "loadBalancer",
        "outlier_detection": "outlierDetection",
        "port_level_settings": "portLevelSettings",
        "tls": "tls",
        "tunnel": "tunnel",
    },
)
class DestinationRuleSpecTrafficPolicy:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPool"] = None,
        load_balancer: typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancer"] = None,
        outlier_detection: typing.Optional["DestinationRuleSpecTrafficPolicyOutlierDetection"] = None,
        port_level_settings: typing.Optional[typing.Sequence["DestinationRuleSpecTrafficPolicyPortLevelSettings"]] = None,
        tls: typing.Optional["DestinationRuleSpecTrafficPolicyTls"] = None,
        tunnel: typing.Optional["DestinationRuleSpecTrafficPolicyTunnel"] = None,
    ) -> None:
        '''
        :param connection_pool: 
        :param load_balancer: Settings controlling the load balancer algorithms.
        :param outlier_detection: 
        :param port_level_settings: Traffic policies specific to individual ports.
        :param tls: TLS related settings for connections to the upstream service.
        :param tunnel: 

        :schema: DestinationRuleSpecTrafficPolicy
        '''
        if isinstance(connection_pool, dict):
            connection_pool = DestinationRuleSpecTrafficPolicyConnectionPool(**connection_pool)
        if isinstance(load_balancer, dict):
            load_balancer = DestinationRuleSpecTrafficPolicyLoadBalancer(**load_balancer)
        if isinstance(outlier_detection, dict):
            outlier_detection = DestinationRuleSpecTrafficPolicyOutlierDetection(**outlier_detection)
        if isinstance(tls, dict):
            tls = DestinationRuleSpecTrafficPolicyTls(**tls)
        if isinstance(tunnel, dict):
            tunnel = DestinationRuleSpecTrafficPolicyTunnel(**tunnel)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if port_level_settings is not None:
            self._values["port_level_settings"] = port_level_settings
        if tls is not None:
            self._values["tls"] = tls
        if tunnel is not None:
            self._values["tunnel"] = tunnel

    @builtins.property
    def connection_pool(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPool"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicy#connectionPool
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPool"], result)

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancer"]:
        '''Settings controlling the load balancer algorithms.

        :schema: DestinationRuleSpecTrafficPolicy#loadBalancer
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancer"], result)

    @builtins.property
    def outlier_detection(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyOutlierDetection"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicy#outlierDetection
        '''
        result = self._values.get("outlier_detection")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyOutlierDetection"], result)

    @builtins.property
    def port_level_settings(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyPortLevelSettings"]]:
        '''Traffic policies specific to individual ports.

        :schema: DestinationRuleSpecTrafficPolicy#portLevelSettings
        '''
        result = self._values.get("port_level_settings")
        return typing.cast(typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyPortLevelSettings"]], result)

    @builtins.property
    def tls(self) -> typing.Optional["DestinationRuleSpecTrafficPolicyTls"]:
        '''TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecTrafficPolicy#tls
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyTls"], result)

    @builtins.property
    def tunnel(self) -> typing.Optional["DestinationRuleSpecTrafficPolicyTunnel"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicy#tunnel
        '''
        result = self._values.get("tunnel")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyTunnel"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"http": "http", "tcp": "tcp"},
)
class DestinationRuleSpecTrafficPolicyConnectionPool:
    def __init__(
        self,
        *,
        http: typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolHttp"] = None,
        tcp: typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolTcp"] = None,
    ) -> None:
        '''
        :param http: HTTP connection pool settings.
        :param tcp: Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPool
        '''
        if isinstance(http, dict):
            http = DestinationRuleSpecTrafficPolicyConnectionPoolHttp(**http)
        if isinstance(tcp, dict):
            tcp = DestinationRuleSpecTrafficPolicyConnectionPoolTcp(**tcp)
        self._values: typing.Dict[str, typing.Any] = {}
        if http is not None:
            self._values["http"] = http
        if tcp is not None:
            self._values["tcp"] = tcp

    @builtins.property
    def http(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolHttp"]:
        '''HTTP connection pool settings.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPool#http
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolHttp"], result)

    @builtins.property
    def tcp(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolTcp"]:
        '''Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPool#tcp
        '''
        result = self._values.get("tcp")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolTcp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyConnectionPoolHttp",
    jsii_struct_bases=[],
    name_mapping={
        "h2_upgrade_policy": "h2UpgradePolicy",
        "http1_max_pending_requests": "http1MaxPendingRequests",
        "http2_max_requests": "http2MaxRequests",
        "idle_timeout": "idleTimeout",
        "max_requests_per_connection": "maxRequestsPerConnection",
        "max_retries": "maxRetries",
        "use_client_protocol": "useClientProtocol",
    },
)
class DestinationRuleSpecTrafficPolicyConnectionPoolHttp:
    def __init__(
        self,
        *,
        h2_upgrade_policy: typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolHttpH2UpgradePolicy"] = None,
        http1_max_pending_requests: typing.Optional[jsii.Number] = None,
        http2_max_requests: typing.Optional[jsii.Number] = None,
        idle_timeout: typing.Optional[builtins.str] = None,
        max_requests_per_connection: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        use_client_protocol: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''HTTP connection pool settings.

        :param h2_upgrade_policy: Specify if http1.1 connection should be upgraded to http2 for the associated destination.
        :param http1_max_pending_requests: Maximum number of pending HTTP requests to a destination.
        :param http2_max_requests: Maximum number of requests to a backend.
        :param idle_timeout: The idle timeout for upstream connection pool connections.
        :param max_requests_per_connection: Maximum number of requests per connection to a backend.
        :param max_retries: 
        :param use_client_protocol: If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if h2_upgrade_policy is not None:
            self._values["h2_upgrade_policy"] = h2_upgrade_policy
        if http1_max_pending_requests is not None:
            self._values["http1_max_pending_requests"] = http1_max_pending_requests
        if http2_max_requests is not None:
            self._values["http2_max_requests"] = http2_max_requests
        if idle_timeout is not None:
            self._values["idle_timeout"] = idle_timeout
        if max_requests_per_connection is not None:
            self._values["max_requests_per_connection"] = max_requests_per_connection
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if use_client_protocol is not None:
            self._values["use_client_protocol"] = use_client_protocol

    @builtins.property
    def h2_upgrade_policy(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolHttpH2UpgradePolicy"]:
        '''Specify if http1.1 connection should be upgraded to http2 for the associated destination.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#h2UpgradePolicy
        '''
        result = self._values.get("h2_upgrade_policy")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolHttpH2UpgradePolicy"], result)

    @builtins.property
    def http1_max_pending_requests(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of pending HTTP requests to a destination.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#http1MaxPendingRequests
        '''
        result = self._values.get("http1_max_pending_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http2_max_requests(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of requests to a backend.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#http2MaxRequests
        '''
        result = self._values.get("http2_max_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def idle_timeout(self) -> typing.Optional[builtins.str]:
        '''The idle timeout for upstream connection pool connections.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#idleTimeout
        '''
        result = self._values.get("idle_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_requests_per_connection(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of requests per connection to a backend.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#maxRequestsPerConnection
        '''
        result = self._values.get("max_requests_per_connection")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#maxRetries
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def use_client_protocol(self) -> typing.Optional[builtins.bool]:
        '''If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttp#useClientProtocol
        '''
        result = self._values.get("use_client_protocol")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyConnectionPoolHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyConnectionPoolHttpH2UpgradePolicy"
)
class DestinationRuleSpecTrafficPolicyConnectionPoolHttpH2UpgradePolicy(enum.Enum):
    '''Specify if http1.1 connection should be upgraded to http2 for the associated destination.

    :schema: DestinationRuleSpecTrafficPolicyConnectionPoolHttpH2UpgradePolicy
    '''

    DEFAULT = "DEFAULT"
    '''DEFAULT.'''
    DO_NOT_UPGRADE = "DO_NOT_UPGRADE"
    '''DO_NOT_UPGRADE.'''
    UPGRADE = "UPGRADE"
    '''UPGRADE.'''


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyConnectionPoolTcp",
    jsii_struct_bases=[],
    name_mapping={
        "connect_timeout": "connectTimeout",
        "max_connections": "maxConnections",
        "tcp_keepalive": "tcpKeepalive",
    },
)
class DestinationRuleSpecTrafficPolicyConnectionPoolTcp:
    def __init__(
        self,
        *,
        connect_timeout: typing.Optional[builtins.str] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        tcp_keepalive: typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive"] = None,
    ) -> None:
        '''Settings common to both HTTP and TCP upstream connections.

        :param connect_timeout: TCP connection timeout.
        :param max_connections: Maximum number of HTTP1 /TCP connections to a destination host.
        :param tcp_keepalive: If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcp
        '''
        if isinstance(tcp_keepalive, dict):
            tcp_keepalive = DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive(**tcp_keepalive)
        self._values: typing.Dict[str, typing.Any] = {}
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if max_connections is not None:
            self._values["max_connections"] = max_connections
        if tcp_keepalive is not None:
            self._values["tcp_keepalive"] = tcp_keepalive

    @builtins.property
    def connect_timeout(self) -> typing.Optional[builtins.str]:
        '''TCP connection timeout.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcp#connectTimeout
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of HTTP1 /TCP connections to a destination host.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcp#maxConnections
        '''
        result = self._values.get("max_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tcp_keepalive(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive"]:
        '''If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcp#tcpKeepalive
        '''
        result = self._values.get("tcp_keepalive")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyConnectionPoolTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "probes": "probes", "time": "time"},
)
class DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive:
    def __init__(
        self,
        *,
        interval: typing.Optional[builtins.str] = None,
        probes: typing.Optional[jsii.Number] = None,
        time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :param interval: The time duration between keep-alive probes.
        :param probes: 
        :param time: 

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if interval is not None:
            self._values["interval"] = interval
        if probes is not None:
            self._values["probes"] = probes
        if time is not None:
            self._values["time"] = time

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''The time duration between keep-alive probes.

        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive#interval
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def probes(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive#probes
        '''
        result = self._values.get("probes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def time(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive#time
        '''
        result = self._values.get("time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "consistent_hash": "consistentHash",
        "locality_lb_setting": "localityLbSetting",
        "simple": "simple",
        "warmup_duration_secs": "warmupDurationSecs",
    },
)
class DestinationRuleSpecTrafficPolicyLoadBalancer:
    def __init__(
        self,
        *,
        consistent_hash: typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash"] = None,
        locality_lb_setting: typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting"] = None,
        simple: typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerSimple"] = None,
        warmup_duration_secs: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Settings controlling the load balancer algorithms.

        :param consistent_hash: 
        :param locality_lb_setting: 
        :param simple: 
        :param warmup_duration_secs: Represents the warmup duration of Service.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancer
        '''
        if isinstance(consistent_hash, dict):
            consistent_hash = DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash(**consistent_hash)
        if isinstance(locality_lb_setting, dict):
            locality_lb_setting = DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting(**locality_lb_setting)
        self._values: typing.Dict[str, typing.Any] = {}
        if consistent_hash is not None:
            self._values["consistent_hash"] = consistent_hash
        if locality_lb_setting is not None:
            self._values["locality_lb_setting"] = locality_lb_setting
        if simple is not None:
            self._values["simple"] = simple
        if warmup_duration_secs is not None:
            self._values["warmup_duration_secs"] = warmup_duration_secs

    @builtins.property
    def consistent_hash(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyLoadBalancer#consistentHash
        '''
        result = self._values.get("consistent_hash")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash"], result)

    @builtins.property
    def locality_lb_setting(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyLoadBalancer#localityLbSetting
        '''
        result = self._values.get("locality_lb_setting")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting"], result)

    @builtins.property
    def simple(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerSimple"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyLoadBalancer#simple
        '''
        result = self._values.get("simple")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerSimple"], result)

    @builtins.property
    def warmup_duration_secs(self) -> typing.Optional[builtins.str]:
        '''Represents the warmup duration of Service.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancer#warmupDurationSecs
        '''
        result = self._values.get("warmup_duration_secs")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash",
    jsii_struct_bases=[],
    name_mapping={
        "http_cookie": "httpCookie",
        "http_header_name": "httpHeaderName",
        "http_query_parameter_name": "httpQueryParameterName",
        "minimum_ring_size": "minimumRingSize",
        "use_source_ip": "useSourceIp",
    },
)
class DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash:
    def __init__(
        self,
        *,
        http_cookie: typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie"] = None,
        http_header_name: typing.Optional[builtins.str] = None,
        http_query_parameter_name: typing.Optional[builtins.str] = None,
        minimum_ring_size: typing.Optional[jsii.Number] = None,
        use_source_ip: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param http_cookie: Hash based on HTTP cookie.
        :param http_header_name: Hash based on a specific HTTP header.
        :param http_query_parameter_name: Hash based on a specific HTTP query parameter.
        :param minimum_ring_size: 
        :param use_source_ip: Hash based on the source IP address.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash
        '''
        if isinstance(http_cookie, dict):
            http_cookie = DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie(**http_cookie)
        self._values: typing.Dict[str, typing.Any] = {}
        if http_cookie is not None:
            self._values["http_cookie"] = http_cookie
        if http_header_name is not None:
            self._values["http_header_name"] = http_header_name
        if http_query_parameter_name is not None:
            self._values["http_query_parameter_name"] = http_query_parameter_name
        if minimum_ring_size is not None:
            self._values["minimum_ring_size"] = minimum_ring_size
        if use_source_ip is not None:
            self._values["use_source_ip"] = use_source_ip

    @builtins.property
    def http_cookie(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie"]:
        '''Hash based on HTTP cookie.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash#httpCookie
        '''
        result = self._values.get("http_cookie")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie"], result)

    @builtins.property
    def http_header_name(self) -> typing.Optional[builtins.str]:
        '''Hash based on a specific HTTP header.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash#httpHeaderName
        '''
        result = self._values.get("http_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_query_parameter_name(self) -> typing.Optional[builtins.str]:
        '''Hash based on a specific HTTP query parameter.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash#httpQueryParameterName
        '''
        result = self._values.get("http_query_parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_ring_size(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash#minimumRingSize
        '''
        result = self._values.get("minimum_ring_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def use_source_ip(self) -> typing.Optional[builtins.bool]:
        '''Hash based on the source IP address.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash#useSourceIp
        '''
        result = self._values.get("use_source_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "ttl": "ttl"},
)
class DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Hash based on HTTP cookie.

        :param name: Name of the cookie.
        :param path: Path to set for the cookie.
        :param ttl: Lifetime of the cookie.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if path is not None:
            self._values["path"] = path
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the cookie.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path to set for the cookie.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie#path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        '''Lifetime of the cookie.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie#ttl
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting",
    jsii_struct_bases=[],
    name_mapping={
        "distribute": "distribute",
        "enabled": "enabled",
        "failover": "failover",
        "failover_priority": "failoverPriority",
    },
)
class DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting:
    def __init__(
        self,
        *,
        distribute: typing.Optional[typing.Sequence["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute"]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        failover: typing.Optional[typing.Sequence["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover"]] = None,
        failover_priority: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param distribute: Optional: only one of distribute, failover or failoverPriority can be set.
        :param enabled: enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.
        :param failover: Optional: only one of distribute, failover or failoverPriority can be set.
        :param failover_priority: failoverPriority is an ordered list of labels used to sort endpoints to do priority based load balancing.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if distribute is not None:
            self._values["distribute"] = distribute
        if enabled is not None:
            self._values["enabled"] = enabled
        if failover is not None:
            self._values["failover"] = failover
        if failover_priority is not None:
            self._values["failover_priority"] = failover_priority

    @builtins.property
    def distribute(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute"]]:
        '''Optional: only one of distribute, failover or failoverPriority can be set.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting#distribute
        '''
        result = self._values.get("distribute")
        return typing.cast(typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute"]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def failover(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover"]]:
        '''Optional: only one of distribute, failover or failoverPriority can be set.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting#failover
        '''
        result = self._values.get("failover")
        return typing.cast(typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover"]], result)

    @builtins.property
    def failover_priority(self) -> typing.Optional[typing.List[builtins.str]]:
        '''failoverPriority is an ordered list of labels used to sort endpoints to do priority based load balancing.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting#failoverPriority
        '''
        result = self._values.get("failover_priority")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        '''
        :param from_: Originating locality, '/' separated, e.g.
        :param to: Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        '''Originating locality, '/' separated, e.g.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute#from
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def to(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute#to
        '''
        result = self._values.get("to")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param from_: Originating region.
        :param to: 

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        '''Originating region.

        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover#from
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def to(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover#to
        '''
        result = self._values.get("to")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyLoadBalancerSimple"
)
class DestinationRuleSpecTrafficPolicyLoadBalancerSimple(enum.Enum):
    '''
    :schema: DestinationRuleSpecTrafficPolicyLoadBalancerSimple
    '''

    UNSPECIFIED = "UNSPECIFIED"
    '''UNSPECIFIED.'''
    LEAST_CONN = "LEAST_CONN"
    '''LEAST_CONN.'''
    RANDOM = "RANDOM"
    '''RANDOM.'''
    PASSTHROUGH = "PASSTHROUGH"
    '''PASSTHROUGH.'''
    ROUND_ROBIN = "ROUND_ROBIN"
    '''ROUND_ROBIN.'''
    LEAST_REQUEST = "LEAST_REQUEST"
    '''LEAST_REQUEST.'''


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyOutlierDetection",
    jsii_struct_bases=[],
    name_mapping={
        "base_ejection_time": "baseEjectionTime",
        "consecutive5_xx_errors": "consecutive5XxErrors",
        "consecutive_errors": "consecutiveErrors",
        "consecutive_gateway_errors": "consecutiveGatewayErrors",
        "consecutive_local_origin_failures": "consecutiveLocalOriginFailures",
        "interval": "interval",
        "max_ejection_percent": "maxEjectionPercent",
        "min_health_percent": "minHealthPercent",
        "split_external_local_origin_errors": "splitExternalLocalOriginErrors",
    },
)
class DestinationRuleSpecTrafficPolicyOutlierDetection:
    def __init__(
        self,
        *,
        base_ejection_time: typing.Optional[builtins.str] = None,
        consecutive5_xx_errors: typing.Optional[jsii.Number] = None,
        consecutive_errors: typing.Optional[jsii.Number] = None,
        consecutive_gateway_errors: typing.Optional[jsii.Number] = None,
        consecutive_local_origin_failures: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[builtins.str] = None,
        max_ejection_percent: typing.Optional[jsii.Number] = None,
        min_health_percent: typing.Optional[jsii.Number] = None,
        split_external_local_origin_errors: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param base_ejection_time: Minimum ejection duration.
        :param consecutive5_xx_errors: Number of 5xx errors before a host is ejected from the connection pool.
        :param consecutive_errors: 
        :param consecutive_gateway_errors: Number of gateway errors before a host is ejected from the connection pool.
        :param consecutive_local_origin_failures: 
        :param interval: Time interval between ejection sweep analysis.
        :param max_ejection_percent: 
        :param min_health_percent: 
        :param split_external_local_origin_errors: Determines whether to distinguish local origin failures from external errors.

        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if base_ejection_time is not None:
            self._values["base_ejection_time"] = base_ejection_time
        if consecutive5_xx_errors is not None:
            self._values["consecutive5_xx_errors"] = consecutive5_xx_errors
        if consecutive_errors is not None:
            self._values["consecutive_errors"] = consecutive_errors
        if consecutive_gateway_errors is not None:
            self._values["consecutive_gateway_errors"] = consecutive_gateway_errors
        if consecutive_local_origin_failures is not None:
            self._values["consecutive_local_origin_failures"] = consecutive_local_origin_failures
        if interval is not None:
            self._values["interval"] = interval
        if max_ejection_percent is not None:
            self._values["max_ejection_percent"] = max_ejection_percent
        if min_health_percent is not None:
            self._values["min_health_percent"] = min_health_percent
        if split_external_local_origin_errors is not None:
            self._values["split_external_local_origin_errors"] = split_external_local_origin_errors

    @builtins.property
    def base_ejection_time(self) -> typing.Optional[builtins.str]:
        '''Minimum ejection duration.

        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#baseEjectionTime
        '''
        result = self._values.get("base_ejection_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consecutive5_xx_errors(self) -> typing.Optional[jsii.Number]:
        '''Number of 5xx errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#consecutive5xxErrors
        '''
        result = self._values.get("consecutive5_xx_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consecutive_errors(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#consecutiveErrors
        '''
        result = self._values.get("consecutive_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consecutive_gateway_errors(self) -> typing.Optional[jsii.Number]:
        '''Number of gateway errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#consecutiveGatewayErrors
        '''
        result = self._values.get("consecutive_gateway_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consecutive_local_origin_failures(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#consecutiveLocalOriginFailures
        '''
        result = self._values.get("consecutive_local_origin_failures")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''Time interval between ejection sweep analysis.

        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#interval
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_ejection_percent(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#maxEjectionPercent
        '''
        result = self._values.get("max_ejection_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_health_percent(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#minHealthPercent
        '''
        result = self._values.get("min_health_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def split_external_local_origin_errors(self) -> typing.Optional[builtins.bool]:
        '''Determines whether to distinguish local origin failures from external errors.

        :schema: DestinationRuleSpecTrafficPolicyOutlierDetection#splitExternalLocalOriginErrors
        '''
        result = self._values.get("split_external_local_origin_errors")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyOutlierDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettings",
    jsii_struct_bases=[],
    name_mapping={
        "connection_pool": "connectionPool",
        "load_balancer": "loadBalancer",
        "outlier_detection": "outlierDetection",
        "port": "port",
        "tls": "tls",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettings:
    def __init__(
        self,
        *,
        connection_pool: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool"] = None,
        load_balancer: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer"] = None,
        outlier_detection: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection"] = None,
        port: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsPort"] = None,
        tls: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsTls"] = None,
    ) -> None:
        '''
        :param connection_pool: 
        :param load_balancer: Settings controlling the load balancer algorithms.
        :param outlier_detection: 
        :param port: 
        :param tls: TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettings
        '''
        if isinstance(connection_pool, dict):
            connection_pool = DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool(**connection_pool)
        if isinstance(load_balancer, dict):
            load_balancer = DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer(**load_balancer)
        if isinstance(outlier_detection, dict):
            outlier_detection = DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection(**outlier_detection)
        if isinstance(port, dict):
            port = DestinationRuleSpecTrafficPolicyPortLevelSettingsPort(**port)
        if isinstance(tls, dict):
            tls = DestinationRuleSpecTrafficPolicyPortLevelSettingsTls(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if port is not None:
            self._values["port"] = port
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def connection_pool(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettings#connectionPool
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool"], result)

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer"]:
        '''Settings controlling the load balancer algorithms.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettings#loadBalancer
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer"], result)

    @builtins.property
    def outlier_detection(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettings#outlierDetection
        '''
        result = self._values.get("outlier_detection")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection"], result)

    @builtins.property
    def port(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsPort"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettings#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsPort"], result)

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsTls"]:
        '''TLS related settings for connections to the upstream service.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettings#tls
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"http": "http", "tcp": "tcp"},
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool:
    def __init__(
        self,
        *,
        http: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp"] = None,
        tcp: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp"] = None,
    ) -> None:
        '''
        :param http: HTTP connection pool settings.
        :param tcp: Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool
        '''
        if isinstance(http, dict):
            http = DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp(**http)
        if isinstance(tcp, dict):
            tcp = DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp(**tcp)
        self._values: typing.Dict[str, typing.Any] = {}
        if http is not None:
            self._values["http"] = http
        if tcp is not None:
            self._values["tcp"] = tcp

    @builtins.property
    def http(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp"]:
        '''HTTP connection pool settings.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool#http
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp"], result)

    @builtins.property
    def tcp(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp"]:
        '''Settings common to both HTTP and TCP upstream connections.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool#tcp
        '''
        result = self._values.get("tcp")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp",
    jsii_struct_bases=[],
    name_mapping={
        "h2_upgrade_policy": "h2UpgradePolicy",
        "http1_max_pending_requests": "http1MaxPendingRequests",
        "http2_max_requests": "http2MaxRequests",
        "idle_timeout": "idleTimeout",
        "max_requests_per_connection": "maxRequestsPerConnection",
        "max_retries": "maxRetries",
        "use_client_protocol": "useClientProtocol",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp:
    def __init__(
        self,
        *,
        h2_upgrade_policy: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"] = None,
        http1_max_pending_requests: typing.Optional[jsii.Number] = None,
        http2_max_requests: typing.Optional[jsii.Number] = None,
        idle_timeout: typing.Optional[builtins.str] = None,
        max_requests_per_connection: typing.Optional[jsii.Number] = None,
        max_retries: typing.Optional[jsii.Number] = None,
        use_client_protocol: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''HTTP connection pool settings.

        :param h2_upgrade_policy: Specify if http1.1 connection should be upgraded to http2 for the associated destination.
        :param http1_max_pending_requests: Maximum number of pending HTTP requests to a destination.
        :param http2_max_requests: Maximum number of requests to a backend.
        :param idle_timeout: The idle timeout for upstream connection pool connections.
        :param max_requests_per_connection: Maximum number of requests per connection to a backend.
        :param max_retries: 
        :param use_client_protocol: If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if h2_upgrade_policy is not None:
            self._values["h2_upgrade_policy"] = h2_upgrade_policy
        if http1_max_pending_requests is not None:
            self._values["http1_max_pending_requests"] = http1_max_pending_requests
        if http2_max_requests is not None:
            self._values["http2_max_requests"] = http2_max_requests
        if idle_timeout is not None:
            self._values["idle_timeout"] = idle_timeout
        if max_requests_per_connection is not None:
            self._values["max_requests_per_connection"] = max_requests_per_connection
        if max_retries is not None:
            self._values["max_retries"] = max_retries
        if use_client_protocol is not None:
            self._values["use_client_protocol"] = use_client_protocol

    @builtins.property
    def h2_upgrade_policy(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"]:
        '''Specify if http1.1 connection should be upgraded to http2 for the associated destination.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#h2UpgradePolicy
        '''
        result = self._values.get("h2_upgrade_policy")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"], result)

    @builtins.property
    def http1_max_pending_requests(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of pending HTTP requests to a destination.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#http1MaxPendingRequests
        '''
        result = self._values.get("http1_max_pending_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http2_max_requests(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of requests to a backend.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#http2MaxRequests
        '''
        result = self._values.get("http2_max_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def idle_timeout(self) -> typing.Optional[builtins.str]:
        '''The idle timeout for upstream connection pool connections.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#idleTimeout
        '''
        result = self._values.get("idle_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_requests_per_connection(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of requests per connection to a backend.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#maxRequestsPerConnection
        '''
        result = self._values.get("max_requests_per_connection")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#maxRetries
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def use_client_protocol(self) -> typing.Optional[builtins.bool]:
        '''If set to true, client protocol will be preserved while initiating connection to backend.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp#useClientProtocol
        '''
        result = self._values.get("use_client_protocol")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy"
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy(
    enum.Enum,
):
    '''Specify if http1.1 connection should be upgraded to http2 for the associated destination.

    :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy
    '''

    DEFAULT = "DEFAULT"
    '''DEFAULT.'''
    DO_NOT_UPGRADE = "DO_NOT_UPGRADE"
    '''DO_NOT_UPGRADE.'''
    UPGRADE = "UPGRADE"
    '''UPGRADE.'''


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp",
    jsii_struct_bases=[],
    name_mapping={
        "connect_timeout": "connectTimeout",
        "max_connections": "maxConnections",
        "tcp_keepalive": "tcpKeepalive",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp:
    def __init__(
        self,
        *,
        connect_timeout: typing.Optional[builtins.str] = None,
        max_connections: typing.Optional[jsii.Number] = None,
        tcp_keepalive: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive"] = None,
    ) -> None:
        '''Settings common to both HTTP and TCP upstream connections.

        :param connect_timeout: TCP connection timeout.
        :param max_connections: Maximum number of HTTP1 /TCP connections to a destination host.
        :param tcp_keepalive: If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp
        '''
        if isinstance(tcp_keepalive, dict):
            tcp_keepalive = DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive(**tcp_keepalive)
        self._values: typing.Dict[str, typing.Any] = {}
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if max_connections is not None:
            self._values["max_connections"] = max_connections
        if tcp_keepalive is not None:
            self._values["tcp_keepalive"] = tcp_keepalive

    @builtins.property
    def connect_timeout(self) -> typing.Optional[builtins.str]:
        '''TCP connection timeout.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp#connectTimeout
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_connections(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of HTTP1 /TCP connections to a destination host.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp#maxConnections
        '''
        result = self._values.get("max_connections")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tcp_keepalive(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive"]:
        '''If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp#tcpKeepalive
        '''
        result = self._values.get("tcp_keepalive")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "probes": "probes", "time": "time"},
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive:
    def __init__(
        self,
        *,
        interval: typing.Optional[builtins.str] = None,
        probes: typing.Optional[jsii.Number] = None,
        time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''If set then set SO_KEEPALIVE on the socket to enable TCP Keepalives.

        :param interval: The time duration between keep-alive probes.
        :param probes: 
        :param time: 

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if interval is not None:
            self._values["interval"] = interval
        if probes is not None:
            self._values["probes"] = probes
        if time is not None:
            self._values["time"] = time

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''The time duration between keep-alive probes.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive#interval
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def probes(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive#probes
        '''
        result = self._values.get("probes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def time(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive#time
        '''
        result = self._values.get("time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "consistent_hash": "consistentHash",
        "locality_lb_setting": "localityLbSetting",
        "simple": "simple",
        "warmup_duration_secs": "warmupDurationSecs",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer:
    def __init__(
        self,
        *,
        consistent_hash: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash"] = None,
        locality_lb_setting: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting"] = None,
        simple: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerSimple"] = None,
        warmup_duration_secs: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Settings controlling the load balancer algorithms.

        :param consistent_hash: 
        :param locality_lb_setting: 
        :param simple: 
        :param warmup_duration_secs: Represents the warmup duration of Service.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer
        '''
        if isinstance(consistent_hash, dict):
            consistent_hash = DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash(**consistent_hash)
        if isinstance(locality_lb_setting, dict):
            locality_lb_setting = DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting(**locality_lb_setting)
        self._values: typing.Dict[str, typing.Any] = {}
        if consistent_hash is not None:
            self._values["consistent_hash"] = consistent_hash
        if locality_lb_setting is not None:
            self._values["locality_lb_setting"] = locality_lb_setting
        if simple is not None:
            self._values["simple"] = simple
        if warmup_duration_secs is not None:
            self._values["warmup_duration_secs"] = warmup_duration_secs

    @builtins.property
    def consistent_hash(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer#consistentHash
        '''
        result = self._values.get("consistent_hash")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash"], result)

    @builtins.property
    def locality_lb_setting(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer#localityLbSetting
        '''
        result = self._values.get("locality_lb_setting")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting"], result)

    @builtins.property
    def simple(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerSimple"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer#simple
        '''
        result = self._values.get("simple")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerSimple"], result)

    @builtins.property
    def warmup_duration_secs(self) -> typing.Optional[builtins.str]:
        '''Represents the warmup duration of Service.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer#warmupDurationSecs
        '''
        result = self._values.get("warmup_duration_secs")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash",
    jsii_struct_bases=[],
    name_mapping={
        "http_cookie": "httpCookie",
        "http_header_name": "httpHeaderName",
        "http_query_parameter_name": "httpQueryParameterName",
        "minimum_ring_size": "minimumRingSize",
        "use_source_ip": "useSourceIp",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash:
    def __init__(
        self,
        *,
        http_cookie: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie"] = None,
        http_header_name: typing.Optional[builtins.str] = None,
        http_query_parameter_name: typing.Optional[builtins.str] = None,
        minimum_ring_size: typing.Optional[jsii.Number] = None,
        use_source_ip: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param http_cookie: Hash based on HTTP cookie.
        :param http_header_name: Hash based on a specific HTTP header.
        :param http_query_parameter_name: Hash based on a specific HTTP query parameter.
        :param minimum_ring_size: 
        :param use_source_ip: Hash based on the source IP address.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash
        '''
        if isinstance(http_cookie, dict):
            http_cookie = DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie(**http_cookie)
        self._values: typing.Dict[str, typing.Any] = {}
        if http_cookie is not None:
            self._values["http_cookie"] = http_cookie
        if http_header_name is not None:
            self._values["http_header_name"] = http_header_name
        if http_query_parameter_name is not None:
            self._values["http_query_parameter_name"] = http_query_parameter_name
        if minimum_ring_size is not None:
            self._values["minimum_ring_size"] = minimum_ring_size
        if use_source_ip is not None:
            self._values["use_source_ip"] = use_source_ip

    @builtins.property
    def http_cookie(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie"]:
        '''Hash based on HTTP cookie.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#httpCookie
        '''
        result = self._values.get("http_cookie")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie"], result)

    @builtins.property
    def http_header_name(self) -> typing.Optional[builtins.str]:
        '''Hash based on a specific HTTP header.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#httpHeaderName
        '''
        result = self._values.get("http_header_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_query_parameter_name(self) -> typing.Optional[builtins.str]:
        '''Hash based on a specific HTTP query parameter.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#httpQueryParameterName
        '''
        result = self._values.get("http_query_parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_ring_size(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#minimumRingSize
        '''
        result = self._values.get("minimum_ring_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def use_source_ip(self) -> typing.Optional[builtins.bool]:
        '''Hash based on the source IP address.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash#useSourceIp
        '''
        result = self._values.get("use_source_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "ttl": "ttl"},
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Hash based on HTTP cookie.

        :param name: Name of the cookie.
        :param path: Path to set for the cookie.
        :param ttl: Lifetime of the cookie.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if path is not None:
            self._values["path"] = path
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the cookie.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path to set for the cookie.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie#path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        '''Lifetime of the cookie.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie#ttl
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting",
    jsii_struct_bases=[],
    name_mapping={
        "distribute": "distribute",
        "enabled": "enabled",
        "failover": "failover",
        "failover_priority": "failoverPriority",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting:
    def __init__(
        self,
        *,
        distribute: typing.Optional[typing.Sequence["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute"]] = None,
        enabled: typing.Optional[builtins.bool] = None,
        failover: typing.Optional[typing.Sequence["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover"]] = None,
        failover_priority: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param distribute: Optional: only one of distribute, failover or failoverPriority can be set.
        :param enabled: enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.
        :param failover: Optional: only one of distribute, failover or failoverPriority can be set.
        :param failover_priority: failoverPriority is an ordered list of labels used to sort endpoints to do priority based load balancing.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if distribute is not None:
            self._values["distribute"] = distribute
        if enabled is not None:
            self._values["enabled"] = enabled
        if failover is not None:
            self._values["failover"] = failover
        if failover_priority is not None:
            self._values["failover_priority"] = failover_priority

    @builtins.property
    def distribute(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute"]]:
        '''Optional: only one of distribute, failover or failoverPriority can be set.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#distribute
        '''
        result = self._values.get("distribute")
        return typing.cast(typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute"]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''enable locality load balancing, this is DestinationRule-level and will override mesh wide settings in entirety.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def failover(
        self,
    ) -> typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover"]]:
        '''Optional: only one of distribute, failover or failoverPriority can be set.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#failover
        '''
        result = self._values.get("failover")
        return typing.cast(typing.Optional[typing.List["DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover"]], result)

    @builtins.property
    def failover_priority(self) -> typing.Optional[typing.List[builtins.str]]:
        '''failoverPriority is an ordered list of labels used to sort endpoints to do priority based load balancing.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting#failoverPriority
        '''
        result = self._values.get("failover_priority")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        '''
        :param from_: Originating locality, '/' separated, e.g.
        :param to: Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        '''Originating locality, '/' separated, e.g.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute#from
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def to(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''Map of upstream localities to traffic distribution weights.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute#to
        '''
        result = self._values.get("to")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param from_: Originating region.
        :param to: 

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        '''Originating region.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover#from
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def to(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover#to
        '''
        result = self._values.get("to")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerSimple"
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerSimple(enum.Enum):
    '''
    :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerSimple
    '''

    UNSPECIFIED = "UNSPECIFIED"
    '''UNSPECIFIED.'''
    LEAST_CONN = "LEAST_CONN"
    '''LEAST_CONN.'''
    RANDOM = "RANDOM"
    '''RANDOM.'''
    PASSTHROUGH = "PASSTHROUGH"
    '''PASSTHROUGH.'''
    ROUND_ROBIN = "ROUND_ROBIN"
    '''ROUND_ROBIN.'''
    LEAST_REQUEST = "LEAST_REQUEST"
    '''LEAST_REQUEST.'''


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection",
    jsii_struct_bases=[],
    name_mapping={
        "base_ejection_time": "baseEjectionTime",
        "consecutive5_xx_errors": "consecutive5XxErrors",
        "consecutive_errors": "consecutiveErrors",
        "consecutive_gateway_errors": "consecutiveGatewayErrors",
        "consecutive_local_origin_failures": "consecutiveLocalOriginFailures",
        "interval": "interval",
        "max_ejection_percent": "maxEjectionPercent",
        "min_health_percent": "minHealthPercent",
        "split_external_local_origin_errors": "splitExternalLocalOriginErrors",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection:
    def __init__(
        self,
        *,
        base_ejection_time: typing.Optional[builtins.str] = None,
        consecutive5_xx_errors: typing.Optional[jsii.Number] = None,
        consecutive_errors: typing.Optional[jsii.Number] = None,
        consecutive_gateway_errors: typing.Optional[jsii.Number] = None,
        consecutive_local_origin_failures: typing.Optional[jsii.Number] = None,
        interval: typing.Optional[builtins.str] = None,
        max_ejection_percent: typing.Optional[jsii.Number] = None,
        min_health_percent: typing.Optional[jsii.Number] = None,
        split_external_local_origin_errors: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param base_ejection_time: Minimum ejection duration.
        :param consecutive5_xx_errors: Number of 5xx errors before a host is ejected from the connection pool.
        :param consecutive_errors: 
        :param consecutive_gateway_errors: Number of gateway errors before a host is ejected from the connection pool.
        :param consecutive_local_origin_failures: 
        :param interval: Time interval between ejection sweep analysis.
        :param max_ejection_percent: 
        :param min_health_percent: 
        :param split_external_local_origin_errors: Determines whether to distinguish local origin failures from external errors.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if base_ejection_time is not None:
            self._values["base_ejection_time"] = base_ejection_time
        if consecutive5_xx_errors is not None:
            self._values["consecutive5_xx_errors"] = consecutive5_xx_errors
        if consecutive_errors is not None:
            self._values["consecutive_errors"] = consecutive_errors
        if consecutive_gateway_errors is not None:
            self._values["consecutive_gateway_errors"] = consecutive_gateway_errors
        if consecutive_local_origin_failures is not None:
            self._values["consecutive_local_origin_failures"] = consecutive_local_origin_failures
        if interval is not None:
            self._values["interval"] = interval
        if max_ejection_percent is not None:
            self._values["max_ejection_percent"] = max_ejection_percent
        if min_health_percent is not None:
            self._values["min_health_percent"] = min_health_percent
        if split_external_local_origin_errors is not None:
            self._values["split_external_local_origin_errors"] = split_external_local_origin_errors

    @builtins.property
    def base_ejection_time(self) -> typing.Optional[builtins.str]:
        '''Minimum ejection duration.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#baseEjectionTime
        '''
        result = self._values.get("base_ejection_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consecutive5_xx_errors(self) -> typing.Optional[jsii.Number]:
        '''Number of 5xx errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#consecutive5xxErrors
        '''
        result = self._values.get("consecutive5_xx_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consecutive_errors(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#consecutiveErrors
        '''
        result = self._values.get("consecutive_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consecutive_gateway_errors(self) -> typing.Optional[jsii.Number]:
        '''Number of gateway errors before a host is ejected from the connection pool.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#consecutiveGatewayErrors
        '''
        result = self._values.get("consecutive_gateway_errors")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def consecutive_local_origin_failures(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#consecutiveLocalOriginFailures
        '''
        result = self._values.get("consecutive_local_origin_failures")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''Time interval between ejection sweep analysis.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#interval
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_ejection_percent(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#maxEjectionPercent
        '''
        result = self._values.get("max_ejection_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_health_percent(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#minHealthPercent
        '''
        result = self._values.get("min_health_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def split_external_local_origin_errors(self) -> typing.Optional[builtins.bool]:
        '''Determines whether to distinguish local origin failures from external errors.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection#splitExternalLocalOriginErrors
        '''
        result = self._values.get("split_external_local_origin_errors")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param number: 

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsPort
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsPort#number
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsTls",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificates": "caCertificates",
        "client_certificate": "clientCertificate",
        "credential_name": "credentialName",
        "insecure_skip_verify": "insecureSkipVerify",
        "mode": "mode",
        "private_key": "privateKey",
        "sni": "sni",
        "subject_alt_names": "subjectAltNames",
    },
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsTls:
    def __init__(
        self,
        *,
        ca_certificates: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        credential_name: typing.Optional[builtins.str] = None,
        insecure_skip_verify: typing.Optional[builtins.bool] = None,
        mode: typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsTlsMode"] = None,
        private_key: typing.Optional[builtins.str] = None,
        sni: typing.Optional[builtins.str] = None,
        subject_alt_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''TLS related settings for connections to the upstream service.

        :param ca_certificates: 
        :param client_certificate: REQUIRED if mode is ``MUTUAL``.
        :param credential_name: 
        :param insecure_skip_verify: 
        :param mode: 
        :param private_key: REQUIRED if mode is ``MUTUAL``.
        :param sni: SNI string to present to the server during TLS handshake.
        :param subject_alt_names: 

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ca_certificates is not None:
            self._values["ca_certificates"] = ca_certificates
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if credential_name is not None:
            self._values["credential_name"] = credential_name
        if insecure_skip_verify is not None:
            self._values["insecure_skip_verify"] = insecure_skip_verify
        if mode is not None:
            self._values["mode"] = mode
        if private_key is not None:
            self._values["private_key"] = private_key
        if sni is not None:
            self._values["sni"] = sni
        if subject_alt_names is not None:
            self._values["subject_alt_names"] = subject_alt_names

    @builtins.property
    def ca_certificates(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#caCertificates
        '''
        result = self._values.get("ca_certificates")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#clientCertificate
        '''
        result = self._values.get("client_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credential_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#credentialName
        '''
        result = self._values.get("credential_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_skip_verify(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#insecureSkipVerify
        '''
        result = self._values.get("insecure_skip_verify")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def mode(
        self,
    ) -> typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsTlsMode"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyPortLevelSettingsTlsMode"], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#privateKey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sni(self) -> typing.Optional[builtins.str]:
        '''SNI string to present to the server during TLS handshake.

        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#sni
        '''
        result = self._values.get("sni")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_alt_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTls#subjectAltNames
        '''
        result = self._values.get("subject_alt_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyPortLevelSettingsTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyPortLevelSettingsTlsMode"
)
class DestinationRuleSpecTrafficPolicyPortLevelSettingsTlsMode(enum.Enum):
    '''
    :schema: DestinationRuleSpecTrafficPolicyPortLevelSettingsTlsMode
    '''

    DISABLE = "DISABLE"
    '''DISABLE.'''
    SIMPLE = "SIMPLE"
    '''SIMPLE.'''
    MUTUAL = "MUTUAL"
    '''MUTUAL.'''
    ISTIO_MUTUAL = "ISTIO_MUTUAL"
    '''ISTIO_MUTUAL.'''


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyTls",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificates": "caCertificates",
        "client_certificate": "clientCertificate",
        "credential_name": "credentialName",
        "insecure_skip_verify": "insecureSkipVerify",
        "mode": "mode",
        "private_key": "privateKey",
        "sni": "sni",
        "subject_alt_names": "subjectAltNames",
    },
)
class DestinationRuleSpecTrafficPolicyTls:
    def __init__(
        self,
        *,
        ca_certificates: typing.Optional[builtins.str] = None,
        client_certificate: typing.Optional[builtins.str] = None,
        credential_name: typing.Optional[builtins.str] = None,
        insecure_skip_verify: typing.Optional[builtins.bool] = None,
        mode: typing.Optional["DestinationRuleSpecTrafficPolicyTlsMode"] = None,
        private_key: typing.Optional[builtins.str] = None,
        sni: typing.Optional[builtins.str] = None,
        subject_alt_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''TLS related settings for connections to the upstream service.

        :param ca_certificates: 
        :param client_certificate: REQUIRED if mode is ``MUTUAL``.
        :param credential_name: 
        :param insecure_skip_verify: 
        :param mode: 
        :param private_key: REQUIRED if mode is ``MUTUAL``.
        :param sni: SNI string to present to the server during TLS handshake.
        :param subject_alt_names: 

        :schema: DestinationRuleSpecTrafficPolicyTls
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ca_certificates is not None:
            self._values["ca_certificates"] = ca_certificates
        if client_certificate is not None:
            self._values["client_certificate"] = client_certificate
        if credential_name is not None:
            self._values["credential_name"] = credential_name
        if insecure_skip_verify is not None:
            self._values["insecure_skip_verify"] = insecure_skip_verify
        if mode is not None:
            self._values["mode"] = mode
        if private_key is not None:
            self._values["private_key"] = private_key
        if sni is not None:
            self._values["sni"] = sni
        if subject_alt_names is not None:
            self._values["subject_alt_names"] = subject_alt_names

    @builtins.property
    def ca_certificates(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyTls#caCertificates
        '''
        result = self._values.get("ca_certificates")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecTrafficPolicyTls#clientCertificate
        '''
        result = self._values.get("client_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credential_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyTls#credentialName
        '''
        result = self._values.get("credential_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_skip_verify(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyTls#insecureSkipVerify
        '''
        result = self._values.get("insecure_skip_verify")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def mode(self) -> typing.Optional["DestinationRuleSpecTrafficPolicyTlsMode"]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyTls#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["DestinationRuleSpecTrafficPolicyTlsMode"], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``MUTUAL``.

        :schema: DestinationRuleSpecTrafficPolicyTls#privateKey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sni(self) -> typing.Optional[builtins.str]:
        '''SNI string to present to the server during TLS handshake.

        :schema: DestinationRuleSpecTrafficPolicyTls#sni
        '''
        result = self._values.get("sni")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_alt_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: DestinationRuleSpecTrafficPolicyTls#subjectAltNames
        '''
        result = self._values.get("subject_alt_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyTlsMode")
class DestinationRuleSpecTrafficPolicyTlsMode(enum.Enum):
    '''
    :schema: DestinationRuleSpecTrafficPolicyTlsMode
    '''

    DISABLE = "DISABLE"
    '''DISABLE.'''
    SIMPLE = "SIMPLE"
    '''SIMPLE.'''
    MUTUAL = "MUTUAL"
    '''MUTUAL.'''
    ISTIO_MUTUAL = "ISTIO_MUTUAL"
    '''ISTIO_MUTUAL.'''


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecTrafficPolicyTunnel",
    jsii_struct_bases=[],
    name_mapping={
        "protocol": "protocol",
        "target_host": "targetHost",
        "target_port": "targetPort",
    },
)
class DestinationRuleSpecTrafficPolicyTunnel:
    def __init__(
        self,
        *,
        protocol: typing.Optional[builtins.str] = None,
        target_host: typing.Optional[builtins.str] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param protocol: Specifies which protocol to use for tunneling the downstream connection.
        :param target_host: Specifies a host to which the downstream connection is tunneled.
        :param target_port: Specifies a port to which the downstream connection is tunneled.

        :schema: DestinationRuleSpecTrafficPolicyTunnel
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_host is not None:
            self._values["target_host"] = target_host
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Specifies which protocol to use for tunneling the downstream connection.

        :schema: DestinationRuleSpecTrafficPolicyTunnel#protocol
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_host(self) -> typing.Optional[builtins.str]:
        '''Specifies a host to which the downstream connection is tunneled.

        :schema: DestinationRuleSpecTrafficPolicyTunnel#targetHost
        '''
        result = self._values.get("target_host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''Specifies a port to which the downstream connection is tunneled.

        :schema: DestinationRuleSpecTrafficPolicyTunnel#targetPort
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecTrafficPolicyTunnel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.DestinationRuleSpecWorkloadSelector",
    jsii_struct_bases=[],
    name_mapping={"match_labels": "matchLabels"},
)
class DestinationRuleSpecWorkloadSelector:
    def __init__(
        self,
        *,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_labels: 

        :schema: DestinationRuleSpecWorkloadSelector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: DestinationRuleSpecWorkloadSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationRuleSpecWorkloadSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EnvoyFilter(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistionetworking.EnvoyFilter",
):
    '''
    :schema: EnvoyFilter
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["EnvoyFilterSpec"] = None,
    ) -> None:
        '''Defines a "EnvoyFilter" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: Customizing Envoy configuration generated by Istio. See more details at: https://istio.io/docs/reference/config/networking/envoy-filter.html
        '''
        props = EnvoyFilterProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["EnvoyFilterSpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "EnvoyFilter".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: Customizing Envoy configuration generated by Istio. See more details at: https://istio.io/docs/reference/config/networking/envoy-filter.html
        '''
        props = EnvoyFilterProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "EnvoyFilter".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class EnvoyFilterProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["EnvoyFilterSpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: Customizing Envoy configuration generated by Istio. See more details at: https://istio.io/docs/reference/config/networking/envoy-filter.html

        :schema: EnvoyFilter
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = EnvoyFilterSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: EnvoyFilter#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["EnvoyFilterSpec"]:
        '''Customizing Envoy configuration generated by Istio.

        See more details at: https://istio.io/docs/reference/config/networking/envoy-filter.html

        :schema: EnvoyFilter#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["EnvoyFilterSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpec",
    jsii_struct_bases=[],
    name_mapping={
        "config_patches": "configPatches",
        "priority": "priority",
        "workload_selector": "workloadSelector",
    },
)
class EnvoyFilterSpec:
    def __init__(
        self,
        *,
        config_patches: typing.Optional[typing.Sequence["EnvoyFilterSpecConfigPatches"]] = None,
        priority: typing.Optional[jsii.Number] = None,
        workload_selector: typing.Optional["EnvoyFilterSpecWorkloadSelector"] = None,
    ) -> None:
        '''Customizing Envoy configuration generated by Istio.

        See more details at: https://istio.io/docs/reference/config/networking/envoy-filter.html

        :param config_patches: One or more patches with match conditions.
        :param priority: Priority defines the order in which patch sets are applied within a context.
        :param workload_selector: 

        :schema: EnvoyFilterSpec
        '''
        if isinstance(workload_selector, dict):
            workload_selector = EnvoyFilterSpecWorkloadSelector(**workload_selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if config_patches is not None:
            self._values["config_patches"] = config_patches
        if priority is not None:
            self._values["priority"] = priority
        if workload_selector is not None:
            self._values["workload_selector"] = workload_selector

    @builtins.property
    def config_patches(
        self,
    ) -> typing.Optional[typing.List["EnvoyFilterSpecConfigPatches"]]:
        '''One or more patches with match conditions.

        :schema: EnvoyFilterSpec#configPatches
        '''
        result = self._values.get("config_patches")
        return typing.cast(typing.Optional[typing.List["EnvoyFilterSpecConfigPatches"]], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Priority defines the order in which patch sets are applied within a context.

        :schema: EnvoyFilterSpec#priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def workload_selector(self) -> typing.Optional["EnvoyFilterSpecWorkloadSelector"]:
        '''
        :schema: EnvoyFilterSpec#workloadSelector
        '''
        result = self._values.get("workload_selector")
        return typing.cast(typing.Optional["EnvoyFilterSpecWorkloadSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatches",
    jsii_struct_bases=[],
    name_mapping={"apply_to": "applyTo", "match": "match", "patch": "patch"},
)
class EnvoyFilterSpecConfigPatches:
    def __init__(
        self,
        *,
        apply_to: typing.Optional["EnvoyFilterSpecConfigPatchesApplyTo"] = None,
        match: typing.Optional["EnvoyFilterSpecConfigPatchesMatch"] = None,
        patch: typing.Optional["EnvoyFilterSpecConfigPatchesPatch"] = None,
    ) -> None:
        '''
        :param apply_to: 
        :param match: Match on listener/route configuration/cluster.
        :param patch: The patch to apply along with the operation.

        :schema: EnvoyFilterSpecConfigPatches
        '''
        if isinstance(match, dict):
            match = EnvoyFilterSpecConfigPatchesMatch(**match)
        if isinstance(patch, dict):
            patch = EnvoyFilterSpecConfigPatchesPatch(**patch)
        self._values: typing.Dict[str, typing.Any] = {}
        if apply_to is not None:
            self._values["apply_to"] = apply_to
        if match is not None:
            self._values["match"] = match
        if patch is not None:
            self._values["patch"] = patch

    @builtins.property
    def apply_to(self) -> typing.Optional["EnvoyFilterSpecConfigPatchesApplyTo"]:
        '''
        :schema: EnvoyFilterSpecConfigPatches#applyTo
        '''
        result = self._values.get("apply_to")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesApplyTo"], result)

    @builtins.property
    def match(self) -> typing.Optional["EnvoyFilterSpecConfigPatchesMatch"]:
        '''Match on listener/route configuration/cluster.

        :schema: EnvoyFilterSpecConfigPatches#match
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesMatch"], result)

    @builtins.property
    def patch(self) -> typing.Optional["EnvoyFilterSpecConfigPatchesPatch"]:
        '''The patch to apply along with the operation.

        :schema: EnvoyFilterSpecConfigPatches#patch
        '''
        result = self._values.get("patch")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesPatch"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpecConfigPatches(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesApplyTo")
class EnvoyFilterSpecConfigPatchesApplyTo(enum.Enum):
    '''
    :schema: EnvoyFilterSpecConfigPatchesApplyTo
    '''

    INVALID = "INVALID"
    '''INVALID.'''
    LISTENER = "LISTENER"
    '''LISTENER.'''
    FILTER_CHAIN = "FILTER_CHAIN"
    '''FILTER_CHAIN.'''
    NETWORK_FILTER = "NETWORK_FILTER"
    '''NETWORK_FILTER.'''
    HTTP_FILTER = "HTTP_FILTER"
    '''HTTP_FILTER.'''
    ROUTE_CONFIGURATION = "ROUTE_CONFIGURATION"
    '''ROUTE_CONFIGURATION.'''
    VIRTUAL_HOST = "VIRTUAL_HOST"
    '''VIRTUAL_HOST.'''
    HTTP_ROUTE = "HTTP_ROUTE"
    '''HTTP_ROUTE.'''
    CLUSTER = "CLUSTER"
    '''CLUSTER.'''
    EXTENSION_CONFIG = "EXTENSION_CONFIG"
    '''EXTENSION_CONFIG.'''
    BOOTSTRAP = "BOOTSTRAP"
    '''BOOTSTRAP.'''


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesMatch",
    jsii_struct_bases=[],
    name_mapping={
        "cluster": "cluster",
        "context": "context",
        "listener": "listener",
        "proxy": "proxy",
        "route_configuration": "routeConfiguration",
    },
)
class EnvoyFilterSpecConfigPatchesMatch:
    def __init__(
        self,
        *,
        cluster: typing.Optional["EnvoyFilterSpecConfigPatchesMatchCluster"] = None,
        context: typing.Optional["EnvoyFilterSpecConfigPatchesMatchContext"] = None,
        listener: typing.Optional["EnvoyFilterSpecConfigPatchesMatchListener"] = None,
        proxy: typing.Optional["EnvoyFilterSpecConfigPatchesMatchProxy"] = None,
        route_configuration: typing.Optional["EnvoyFilterSpecConfigPatchesMatchRouteConfiguration"] = None,
    ) -> None:
        '''Match on listener/route configuration/cluster.

        :param cluster: Match on envoy cluster attributes.
        :param context: The specific config generation context to match on.
        :param listener: Match on envoy listener attributes.
        :param proxy: Match on properties associated with a proxy.
        :param route_configuration: Match on envoy HTTP route configuration attributes.

        :schema: EnvoyFilterSpecConfigPatchesMatch
        '''
        if isinstance(cluster, dict):
            cluster = EnvoyFilterSpecConfigPatchesMatchCluster(**cluster)
        if isinstance(listener, dict):
            listener = EnvoyFilterSpecConfigPatchesMatchListener(**listener)
        if isinstance(proxy, dict):
            proxy = EnvoyFilterSpecConfigPatchesMatchProxy(**proxy)
        if isinstance(route_configuration, dict):
            route_configuration = EnvoyFilterSpecConfigPatchesMatchRouteConfiguration(**route_configuration)
        self._values: typing.Dict[str, typing.Any] = {}
        if cluster is not None:
            self._values["cluster"] = cluster
        if context is not None:
            self._values["context"] = context
        if listener is not None:
            self._values["listener"] = listener
        if proxy is not None:
            self._values["proxy"] = proxy
        if route_configuration is not None:
            self._values["route_configuration"] = route_configuration

    @builtins.property
    def cluster(self) -> typing.Optional["EnvoyFilterSpecConfigPatchesMatchCluster"]:
        '''Match on envoy cluster attributes.

        :schema: EnvoyFilterSpecConfigPatchesMatch#cluster
        '''
        result = self._values.get("cluster")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesMatchCluster"], result)

    @builtins.property
    def context(self) -> typing.Optional["EnvoyFilterSpecConfigPatchesMatchContext"]:
        '''The specific config generation context to match on.

        :schema: EnvoyFilterSpecConfigPatchesMatch#context
        '''
        result = self._values.get("context")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesMatchContext"], result)

    @builtins.property
    def listener(self) -> typing.Optional["EnvoyFilterSpecConfigPatchesMatchListener"]:
        '''Match on envoy listener attributes.

        :schema: EnvoyFilterSpecConfigPatchesMatch#listener
        '''
        result = self._values.get("listener")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesMatchListener"], result)

    @builtins.property
    def proxy(self) -> typing.Optional["EnvoyFilterSpecConfigPatchesMatchProxy"]:
        '''Match on properties associated with a proxy.

        :schema: EnvoyFilterSpecConfigPatchesMatch#proxy
        '''
        result = self._values.get("proxy")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesMatchProxy"], result)

    @builtins.property
    def route_configuration(
        self,
    ) -> typing.Optional["EnvoyFilterSpecConfigPatchesMatchRouteConfiguration"]:
        '''Match on envoy HTTP route configuration attributes.

        :schema: EnvoyFilterSpecConfigPatchesMatch#routeConfiguration
        '''
        result = self._values.get("route_configuration")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesMatchRouteConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpecConfigPatchesMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesMatchCluster",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "port_number": "portNumber",
        "service": "service",
        "subset": "subset",
    },
)
class EnvoyFilterSpecConfigPatchesMatchCluster:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        port_number: typing.Optional[jsii.Number] = None,
        service: typing.Optional[builtins.str] = None,
        subset: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Match on envoy cluster attributes.

        :param name: The exact name of the cluster to match.
        :param port_number: The service port for which this cluster was generated.
        :param service: The fully qualified service name for this cluster.
        :param subset: The subset associated with the service.

        :schema: EnvoyFilterSpecConfigPatchesMatchCluster
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if port_number is not None:
            self._values["port_number"] = port_number
        if service is not None:
            self._values["service"] = service
        if subset is not None:
            self._values["subset"] = subset

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The exact name of the cluster to match.

        :schema: EnvoyFilterSpecConfigPatchesMatchCluster#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_number(self) -> typing.Optional[jsii.Number]:
        '''The service port for which this cluster was generated.

        :schema: EnvoyFilterSpecConfigPatchesMatchCluster#portNumber
        '''
        result = self._values.get("port_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''The fully qualified service name for this cluster.

        :schema: EnvoyFilterSpecConfigPatchesMatchCluster#service
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subset(self) -> typing.Optional[builtins.str]:
        '''The subset associated with the service.

        :schema: EnvoyFilterSpecConfigPatchesMatchCluster#subset
        '''
        result = self._values.get("subset")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpecConfigPatchesMatchCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesMatchContext")
class EnvoyFilterSpecConfigPatchesMatchContext(enum.Enum):
    '''The specific config generation context to match on.

    :schema: EnvoyFilterSpecConfigPatchesMatchContext
    '''

    ANY = "ANY"
    '''ANY.'''
    SIDECAR_INBOUND = "SIDECAR_INBOUND"
    '''SIDECAR_INBOUND.'''
    SIDECAR_OUTBOUND = "SIDECAR_OUTBOUND"
    '''SIDECAR_OUTBOUND.'''
    GATEWAY = "GATEWAY"
    '''GATEWAY.'''


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesMatchListener",
    jsii_struct_bases=[],
    name_mapping={
        "filter_chain": "filterChain",
        "name": "name",
        "port_name": "portName",
        "port_number": "portNumber",
    },
)
class EnvoyFilterSpecConfigPatchesMatchListener:
    def __init__(
        self,
        *,
        filter_chain: typing.Optional["EnvoyFilterSpecConfigPatchesMatchListenerFilterChain"] = None,
        name: typing.Optional[builtins.str] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Match on envoy listener attributes.

        :param filter_chain: Match a specific filter chain in a listener.
        :param name: Match a specific listener by its name.
        :param port_name: 
        :param port_number: 

        :schema: EnvoyFilterSpecConfigPatchesMatchListener
        '''
        if isinstance(filter_chain, dict):
            filter_chain = EnvoyFilterSpecConfigPatchesMatchListenerFilterChain(**filter_chain)
        self._values: typing.Dict[str, typing.Any] = {}
        if filter_chain is not None:
            self._values["filter_chain"] = filter_chain
        if name is not None:
            self._values["name"] = name
        if port_name is not None:
            self._values["port_name"] = port_name
        if port_number is not None:
            self._values["port_number"] = port_number

    @builtins.property
    def filter_chain(
        self,
    ) -> typing.Optional["EnvoyFilterSpecConfigPatchesMatchListenerFilterChain"]:
        '''Match a specific filter chain in a listener.

        :schema: EnvoyFilterSpecConfigPatchesMatchListener#filterChain
        '''
        result = self._values.get("filter_chain")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesMatchListenerFilterChain"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Match a specific listener by its name.

        :schema: EnvoyFilterSpecConfigPatchesMatchListener#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: EnvoyFilterSpecConfigPatchesMatchListener#portName
        '''
        result = self._values.get("port_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_number(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EnvoyFilterSpecConfigPatchesMatchListener#portNumber
        '''
        result = self._values.get("port_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpecConfigPatchesMatchListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesMatchListenerFilterChain",
    jsii_struct_bases=[],
    name_mapping={
        "application_protocols": "applicationProtocols",
        "destination_port": "destinationPort",
        "filter": "filter",
        "name": "name",
        "sni": "sni",
        "transport_protocol": "transportProtocol",
    },
)
class EnvoyFilterSpecConfigPatchesMatchListenerFilterChain:
    def __init__(
        self,
        *,
        application_protocols: typing.Optional[builtins.str] = None,
        destination_port: typing.Optional[jsii.Number] = None,
        filter: typing.Optional["EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilter"] = None,
        name: typing.Optional[builtins.str] = None,
        sni: typing.Optional[builtins.str] = None,
        transport_protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Match a specific filter chain in a listener.

        :param application_protocols: Applies only to sidecars.
        :param destination_port: The destination_port value used by a filter chain's match condition.
        :param filter: The name of a specific filter to apply the patch to.
        :param name: The name assigned to the filter chain.
        :param sni: The SNI value used by a filter chain's match condition.
        :param transport_protocol: Applies only to ``SIDECAR_INBOUND`` context.

        :schema: EnvoyFilterSpecConfigPatchesMatchListenerFilterChain
        '''
        if isinstance(filter, dict):
            filter = EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilter(**filter)
        self._values: typing.Dict[str, typing.Any] = {}
        if application_protocols is not None:
            self._values["application_protocols"] = application_protocols
        if destination_port is not None:
            self._values["destination_port"] = destination_port
        if filter is not None:
            self._values["filter"] = filter
        if name is not None:
            self._values["name"] = name
        if sni is not None:
            self._values["sni"] = sni
        if transport_protocol is not None:
            self._values["transport_protocol"] = transport_protocol

    @builtins.property
    def application_protocols(self) -> typing.Optional[builtins.str]:
        '''Applies only to sidecars.

        :schema: EnvoyFilterSpecConfigPatchesMatchListenerFilterChain#applicationProtocols
        '''
        result = self._values.get("application_protocols")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_port(self) -> typing.Optional[jsii.Number]:
        '''The destination_port value used by a filter chain's match condition.

        :schema: EnvoyFilterSpecConfigPatchesMatchListenerFilterChain#destinationPort
        '''
        result = self._values.get("destination_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def filter(
        self,
    ) -> typing.Optional["EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilter"]:
        '''The name of a specific filter to apply the patch to.

        :schema: EnvoyFilterSpecConfigPatchesMatchListenerFilterChain#filter
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilter"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name assigned to the filter chain.

        :schema: EnvoyFilterSpecConfigPatchesMatchListenerFilterChain#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sni(self) -> typing.Optional[builtins.str]:
        '''The SNI value used by a filter chain's match condition.

        :schema: EnvoyFilterSpecConfigPatchesMatchListenerFilterChain#sni
        '''
        result = self._values.get("sni")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def transport_protocol(self) -> typing.Optional[builtins.str]:
        '''Applies only to ``SIDECAR_INBOUND`` context.

        :schema: EnvoyFilterSpecConfigPatchesMatchListenerFilterChain#transportProtocol
        '''
        result = self._values.get("transport_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpecConfigPatchesMatchListenerFilterChain(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "sub_filter": "subFilter"},
)
class EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilter:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        sub_filter: typing.Optional["EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilterSubFilter"] = None,
    ) -> None:
        '''The name of a specific filter to apply the patch to.

        :param name: The filter name to match on.
        :param sub_filter: 

        :schema: EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilter
        '''
        if isinstance(sub_filter, dict):
            sub_filter = EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilterSubFilter(**sub_filter)
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if sub_filter is not None:
            self._values["sub_filter"] = sub_filter

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The filter name to match on.

        :schema: EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilter#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sub_filter(
        self,
    ) -> typing.Optional["EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilterSubFilter"]:
        '''
        :schema: EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilter#subFilter
        '''
        result = self._values.get("sub_filter")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilterSubFilter"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilterSubFilter",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilterSubFilter:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param name: The filter name to match on.

        :schema: EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilterSubFilter
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The filter name to match on.

        :schema: EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilterSubFilter#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilterSubFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesMatchProxy",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "proxy_version": "proxyVersion"},
)
class EnvoyFilterSpecConfigPatchesMatchProxy:
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        proxy_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Match on properties associated with a proxy.

        :param metadata: 
        :param proxy_version: 

        :schema: EnvoyFilterSpecConfigPatchesMatchProxy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if proxy_version is not None:
            self._values["proxy_version"] = proxy_version

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: EnvoyFilterSpecConfigPatchesMatchProxy#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def proxy_version(self) -> typing.Optional[builtins.str]:
        '''
        :schema: EnvoyFilterSpecConfigPatchesMatchProxy#proxyVersion
        '''
        result = self._values.get("proxy_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpecConfigPatchesMatchProxy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesMatchRouteConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "gateway": "gateway",
        "name": "name",
        "port_name": "portName",
        "port_number": "portNumber",
        "vhost": "vhost",
    },
)
class EnvoyFilterSpecConfigPatchesMatchRouteConfiguration:
    def __init__(
        self,
        *,
        gateway: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_number: typing.Optional[jsii.Number] = None,
        vhost: typing.Optional["EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhost"] = None,
    ) -> None:
        '''Match on envoy HTTP route configuration attributes.

        :param gateway: 
        :param name: Route configuration name to match on.
        :param port_name: Applicable only for GATEWAY context.
        :param port_number: 
        :param vhost: 

        :schema: EnvoyFilterSpecConfigPatchesMatchRouteConfiguration
        '''
        if isinstance(vhost, dict):
            vhost = EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhost(**vhost)
        self._values: typing.Dict[str, typing.Any] = {}
        if gateway is not None:
            self._values["gateway"] = gateway
        if name is not None:
            self._values["name"] = name
        if port_name is not None:
            self._values["port_name"] = port_name
        if port_number is not None:
            self._values["port_number"] = port_number
        if vhost is not None:
            self._values["vhost"] = vhost

    @builtins.property
    def gateway(self) -> typing.Optional[builtins.str]:
        '''
        :schema: EnvoyFilterSpecConfigPatchesMatchRouteConfiguration#gateway
        '''
        result = self._values.get("gateway")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Route configuration name to match on.

        :schema: EnvoyFilterSpecConfigPatchesMatchRouteConfiguration#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_name(self) -> typing.Optional[builtins.str]:
        '''Applicable only for GATEWAY context.

        :schema: EnvoyFilterSpecConfigPatchesMatchRouteConfiguration#portName
        '''
        result = self._values.get("port_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_number(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: EnvoyFilterSpecConfigPatchesMatchRouteConfiguration#portNumber
        '''
        result = self._values.get("port_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vhost(
        self,
    ) -> typing.Optional["EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhost"]:
        '''
        :schema: EnvoyFilterSpecConfigPatchesMatchRouteConfiguration#vhost
        '''
        result = self._values.get("vhost")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhost"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpecConfigPatchesMatchRouteConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhost",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "route": "route"},
)
class EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhost:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        route: typing.Optional["EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRoute"] = None,
    ) -> None:
        '''
        :param name: 
        :param route: Match a specific route within the virtual host.

        :schema: EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhost
        '''
        if isinstance(route, dict):
            route = EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRoute(**route)
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if route is not None:
            self._values["route"] = route

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhost#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route(
        self,
    ) -> typing.Optional["EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRoute"]:
        '''Match a specific route within the virtual host.

        :schema: EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhost#route
        '''
        result = self._values.get("route")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRoute"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhost(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRoute",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "name": "name"},
)
class EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRoute:
    def __init__(
        self,
        *,
        action: typing.Optional["EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRouteAction"] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Match a specific route within the virtual host.

        :param action: Match a route with specific action type.
        :param name: 

        :schema: EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRoute
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def action(
        self,
    ) -> typing.Optional["EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRouteAction"]:
        '''Match a route with specific action type.

        :schema: EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRoute#action
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRouteAction"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRoute#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRouteAction"
)
class EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRouteAction(enum.Enum):
    '''Match a route with specific action type.

    :schema: EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRouteAction
    '''

    ANY = "ANY"
    '''ANY.'''
    ROUTE = "ROUTE"
    '''ROUTE.'''
    REDIRECT = "REDIRECT"
    '''REDIRECT.'''
    DIRECT_RESPONSE = "DIRECT_RESPONSE"
    '''DIRECT_RESPONSE.'''


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesPatch",
    jsii_struct_bases=[],
    name_mapping={
        "filter_class": "filterClass",
        "operation": "operation",
        "value": "value",
    },
)
class EnvoyFilterSpecConfigPatchesPatch:
    def __init__(
        self,
        *,
        filter_class: typing.Optional["EnvoyFilterSpecConfigPatchesPatchFilterClass"] = None,
        operation: typing.Optional["EnvoyFilterSpecConfigPatchesPatchOperation"] = None,
        value: typing.Any = None,
    ) -> None:
        '''The patch to apply along with the operation.

        :param filter_class: Determines the filter insertion order.
        :param operation: Determines how the patch should be applied.
        :param value: The JSON config of the object being patched.

        :schema: EnvoyFilterSpecConfigPatchesPatch
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if filter_class is not None:
            self._values["filter_class"] = filter_class
        if operation is not None:
            self._values["operation"] = operation
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def filter_class(
        self,
    ) -> typing.Optional["EnvoyFilterSpecConfigPatchesPatchFilterClass"]:
        '''Determines the filter insertion order.

        :schema: EnvoyFilterSpecConfigPatchesPatch#filterClass
        '''
        result = self._values.get("filter_class")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesPatchFilterClass"], result)

    @builtins.property
    def operation(
        self,
    ) -> typing.Optional["EnvoyFilterSpecConfigPatchesPatchOperation"]:
        '''Determines how the patch should be applied.

        :schema: EnvoyFilterSpecConfigPatchesPatch#operation
        '''
        result = self._values.get("operation")
        return typing.cast(typing.Optional["EnvoyFilterSpecConfigPatchesPatchOperation"], result)

    @builtins.property
    def value(self) -> typing.Any:
        '''The JSON config of the object being patched.

        :schema: EnvoyFilterSpecConfigPatchesPatch#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpecConfigPatchesPatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesPatchFilterClass")
class EnvoyFilterSpecConfigPatchesPatchFilterClass(enum.Enum):
    '''Determines the filter insertion order.

    :schema: EnvoyFilterSpecConfigPatchesPatchFilterClass
    '''

    UNSPECIFIED = "UNSPECIFIED"
    '''UNSPECIFIED.'''
    AUTHN = "AUTHN"
    '''AUTHN.'''
    AUTHZ = "AUTHZ"
    '''AUTHZ.'''
    STATS = "STATS"
    '''STATS.'''


@jsii.enum(jsii_type="ioistionetworking.EnvoyFilterSpecConfigPatchesPatchOperation")
class EnvoyFilterSpecConfigPatchesPatchOperation(enum.Enum):
    '''Determines how the patch should be applied.

    :schema: EnvoyFilterSpecConfigPatchesPatchOperation
    '''

    INVALID = "INVALID"
    '''INVALID.'''
    MERGE = "MERGE"
    '''MERGE.'''
    ADD = "ADD"
    '''ADD.'''
    REMOVE = "REMOVE"
    '''REMOVE.'''
    INSERT_BEFORE = "INSERT_BEFORE"
    '''INSERT_BEFORE.'''
    INSERT_AFTER = "INSERT_AFTER"
    '''INSERT_AFTER.'''
    INSERT_FIRST = "INSERT_FIRST"
    '''INSERT_FIRST.'''
    REPLACE = "REPLACE"
    '''REPLACE.'''


@jsii.data_type(
    jsii_type="ioistionetworking.EnvoyFilterSpecWorkloadSelector",
    jsii_struct_bases=[],
    name_mapping={"labels": "labels"},
)
class EnvoyFilterSpecWorkloadSelector:
    def __init__(
        self,
        *,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param labels: 

        :schema: EnvoyFilterSpecWorkloadSelector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: EnvoyFilterSpecWorkloadSelector#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvoyFilterSpecWorkloadSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Gateway(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistionetworking.Gateway",
):
    '''
    :schema: Gateway
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["GatewaySpec"] = None,
    ) -> None:
        '''Defines a "Gateway" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: Configuration affecting edge load balancer. See more details at: https://istio.io/docs/reference/config/networking/gateway.html
        '''
        props = GatewayProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["GatewaySpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "Gateway".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: Configuration affecting edge load balancer. See more details at: https://istio.io/docs/reference/config/networking/gateway.html
        '''
        props = GatewayProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "Gateway".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistionetworking.GatewayProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class GatewayProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["GatewaySpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: Configuration affecting edge load balancer. See more details at: https://istio.io/docs/reference/config/networking/gateway.html

        :schema: Gateway
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = GatewaySpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: Gateway#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["GatewaySpec"]:
        '''Configuration affecting edge load balancer.

        See more details at: https://istio.io/docs/reference/config/networking/gateway.html

        :schema: Gateway#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["GatewaySpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.GatewaySpec",
    jsii_struct_bases=[],
    name_mapping={"selector": "selector", "servers": "servers"},
)
class GatewaySpec:
    def __init__(
        self,
        *,
        selector: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        servers: typing.Optional[typing.Sequence["GatewaySpecServers"]] = None,
    ) -> None:
        '''Configuration affecting edge load balancer.

        See more details at: https://istio.io/docs/reference/config/networking/gateway.html

        :param selector: 
        :param servers: A list of server specifications.

        :schema: GatewaySpec
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if selector is not None:
            self._values["selector"] = selector
        if servers is not None:
            self._values["servers"] = servers

    @builtins.property
    def selector(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: GatewaySpec#selector
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def servers(self) -> typing.Optional[typing.List["GatewaySpecServers"]]:
        '''A list of server specifications.

        :schema: GatewaySpec#servers
        '''
        result = self._values.get("servers")
        return typing.cast(typing.Optional[typing.List["GatewaySpecServers"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.GatewaySpecServers",
    jsii_struct_bases=[],
    name_mapping={
        "bind": "bind",
        "default_endpoint": "defaultEndpoint",
        "hosts": "hosts",
        "name": "name",
        "port": "port",
        "tls": "tls",
    },
)
class GatewaySpecServers:
    def __init__(
        self,
        *,
        bind: typing.Optional[builtins.str] = None,
        default_endpoint: typing.Optional[builtins.str] = None,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional["GatewaySpecServersPort"] = None,
        tls: typing.Optional["GatewaySpecServersTls"] = None,
    ) -> None:
        '''
        :param bind: 
        :param default_endpoint: 
        :param hosts: One or more hosts exposed by this gateway.
        :param name: An optional name of the server, when set must be unique across all servers.
        :param port: 
        :param tls: Set of TLS related options that govern the server's behavior.

        :schema: GatewaySpecServers
        '''
        if isinstance(port, dict):
            port = GatewaySpecServersPort(**port)
        if isinstance(tls, dict):
            tls = GatewaySpecServersTls(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if bind is not None:
            self._values["bind"] = bind
        if default_endpoint is not None:
            self._values["default_endpoint"] = default_endpoint
        if hosts is not None:
            self._values["hosts"] = hosts
        if name is not None:
            self._values["name"] = name
        if port is not None:
            self._values["port"] = port
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def bind(self) -> typing.Optional[builtins.str]:
        '''
        :schema: GatewaySpecServers#bind
        '''
        result = self._values.get("bind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :schema: GatewaySpecServers#defaultEndpoint
        '''
        result = self._values.get("default_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''One or more hosts exposed by this gateway.

        :schema: GatewaySpecServers#hosts
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''An optional name of the server, when set must be unique across all servers.

        :schema: GatewaySpecServers#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional["GatewaySpecServersPort"]:
        '''
        :schema: GatewaySpecServers#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional["GatewaySpecServersPort"], result)

    @builtins.property
    def tls(self) -> typing.Optional["GatewaySpecServersTls"]:
        '''Set of TLS related options that govern the server's behavior.

        :schema: GatewaySpecServers#tls
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["GatewaySpecServersTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecServers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.GatewaySpecServersPort",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "number": "number",
        "protocol": "protocol",
        "target_port": "targetPort",
    },
)
class GatewaySpecServersPort:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Label assigned to the port.
        :param number: A valid non-negative integer port number.
        :param protocol: The protocol exposed on the port.
        :param target_port: 

        :schema: GatewaySpecServersPort
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if number is not None:
            self._values["number"] = number
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Label assigned to the port.

        :schema: GatewaySpecServersPort#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''A valid non-negative integer port number.

        :schema: GatewaySpecServersPort#number
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol exposed on the port.

        :schema: GatewaySpecServersPort#protocol
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: GatewaySpecServersPort#targetPort
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecServersPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.GatewaySpecServersTls",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificates": "caCertificates",
        "cipher_suites": "cipherSuites",
        "credential_name": "credentialName",
        "https_redirect": "httpsRedirect",
        "max_protocol_version": "maxProtocolVersion",
        "min_protocol_version": "minProtocolVersion",
        "mode": "mode",
        "private_key": "privateKey",
        "server_certificate": "serverCertificate",
        "subject_alt_names": "subjectAltNames",
        "verify_certificate_hash": "verifyCertificateHash",
        "verify_certificate_spki": "verifyCertificateSpki",
    },
)
class GatewaySpecServersTls:
    def __init__(
        self,
        *,
        ca_certificates: typing.Optional[builtins.str] = None,
        cipher_suites: typing.Optional[typing.Sequence[builtins.str]] = None,
        credential_name: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[builtins.bool] = None,
        max_protocol_version: typing.Optional["GatewaySpecServersTlsMaxProtocolVersion"] = None,
        min_protocol_version: typing.Optional["GatewaySpecServersTlsMinProtocolVersion"] = None,
        mode: typing.Optional["GatewaySpecServersTlsMode"] = None,
        private_key: typing.Optional[builtins.str] = None,
        server_certificate: typing.Optional[builtins.str] = None,
        subject_alt_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        verify_certificate_hash: typing.Optional[typing.Sequence[builtins.str]] = None,
        verify_certificate_spki: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Set of TLS related options that govern the server's behavior.

        :param ca_certificates: REQUIRED if mode is ``MUTUAL``.
        :param cipher_suites: Optional: If specified, only support the specified cipher list.
        :param credential_name: 
        :param https_redirect: 
        :param max_protocol_version: Optional: Maximum TLS protocol version.
        :param min_protocol_version: Optional: Minimum TLS protocol version.
        :param mode: 
        :param private_key: REQUIRED if mode is ``SIMPLE`` or ``MUTUAL``.
        :param server_certificate: REQUIRED if mode is ``SIMPLE`` or ``MUTUAL``.
        :param subject_alt_names: 
        :param verify_certificate_hash: 
        :param verify_certificate_spki: 

        :schema: GatewaySpecServersTls
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ca_certificates is not None:
            self._values["ca_certificates"] = ca_certificates
        if cipher_suites is not None:
            self._values["cipher_suites"] = cipher_suites
        if credential_name is not None:
            self._values["credential_name"] = credential_name
        if https_redirect is not None:
            self._values["https_redirect"] = https_redirect
        if max_protocol_version is not None:
            self._values["max_protocol_version"] = max_protocol_version
        if min_protocol_version is not None:
            self._values["min_protocol_version"] = min_protocol_version
        if mode is not None:
            self._values["mode"] = mode
        if private_key is not None:
            self._values["private_key"] = private_key
        if server_certificate is not None:
            self._values["server_certificate"] = server_certificate
        if subject_alt_names is not None:
            self._values["subject_alt_names"] = subject_alt_names
        if verify_certificate_hash is not None:
            self._values["verify_certificate_hash"] = verify_certificate_hash
        if verify_certificate_spki is not None:
            self._values["verify_certificate_spki"] = verify_certificate_spki

    @builtins.property
    def ca_certificates(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``MUTUAL``.

        :schema: GatewaySpecServersTls#caCertificates
        '''
        result = self._values.get("ca_certificates")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cipher_suites(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional: If specified, only support the specified cipher list.

        :schema: GatewaySpecServersTls#cipherSuites
        '''
        result = self._values.get("cipher_suites")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def credential_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: GatewaySpecServersTls#credentialName
        '''
        result = self._values.get("credential_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def https_redirect(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: GatewaySpecServersTls#httpsRedirect
        '''
        result = self._values.get("https_redirect")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def max_protocol_version(
        self,
    ) -> typing.Optional["GatewaySpecServersTlsMaxProtocolVersion"]:
        '''Optional: Maximum TLS protocol version.

        :schema: GatewaySpecServersTls#maxProtocolVersion
        '''
        result = self._values.get("max_protocol_version")
        return typing.cast(typing.Optional["GatewaySpecServersTlsMaxProtocolVersion"], result)

    @builtins.property
    def min_protocol_version(
        self,
    ) -> typing.Optional["GatewaySpecServersTlsMinProtocolVersion"]:
        '''Optional: Minimum TLS protocol version.

        :schema: GatewaySpecServersTls#minProtocolVersion
        '''
        result = self._values.get("min_protocol_version")
        return typing.cast(typing.Optional["GatewaySpecServersTlsMinProtocolVersion"], result)

    @builtins.property
    def mode(self) -> typing.Optional["GatewaySpecServersTlsMode"]:
        '''
        :schema: GatewaySpecServersTls#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["GatewaySpecServersTlsMode"], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``SIMPLE`` or ``MUTUAL``.

        :schema: GatewaySpecServersTls#privateKey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_certificate(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``SIMPLE`` or ``MUTUAL``.

        :schema: GatewaySpecServersTls#serverCertificate
        '''
        result = self._values.get("server_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_alt_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: GatewaySpecServersTls#subjectAltNames
        '''
        result = self._values.get("subject_alt_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def verify_certificate_hash(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: GatewaySpecServersTls#verifyCertificateHash
        '''
        result = self._values.get("verify_certificate_hash")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def verify_certificate_spki(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: GatewaySpecServersTls#verifyCertificateSpki
        '''
        result = self._values.get("verify_certificate_spki")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewaySpecServersTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistionetworking.GatewaySpecServersTlsMaxProtocolVersion")
class GatewaySpecServersTlsMaxProtocolVersion(enum.Enum):
    '''Optional: Maximum TLS protocol version.

    :schema: GatewaySpecServersTlsMaxProtocolVersion
    '''

    TLS_AUTO = "TLS_AUTO"
    '''TLS_AUTO.'''
    TLSV1_0 = "TLSV1_0"
    '''TLSV1_0.'''
    TLSV1_1 = "TLSV1_1"
    '''TLSV1_1.'''
    TLSV1_2 = "TLSV1_2"
    '''TLSV1_2.'''
    TLSV1_3 = "TLSV1_3"
    '''TLSV1_3.'''


@jsii.enum(jsii_type="ioistionetworking.GatewaySpecServersTlsMinProtocolVersion")
class GatewaySpecServersTlsMinProtocolVersion(enum.Enum):
    '''Optional: Minimum TLS protocol version.

    :schema: GatewaySpecServersTlsMinProtocolVersion
    '''

    TLS_AUTO = "TLS_AUTO"
    '''TLS_AUTO.'''
    TLSV1_0 = "TLSV1_0"
    '''TLSV1_0.'''
    TLSV1_1 = "TLSV1_1"
    '''TLSV1_1.'''
    TLSV1_2 = "TLSV1_2"
    '''TLSV1_2.'''
    TLSV1_3 = "TLSV1_3"
    '''TLSV1_3.'''


@jsii.enum(jsii_type="ioistionetworking.GatewaySpecServersTlsMode")
class GatewaySpecServersTlsMode(enum.Enum):
    '''
    :schema: GatewaySpecServersTlsMode
    '''

    PASSTHROUGH = "PASSTHROUGH"
    '''PASSTHROUGH.'''
    SIMPLE = "SIMPLE"
    '''SIMPLE.'''
    MUTUAL = "MUTUAL"
    '''MUTUAL.'''
    AUTO_PASSTHROUGH = "AUTO_PASSTHROUGH"
    '''AUTO_PASSTHROUGH.'''
    ISTIO_MUTUAL = "ISTIO_MUTUAL"
    '''ISTIO_MUTUAL.'''


class ProxyConfig(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistionetworking.ProxyConfig",
):
    '''
    :schema: ProxyConfig
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["ProxyConfigSpec"] = None,
    ) -> None:
        '''Defines a "ProxyConfig" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: Provides configuration for individual workloads. See more details at: https://istio.io/docs/reference/config/networking/proxy-config.html
        '''
        props = ProxyConfigProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["ProxyConfigSpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "ProxyConfig".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: Provides configuration for individual workloads. See more details at: https://istio.io/docs/reference/config/networking/proxy-config.html
        '''
        props = ProxyConfigProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "ProxyConfig".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistionetworking.ProxyConfigProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class ProxyConfigProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["ProxyConfigSpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: Provides configuration for individual workloads. See more details at: https://istio.io/docs/reference/config/networking/proxy-config.html

        :schema: ProxyConfig
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = ProxyConfigSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: ProxyConfig#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["ProxyConfigSpec"]:
        '''Provides configuration for individual workloads.

        See more details at: https://istio.io/docs/reference/config/networking/proxy-config.html

        :schema: ProxyConfig#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["ProxyConfigSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProxyConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.ProxyConfigSpec",
    jsii_struct_bases=[],
    name_mapping={
        "concurrency": "concurrency",
        "environment_variables": "environmentVariables",
        "image": "image",
        "selector": "selector",
    },
)
class ProxyConfigSpec:
    def __init__(
        self,
        *,
        concurrency: typing.Optional[jsii.Number] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        image: typing.Optional["ProxyConfigSpecImage"] = None,
        selector: typing.Optional["ProxyConfigSpecSelector"] = None,
    ) -> None:
        '''Provides configuration for individual workloads.

        See more details at: https://istio.io/docs/reference/config/networking/proxy-config.html

        :param concurrency: The number of worker threads to run.
        :param environment_variables: Additional environment variables for the proxy.
        :param image: Specifies the details of the proxy image.
        :param selector: Optional.

        :schema: ProxyConfigSpec
        '''
        if isinstance(image, dict):
            image = ProxyConfigSpecImage(**image)
        if isinstance(selector, dict):
            selector = ProxyConfigSpecSelector(**selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if concurrency is not None:
            self._values["concurrency"] = concurrency
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if image is not None:
            self._values["image"] = image
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def concurrency(self) -> typing.Optional[jsii.Number]:
        '''The number of worker threads to run.

        :schema: ProxyConfigSpec#concurrency
        '''
        result = self._values.get("concurrency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional environment variables for the proxy.

        :schema: ProxyConfigSpec#environmentVariables
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def image(self) -> typing.Optional["ProxyConfigSpecImage"]:
        '''Specifies the details of the proxy image.

        :schema: ProxyConfigSpec#image
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional["ProxyConfigSpecImage"], result)

    @builtins.property
    def selector(self) -> typing.Optional["ProxyConfigSpecSelector"]:
        '''Optional.

        :schema: ProxyConfigSpec#selector
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional["ProxyConfigSpecSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProxyConfigSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.ProxyConfigSpecImage",
    jsii_struct_bases=[],
    name_mapping={"image_type": "imageType"},
)
class ProxyConfigSpecImage:
    def __init__(self, *, image_type: typing.Optional[builtins.str] = None) -> None:
        '''Specifies the details of the proxy image.

        :param image_type: The image type of the image.

        :schema: ProxyConfigSpecImage
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if image_type is not None:
            self._values["image_type"] = image_type

    @builtins.property
    def image_type(self) -> typing.Optional[builtins.str]:
        '''The image type of the image.

        :schema: ProxyConfigSpecImage#imageType
        '''
        result = self._values.get("image_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProxyConfigSpecImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.ProxyConfigSpecSelector",
    jsii_struct_bases=[],
    name_mapping={"match_labels": "matchLabels"},
)
class ProxyConfigSpecSelector:
    def __init__(
        self,
        *,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Optional.

        :param match_labels: 

        :schema: ProxyConfigSpecSelector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: ProxyConfigSpecSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProxyConfigSpecSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEntry(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistionetworking.ServiceEntry",
):
    '''
    :schema: ServiceEntry
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["ServiceEntrySpec"] = None,
    ) -> None:
        '''Defines a "ServiceEntry" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: Configuration affecting service registry. See more details at: https://istio.io/docs/reference/config/networking/service-entry.html
        '''
        props = ServiceEntryProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["ServiceEntrySpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "ServiceEntry".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: Configuration affecting service registry. See more details at: https://istio.io/docs/reference/config/networking/service-entry.html
        '''
        props = ServiceEntryProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "ServiceEntry".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistionetworking.ServiceEntryProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class ServiceEntryProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["ServiceEntrySpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: Configuration affecting service registry. See more details at: https://istio.io/docs/reference/config/networking/service-entry.html

        :schema: ServiceEntry
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = ServiceEntrySpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: ServiceEntry#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["ServiceEntrySpec"]:
        '''Configuration affecting service registry.

        See more details at: https://istio.io/docs/reference/config/networking/service-entry.html

        :schema: ServiceEntry#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["ServiceEntrySpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEntryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.ServiceEntrySpec",
    jsii_struct_bases=[],
    name_mapping={
        "addresses": "addresses",
        "endpoints": "endpoints",
        "export_to": "exportTo",
        "hosts": "hosts",
        "location": "location",
        "ports": "ports",
        "resolution": "resolution",
        "subject_alt_names": "subjectAltNames",
        "workload_selector": "workloadSelector",
    },
)
class ServiceEntrySpec:
    def __init__(
        self,
        *,
        addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        endpoints: typing.Optional[typing.Sequence["ServiceEntrySpecEndpoints"]] = None,
        export_to: typing.Optional[typing.Sequence[builtins.str]] = None,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        location: typing.Optional["ServiceEntrySpecLocation"] = None,
        ports: typing.Optional[typing.Sequence["ServiceEntrySpecPorts"]] = None,
        resolution: typing.Optional["ServiceEntrySpecResolution"] = None,
        subject_alt_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        workload_selector: typing.Optional["ServiceEntrySpecWorkloadSelector"] = None,
    ) -> None:
        '''Configuration affecting service registry.

        See more details at: https://istio.io/docs/reference/config/networking/service-entry.html

        :param addresses: The virtual IP addresses associated with the service.
        :param endpoints: One or more endpoints associated with the service.
        :param export_to: A list of namespaces to which this service is exported.
        :param hosts: The hosts associated with the ServiceEntry.
        :param location: 
        :param ports: The ports associated with the external service.
        :param resolution: Service discovery mode for the hosts.
        :param subject_alt_names: 
        :param workload_selector: Applicable only for MESH_INTERNAL services.

        :schema: ServiceEntrySpec
        '''
        if isinstance(workload_selector, dict):
            workload_selector = ServiceEntrySpecWorkloadSelector(**workload_selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if addresses is not None:
            self._values["addresses"] = addresses
        if endpoints is not None:
            self._values["endpoints"] = endpoints
        if export_to is not None:
            self._values["export_to"] = export_to
        if hosts is not None:
            self._values["hosts"] = hosts
        if location is not None:
            self._values["location"] = location
        if ports is not None:
            self._values["ports"] = ports
        if resolution is not None:
            self._values["resolution"] = resolution
        if subject_alt_names is not None:
            self._values["subject_alt_names"] = subject_alt_names
        if workload_selector is not None:
            self._values["workload_selector"] = workload_selector

    @builtins.property
    def addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The virtual IP addresses associated with the service.

        :schema: ServiceEntrySpec#addresses
        '''
        result = self._values.get("addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def endpoints(self) -> typing.Optional[typing.List["ServiceEntrySpecEndpoints"]]:
        '''One or more endpoints associated with the service.

        :schema: ServiceEntrySpec#endpoints
        '''
        result = self._values.get("endpoints")
        return typing.cast(typing.Optional[typing.List["ServiceEntrySpecEndpoints"]], result)

    @builtins.property
    def export_to(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of namespaces to which this service is exported.

        :schema: ServiceEntrySpec#exportTo
        '''
        result = self._values.get("export_to")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The hosts associated with the ServiceEntry.

        :schema: ServiceEntrySpec#hosts
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def location(self) -> typing.Optional["ServiceEntrySpecLocation"]:
        '''
        :schema: ServiceEntrySpec#location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional["ServiceEntrySpecLocation"], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List["ServiceEntrySpecPorts"]]:
        '''The ports associated with the external service.

        :schema: ServiceEntrySpec#ports
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List["ServiceEntrySpecPorts"]], result)

    @builtins.property
    def resolution(self) -> typing.Optional["ServiceEntrySpecResolution"]:
        '''Service discovery mode for the hosts.

        :schema: ServiceEntrySpec#resolution
        '''
        result = self._values.get("resolution")
        return typing.cast(typing.Optional["ServiceEntrySpecResolution"], result)

    @builtins.property
    def subject_alt_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: ServiceEntrySpec#subjectAltNames
        '''
        result = self._values.get("subject_alt_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def workload_selector(self) -> typing.Optional["ServiceEntrySpecWorkloadSelector"]:
        '''Applicable only for MESH_INTERNAL services.

        :schema: ServiceEntrySpec#workloadSelector
        '''
        result = self._values.get("workload_selector")
        return typing.cast(typing.Optional["ServiceEntrySpecWorkloadSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEntrySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.ServiceEntrySpecEndpoints",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "labels": "labels",
        "locality": "locality",
        "network": "network",
        "ports": "ports",
        "service_account": "serviceAccount",
        "weight": "weight",
    },
)
class ServiceEntrySpecEndpoints:
    def __init__(
        self,
        *,
        address: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        locality: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
        service_account: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param address: 
        :param labels: One or more labels associated with the endpoint.
        :param locality: The locality associated with the endpoint.
        :param network: 
        :param ports: Set of ports associated with the endpoint.
        :param service_account: 
        :param weight: The load balancing weight associated with the endpoint.

        :schema: ServiceEntrySpecEndpoints
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if address is not None:
            self._values["address"] = address
        if labels is not None:
            self._values["labels"] = labels
        if locality is not None:
            self._values["locality"] = locality
        if network is not None:
            self._values["network"] = network
        if ports is not None:
            self._values["ports"] = ports
        if service_account is not None:
            self._values["service_account"] = service_account
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ServiceEntrySpecEndpoints#address
        '''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''One or more labels associated with the endpoint.

        :schema: ServiceEntrySpecEndpoints#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def locality(self) -> typing.Optional[builtins.str]:
        '''The locality associated with the endpoint.

        :schema: ServiceEntrySpecEndpoints#locality
        '''
        result = self._values.get("locality")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ServiceEntrySpecEndpoints#network
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''Set of ports associated with the endpoint.

        :schema: ServiceEntrySpecEndpoints#ports
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''
        :schema: ServiceEntrySpecEndpoints#serviceAccount
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''The load balancing weight associated with the endpoint.

        :schema: ServiceEntrySpecEndpoints#weight
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEntrySpecEndpoints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistionetworking.ServiceEntrySpecLocation")
class ServiceEntrySpecLocation(enum.Enum):
    '''
    :schema: ServiceEntrySpecLocation
    '''

    MESH_EXTERNAL = "MESH_EXTERNAL"
    '''MESH_EXTERNAL.'''
    MESH_INTERNAL = "MESH_INTERNAL"
    '''MESH_INTERNAL.'''


@jsii.data_type(
    jsii_type="ioistionetworking.ServiceEntrySpecPorts",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "number": "number",
        "protocol": "protocol",
        "target_port": "targetPort",
    },
)
class ServiceEntrySpecPorts:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Label assigned to the port.
        :param number: A valid non-negative integer port number.
        :param protocol: The protocol exposed on the port.
        :param target_port: 

        :schema: ServiceEntrySpecPorts
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if number is not None:
            self._values["number"] = number
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Label assigned to the port.

        :schema: ServiceEntrySpecPorts#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''A valid non-negative integer port number.

        :schema: ServiceEntrySpecPorts#number
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol exposed on the port.

        :schema: ServiceEntrySpecPorts#protocol
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: ServiceEntrySpecPorts#targetPort
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEntrySpecPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistionetworking.ServiceEntrySpecResolution")
class ServiceEntrySpecResolution(enum.Enum):
    '''Service discovery mode for the hosts.

    :schema: ServiceEntrySpecResolution
    '''

    NONE = "NONE"
    '''NONE.'''
    STATIC = "STATIC"
    '''STATIC.'''
    DNS = "DNS"
    '''DNS.'''
    DNS_ROUND_ROBIN = "DNS_ROUND_ROBIN"
    '''DNS_ROUND_ROBIN.'''


@jsii.data_type(
    jsii_type="ioistionetworking.ServiceEntrySpecWorkloadSelector",
    jsii_struct_bases=[],
    name_mapping={"labels": "labels"},
)
class ServiceEntrySpecWorkloadSelector:
    def __init__(
        self,
        *,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Applicable only for MESH_INTERNAL services.

        :param labels: 

        :schema: ServiceEntrySpecWorkloadSelector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: ServiceEntrySpecWorkloadSelector#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEntrySpecWorkloadSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Sidecar(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistionetworking.Sidecar",
):
    '''
    :schema: Sidecar
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["SidecarSpec"] = None,
    ) -> None:
        '''Defines a "Sidecar" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: Configuration affecting network reachability of a sidecar. See more details at: https://istio.io/docs/reference/config/networking/sidecar.html
        '''
        props = SidecarProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["SidecarSpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "Sidecar".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: Configuration affecting network reachability of a sidecar. See more details at: https://istio.io/docs/reference/config/networking/sidecar.html
        '''
        props = SidecarProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "Sidecar".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistionetworking.SidecarProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class SidecarProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["SidecarSpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: Configuration affecting network reachability of a sidecar. See more details at: https://istio.io/docs/reference/config/networking/sidecar.html

        :schema: Sidecar
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = SidecarSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: Sidecar#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["SidecarSpec"]:
        '''Configuration affecting network reachability of a sidecar.

        See more details at: https://istio.io/docs/reference/config/networking/sidecar.html

        :schema: Sidecar#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["SidecarSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.SidecarSpec",
    jsii_struct_bases=[],
    name_mapping={
        "egress": "egress",
        "ingress": "ingress",
        "outbound_traffic_policy": "outboundTrafficPolicy",
        "workload_selector": "workloadSelector",
    },
)
class SidecarSpec:
    def __init__(
        self,
        *,
        egress: typing.Optional[typing.Sequence["SidecarSpecEgress"]] = None,
        ingress: typing.Optional[typing.Sequence["SidecarSpecIngress"]] = None,
        outbound_traffic_policy: typing.Optional["SidecarSpecOutboundTrafficPolicy"] = None,
        workload_selector: typing.Optional["SidecarSpecWorkloadSelector"] = None,
    ) -> None:
        '''Configuration affecting network reachability of a sidecar.

        See more details at: https://istio.io/docs/reference/config/networking/sidecar.html

        :param egress: 
        :param ingress: 
        :param outbound_traffic_policy: Configuration for the outbound traffic policy.
        :param workload_selector: 

        :schema: SidecarSpec
        '''
        if isinstance(outbound_traffic_policy, dict):
            outbound_traffic_policy = SidecarSpecOutboundTrafficPolicy(**outbound_traffic_policy)
        if isinstance(workload_selector, dict):
            workload_selector = SidecarSpecWorkloadSelector(**workload_selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if egress is not None:
            self._values["egress"] = egress
        if ingress is not None:
            self._values["ingress"] = ingress
        if outbound_traffic_policy is not None:
            self._values["outbound_traffic_policy"] = outbound_traffic_policy
        if workload_selector is not None:
            self._values["workload_selector"] = workload_selector

    @builtins.property
    def egress(self) -> typing.Optional[typing.List["SidecarSpecEgress"]]:
        '''
        :schema: SidecarSpec#egress
        '''
        result = self._values.get("egress")
        return typing.cast(typing.Optional[typing.List["SidecarSpecEgress"]], result)

    @builtins.property
    def ingress(self) -> typing.Optional[typing.List["SidecarSpecIngress"]]:
        '''
        :schema: SidecarSpec#ingress
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional[typing.List["SidecarSpecIngress"]], result)

    @builtins.property
    def outbound_traffic_policy(
        self,
    ) -> typing.Optional["SidecarSpecOutboundTrafficPolicy"]:
        '''Configuration for the outbound traffic policy.

        :schema: SidecarSpec#outboundTrafficPolicy
        '''
        result = self._values.get("outbound_traffic_policy")
        return typing.cast(typing.Optional["SidecarSpecOutboundTrafficPolicy"], result)

    @builtins.property
    def workload_selector(self) -> typing.Optional["SidecarSpecWorkloadSelector"]:
        '''
        :schema: SidecarSpec#workloadSelector
        '''
        result = self._values.get("workload_selector")
        return typing.cast(typing.Optional["SidecarSpecWorkloadSelector"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.SidecarSpecEgress",
    jsii_struct_bases=[],
    name_mapping={
        "bind": "bind",
        "capture_mode": "captureMode",
        "hosts": "hosts",
        "port": "port",
    },
)
class SidecarSpecEgress:
    def __init__(
        self,
        *,
        bind: typing.Optional[builtins.str] = None,
        capture_mode: typing.Optional["SidecarSpecEgressCaptureMode"] = None,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        port: typing.Optional["SidecarSpecEgressPort"] = None,
    ) -> None:
        '''
        :param bind: 
        :param capture_mode: 
        :param hosts: 
        :param port: The port associated with the listener.

        :schema: SidecarSpecEgress
        '''
        if isinstance(port, dict):
            port = SidecarSpecEgressPort(**port)
        self._values: typing.Dict[str, typing.Any] = {}
        if bind is not None:
            self._values["bind"] = bind
        if capture_mode is not None:
            self._values["capture_mode"] = capture_mode
        if hosts is not None:
            self._values["hosts"] = hosts
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def bind(self) -> typing.Optional[builtins.str]:
        '''
        :schema: SidecarSpecEgress#bind
        '''
        result = self._values.get("bind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capture_mode(self) -> typing.Optional["SidecarSpecEgressCaptureMode"]:
        '''
        :schema: SidecarSpecEgress#captureMode
        '''
        result = self._values.get("capture_mode")
        return typing.cast(typing.Optional["SidecarSpecEgressCaptureMode"], result)

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: SidecarSpecEgress#hosts
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def port(self) -> typing.Optional["SidecarSpecEgressPort"]:
        '''The port associated with the listener.

        :schema: SidecarSpecEgress#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional["SidecarSpecEgressPort"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecEgress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistionetworking.SidecarSpecEgressCaptureMode")
class SidecarSpecEgressCaptureMode(enum.Enum):
    '''
    :schema: SidecarSpecEgressCaptureMode
    '''

    DEFAULT = "DEFAULT"
    '''DEFAULT.'''
    IPTABLES = "IPTABLES"
    '''IPTABLES.'''
    NONE = "NONE"
    '''NONE.'''


@jsii.data_type(
    jsii_type="ioistionetworking.SidecarSpecEgressPort",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "number": "number",
        "protocol": "protocol",
        "target_port": "targetPort",
    },
)
class SidecarSpecEgressPort:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''The port associated with the listener.

        :param name: Label assigned to the port.
        :param number: A valid non-negative integer port number.
        :param protocol: The protocol exposed on the port.
        :param target_port: 

        :schema: SidecarSpecEgressPort
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if number is not None:
            self._values["number"] = number
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Label assigned to the port.

        :schema: SidecarSpecEgressPort#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''A valid non-negative integer port number.

        :schema: SidecarSpecEgressPort#number
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol exposed on the port.

        :schema: SidecarSpecEgressPort#protocol
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: SidecarSpecEgressPort#targetPort
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecEgressPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.SidecarSpecIngress",
    jsii_struct_bases=[],
    name_mapping={
        "bind": "bind",
        "capture_mode": "captureMode",
        "default_endpoint": "defaultEndpoint",
        "port": "port",
        "tls": "tls",
    },
)
class SidecarSpecIngress:
    def __init__(
        self,
        *,
        bind: typing.Optional[builtins.str] = None,
        capture_mode: typing.Optional["SidecarSpecIngressCaptureMode"] = None,
        default_endpoint: typing.Optional[builtins.str] = None,
        port: typing.Optional["SidecarSpecIngressPort"] = None,
        tls: typing.Optional["SidecarSpecIngressTls"] = None,
    ) -> None:
        '''
        :param bind: The IP to which the listener should be bound.
        :param capture_mode: 
        :param default_endpoint: 
        :param port: The port associated with the listener.
        :param tls: 

        :schema: SidecarSpecIngress
        '''
        if isinstance(port, dict):
            port = SidecarSpecIngressPort(**port)
        if isinstance(tls, dict):
            tls = SidecarSpecIngressTls(**tls)
        self._values: typing.Dict[str, typing.Any] = {}
        if bind is not None:
            self._values["bind"] = bind
        if capture_mode is not None:
            self._values["capture_mode"] = capture_mode
        if default_endpoint is not None:
            self._values["default_endpoint"] = default_endpoint
        if port is not None:
            self._values["port"] = port
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def bind(self) -> typing.Optional[builtins.str]:
        '''The IP to which the listener should be bound.

        :schema: SidecarSpecIngress#bind
        '''
        result = self._values.get("bind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capture_mode(self) -> typing.Optional["SidecarSpecIngressCaptureMode"]:
        '''
        :schema: SidecarSpecIngress#captureMode
        '''
        result = self._values.get("capture_mode")
        return typing.cast(typing.Optional["SidecarSpecIngressCaptureMode"], result)

    @builtins.property
    def default_endpoint(self) -> typing.Optional[builtins.str]:
        '''
        :schema: SidecarSpecIngress#defaultEndpoint
        '''
        result = self._values.get("default_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional["SidecarSpecIngressPort"]:
        '''The port associated with the listener.

        :schema: SidecarSpecIngress#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional["SidecarSpecIngressPort"], result)

    @builtins.property
    def tls(self) -> typing.Optional["SidecarSpecIngressTls"]:
        '''
        :schema: SidecarSpecIngress#tls
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["SidecarSpecIngressTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistionetworking.SidecarSpecIngressCaptureMode")
class SidecarSpecIngressCaptureMode(enum.Enum):
    '''
    :schema: SidecarSpecIngressCaptureMode
    '''

    DEFAULT = "DEFAULT"
    '''DEFAULT.'''
    IPTABLES = "IPTABLES"
    '''IPTABLES.'''
    NONE = "NONE"
    '''NONE.'''


@jsii.data_type(
    jsii_type="ioistionetworking.SidecarSpecIngressPort",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "number": "number",
        "protocol": "protocol",
        "target_port": "targetPort",
    },
)
class SidecarSpecIngressPort:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        number: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        target_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''The port associated with the listener.

        :param name: Label assigned to the port.
        :param number: A valid non-negative integer port number.
        :param protocol: The protocol exposed on the port.
        :param target_port: 

        :schema: SidecarSpecIngressPort
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if number is not None:
            self._values["number"] = number
        if protocol is not None:
            self._values["protocol"] = protocol
        if target_port is not None:
            self._values["target_port"] = target_port

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Label assigned to the port.

        :schema: SidecarSpecIngressPort#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''A valid non-negative integer port number.

        :schema: SidecarSpecIngressPort#number
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol exposed on the port.

        :schema: SidecarSpecIngressPort#protocol
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: SidecarSpecIngressPort#targetPort
        '''
        result = self._values.get("target_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecIngressPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.SidecarSpecIngressTls",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificates": "caCertificates",
        "cipher_suites": "cipherSuites",
        "credential_name": "credentialName",
        "https_redirect": "httpsRedirect",
        "max_protocol_version": "maxProtocolVersion",
        "min_protocol_version": "minProtocolVersion",
        "mode": "mode",
        "private_key": "privateKey",
        "server_certificate": "serverCertificate",
        "subject_alt_names": "subjectAltNames",
        "verify_certificate_hash": "verifyCertificateHash",
        "verify_certificate_spki": "verifyCertificateSpki",
    },
)
class SidecarSpecIngressTls:
    def __init__(
        self,
        *,
        ca_certificates: typing.Optional[builtins.str] = None,
        cipher_suites: typing.Optional[typing.Sequence[builtins.str]] = None,
        credential_name: typing.Optional[builtins.str] = None,
        https_redirect: typing.Optional[builtins.bool] = None,
        max_protocol_version: typing.Optional["SidecarSpecIngressTlsMaxProtocolVersion"] = None,
        min_protocol_version: typing.Optional["SidecarSpecIngressTlsMinProtocolVersion"] = None,
        mode: typing.Optional["SidecarSpecIngressTlsMode"] = None,
        private_key: typing.Optional[builtins.str] = None,
        server_certificate: typing.Optional[builtins.str] = None,
        subject_alt_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        verify_certificate_hash: typing.Optional[typing.Sequence[builtins.str]] = None,
        verify_certificate_spki: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param ca_certificates: REQUIRED if mode is ``MUTUAL``.
        :param cipher_suites: Optional: If specified, only support the specified cipher list.
        :param credential_name: 
        :param https_redirect: 
        :param max_protocol_version: Optional: Maximum TLS protocol version.
        :param min_protocol_version: Optional: Minimum TLS protocol version.
        :param mode: 
        :param private_key: REQUIRED if mode is ``SIMPLE`` or ``MUTUAL``.
        :param server_certificate: REQUIRED if mode is ``SIMPLE`` or ``MUTUAL``.
        :param subject_alt_names: 
        :param verify_certificate_hash: 
        :param verify_certificate_spki: 

        :schema: SidecarSpecIngressTls
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ca_certificates is not None:
            self._values["ca_certificates"] = ca_certificates
        if cipher_suites is not None:
            self._values["cipher_suites"] = cipher_suites
        if credential_name is not None:
            self._values["credential_name"] = credential_name
        if https_redirect is not None:
            self._values["https_redirect"] = https_redirect
        if max_protocol_version is not None:
            self._values["max_protocol_version"] = max_protocol_version
        if min_protocol_version is not None:
            self._values["min_protocol_version"] = min_protocol_version
        if mode is not None:
            self._values["mode"] = mode
        if private_key is not None:
            self._values["private_key"] = private_key
        if server_certificate is not None:
            self._values["server_certificate"] = server_certificate
        if subject_alt_names is not None:
            self._values["subject_alt_names"] = subject_alt_names
        if verify_certificate_hash is not None:
            self._values["verify_certificate_hash"] = verify_certificate_hash
        if verify_certificate_spki is not None:
            self._values["verify_certificate_spki"] = verify_certificate_spki

    @builtins.property
    def ca_certificates(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``MUTUAL``.

        :schema: SidecarSpecIngressTls#caCertificates
        '''
        result = self._values.get("ca_certificates")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cipher_suites(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional: If specified, only support the specified cipher list.

        :schema: SidecarSpecIngressTls#cipherSuites
        '''
        result = self._values.get("cipher_suites")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def credential_name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: SidecarSpecIngressTls#credentialName
        '''
        result = self._values.get("credential_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def https_redirect(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: SidecarSpecIngressTls#httpsRedirect
        '''
        result = self._values.get("https_redirect")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def max_protocol_version(
        self,
    ) -> typing.Optional["SidecarSpecIngressTlsMaxProtocolVersion"]:
        '''Optional: Maximum TLS protocol version.

        :schema: SidecarSpecIngressTls#maxProtocolVersion
        '''
        result = self._values.get("max_protocol_version")
        return typing.cast(typing.Optional["SidecarSpecIngressTlsMaxProtocolVersion"], result)

    @builtins.property
    def min_protocol_version(
        self,
    ) -> typing.Optional["SidecarSpecIngressTlsMinProtocolVersion"]:
        '''Optional: Minimum TLS protocol version.

        :schema: SidecarSpecIngressTls#minProtocolVersion
        '''
        result = self._values.get("min_protocol_version")
        return typing.cast(typing.Optional["SidecarSpecIngressTlsMinProtocolVersion"], result)

    @builtins.property
    def mode(self) -> typing.Optional["SidecarSpecIngressTlsMode"]:
        '''
        :schema: SidecarSpecIngressTls#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["SidecarSpecIngressTlsMode"], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``SIMPLE`` or ``MUTUAL``.

        :schema: SidecarSpecIngressTls#privateKey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_certificate(self) -> typing.Optional[builtins.str]:
        '''REQUIRED if mode is ``SIMPLE`` or ``MUTUAL``.

        :schema: SidecarSpecIngressTls#serverCertificate
        '''
        result = self._values.get("server_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_alt_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: SidecarSpecIngressTls#subjectAltNames
        '''
        result = self._values.get("subject_alt_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def verify_certificate_hash(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: SidecarSpecIngressTls#verifyCertificateHash
        '''
        result = self._values.get("verify_certificate_hash")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def verify_certificate_spki(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: SidecarSpecIngressTls#verifyCertificateSpki
        '''
        result = self._values.get("verify_certificate_spki")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecIngressTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistionetworking.SidecarSpecIngressTlsMaxProtocolVersion")
class SidecarSpecIngressTlsMaxProtocolVersion(enum.Enum):
    '''Optional: Maximum TLS protocol version.

    :schema: SidecarSpecIngressTlsMaxProtocolVersion
    '''

    TLS_AUTO = "TLS_AUTO"
    '''TLS_AUTO.'''
    TLSV1_0 = "TLSV1_0"
    '''TLSV1_0.'''
    TLSV1_1 = "TLSV1_1"
    '''TLSV1_1.'''
    TLSV1_2 = "TLSV1_2"
    '''TLSV1_2.'''
    TLSV1_3 = "TLSV1_3"
    '''TLSV1_3.'''


@jsii.enum(jsii_type="ioistionetworking.SidecarSpecIngressTlsMinProtocolVersion")
class SidecarSpecIngressTlsMinProtocolVersion(enum.Enum):
    '''Optional: Minimum TLS protocol version.

    :schema: SidecarSpecIngressTlsMinProtocolVersion
    '''

    TLS_AUTO = "TLS_AUTO"
    '''TLS_AUTO.'''
    TLSV1_0 = "TLSV1_0"
    '''TLSV1_0.'''
    TLSV1_1 = "TLSV1_1"
    '''TLSV1_1.'''
    TLSV1_2 = "TLSV1_2"
    '''TLSV1_2.'''
    TLSV1_3 = "TLSV1_3"
    '''TLSV1_3.'''


@jsii.enum(jsii_type="ioistionetworking.SidecarSpecIngressTlsMode")
class SidecarSpecIngressTlsMode(enum.Enum):
    '''
    :schema: SidecarSpecIngressTlsMode
    '''

    PASSTHROUGH = "PASSTHROUGH"
    '''PASSTHROUGH.'''
    SIMPLE = "SIMPLE"
    '''SIMPLE.'''
    MUTUAL = "MUTUAL"
    '''MUTUAL.'''
    AUTO_PASSTHROUGH = "AUTO_PASSTHROUGH"
    '''AUTO_PASSTHROUGH.'''
    ISTIO_MUTUAL = "ISTIO_MUTUAL"
    '''ISTIO_MUTUAL.'''


@jsii.data_type(
    jsii_type="ioistionetworking.SidecarSpecOutboundTrafficPolicy",
    jsii_struct_bases=[],
    name_mapping={"egress_proxy": "egressProxy", "mode": "mode"},
)
class SidecarSpecOutboundTrafficPolicy:
    def __init__(
        self,
        *,
        egress_proxy: typing.Optional["SidecarSpecOutboundTrafficPolicyEgressProxy"] = None,
        mode: typing.Optional["SidecarSpecOutboundTrafficPolicyMode"] = None,
    ) -> None:
        '''Configuration for the outbound traffic policy.

        :param egress_proxy: 
        :param mode: 

        :schema: SidecarSpecOutboundTrafficPolicy
        '''
        if isinstance(egress_proxy, dict):
            egress_proxy = SidecarSpecOutboundTrafficPolicyEgressProxy(**egress_proxy)
        self._values: typing.Dict[str, typing.Any] = {}
        if egress_proxy is not None:
            self._values["egress_proxy"] = egress_proxy
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def egress_proxy(
        self,
    ) -> typing.Optional["SidecarSpecOutboundTrafficPolicyEgressProxy"]:
        '''
        :schema: SidecarSpecOutboundTrafficPolicy#egressProxy
        '''
        result = self._values.get("egress_proxy")
        return typing.cast(typing.Optional["SidecarSpecOutboundTrafficPolicyEgressProxy"], result)

    @builtins.property
    def mode(self) -> typing.Optional["SidecarSpecOutboundTrafficPolicyMode"]:
        '''
        :schema: SidecarSpecOutboundTrafficPolicy#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["SidecarSpecOutboundTrafficPolicyMode"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecOutboundTrafficPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.SidecarSpecOutboundTrafficPolicyEgressProxy",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port", "subset": "subset"},
)
class SidecarSpecOutboundTrafficPolicyEgressProxy:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional["SidecarSpecOutboundTrafficPolicyEgressProxyPort"] = None,
        subset: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: The name of a service from the service registry.
        :param port: Specifies the port on the host that is being addressed.
        :param subset: The name of a subset within the service.

        :schema: SidecarSpecOutboundTrafficPolicyEgressProxy
        '''
        if isinstance(port, dict):
            port = SidecarSpecOutboundTrafficPolicyEgressProxyPort(**port)
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port
        if subset is not None:
            self._values["subset"] = subset

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The name of a service from the service registry.

        :schema: SidecarSpecOutboundTrafficPolicyEgressProxy#host
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(
        self,
    ) -> typing.Optional["SidecarSpecOutboundTrafficPolicyEgressProxyPort"]:
        '''Specifies the port on the host that is being addressed.

        :schema: SidecarSpecOutboundTrafficPolicyEgressProxy#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional["SidecarSpecOutboundTrafficPolicyEgressProxyPort"], result)

    @builtins.property
    def subset(self) -> typing.Optional[builtins.str]:
        '''The name of a subset within the service.

        :schema: SidecarSpecOutboundTrafficPolicyEgressProxy#subset
        '''
        result = self._values.get("subset")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecOutboundTrafficPolicyEgressProxy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.SidecarSpecOutboundTrafficPolicyEgressProxyPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class SidecarSpecOutboundTrafficPolicyEgressProxyPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        '''Specifies the port on the host that is being addressed.

        :param number: 

        :schema: SidecarSpecOutboundTrafficPolicyEgressProxyPort
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: SidecarSpecOutboundTrafficPolicyEgressProxyPort#number
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecOutboundTrafficPolicyEgressProxyPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistionetworking.SidecarSpecOutboundTrafficPolicyMode")
class SidecarSpecOutboundTrafficPolicyMode(enum.Enum):
    '''
    :schema: SidecarSpecOutboundTrafficPolicyMode
    '''

    REGISTRY_ONLY = "REGISTRY_ONLY"
    '''REGISTRY_ONLY.'''
    ALLOW_ANY = "ALLOW_ANY"
    '''ALLOW_ANY.'''


@jsii.data_type(
    jsii_type="ioistionetworking.SidecarSpecWorkloadSelector",
    jsii_struct_bases=[],
    name_mapping={"labels": "labels"},
)
class SidecarSpecWorkloadSelector:
    def __init__(
        self,
        *,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param labels: 

        :schema: SidecarSpecWorkloadSelector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: SidecarSpecWorkloadSelector#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SidecarSpecWorkloadSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualService(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistionetworking.VirtualService",
):
    '''
    :schema: VirtualService
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["VirtualServiceSpec"] = None,
    ) -> None:
        '''Defines a "VirtualService" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: Configuration affecting label/content routing, sni routing, etc. See more details at: https://istio.io/docs/reference/config/networking/virtual-service.html
        '''
        props = VirtualServiceProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["VirtualServiceSpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "VirtualService".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: Configuration affecting label/content routing, sni routing, etc. See more details at: https://istio.io/docs/reference/config/networking/virtual-service.html
        '''
        props = VirtualServiceProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "VirtualService".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class VirtualServiceProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["VirtualServiceSpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: Configuration affecting label/content routing, sni routing, etc. See more details at: https://istio.io/docs/reference/config/networking/virtual-service.html

        :schema: VirtualService
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = VirtualServiceSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: VirtualService#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["VirtualServiceSpec"]:
        '''Configuration affecting label/content routing, sni routing, etc.

        See more details at: https://istio.io/docs/reference/config/networking/virtual-service.html

        :schema: VirtualService#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["VirtualServiceSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "export_to": "exportTo",
        "gateways": "gateways",
        "hosts": "hosts",
        "http": "http",
        "tcp": "tcp",
        "tls": "tls",
    },
)
class VirtualServiceSpec:
    def __init__(
        self,
        *,
        export_to: typing.Optional[typing.Sequence[builtins.str]] = None,
        gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        http: typing.Optional[typing.Sequence["VirtualServiceSpecHttp"]] = None,
        tcp: typing.Optional[typing.Sequence["VirtualServiceSpecTcp"]] = None,
        tls: typing.Optional[typing.Sequence["VirtualServiceSpecTls"]] = None,
    ) -> None:
        '''Configuration affecting label/content routing, sni routing, etc.

        See more details at: https://istio.io/docs/reference/config/networking/virtual-service.html

        :param export_to: A list of namespaces to which this virtual service is exported.
        :param gateways: The names of gateways and sidecars that should apply these routes.
        :param hosts: The destination hosts to which traffic is being sent.
        :param http: An ordered list of route rules for HTTP traffic.
        :param tcp: An ordered list of route rules for opaque TCP traffic.
        :param tls: 

        :schema: VirtualServiceSpec
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if export_to is not None:
            self._values["export_to"] = export_to
        if gateways is not None:
            self._values["gateways"] = gateways
        if hosts is not None:
            self._values["hosts"] = hosts
        if http is not None:
            self._values["http"] = http
        if tcp is not None:
            self._values["tcp"] = tcp
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def export_to(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of namespaces to which this virtual service is exported.

        :schema: VirtualServiceSpec#exportTo
        '''
        result = self._values.get("export_to")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def gateways(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The names of gateways and sidecars that should apply these routes.

        :schema: VirtualServiceSpec#gateways
        '''
        result = self._values.get("gateways")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The destination hosts to which traffic is being sent.

        :schema: VirtualServiceSpec#hosts
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def http(self) -> typing.Optional[typing.List["VirtualServiceSpecHttp"]]:
        '''An ordered list of route rules for HTTP traffic.

        :schema: VirtualServiceSpec#http
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional[typing.List["VirtualServiceSpecHttp"]], result)

    @builtins.property
    def tcp(self) -> typing.Optional[typing.List["VirtualServiceSpecTcp"]]:
        '''An ordered list of route rules for opaque TCP traffic.

        :schema: VirtualServiceSpec#tcp
        '''
        result = self._values.get("tcp")
        return typing.cast(typing.Optional[typing.List["VirtualServiceSpecTcp"]], result)

    @builtins.property
    def tls(self) -> typing.Optional[typing.List["VirtualServiceSpecTls"]]:
        '''
        :schema: VirtualServiceSpec#tls
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.List["VirtualServiceSpecTls"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttp",
    jsii_struct_bases=[],
    name_mapping={
        "cors_policy": "corsPolicy",
        "delegate": "delegate",
        "fault": "fault",
        "headers": "headers",
        "match": "match",
        "mirror": "mirror",
        "mirror_percent": "mirrorPercent",
        "mirror_percentage": "mirrorPercentage",
        "name": "name",
        "redirect": "redirect",
        "retries": "retries",
        "rewrite": "rewrite",
        "route": "route",
        "timeout": "timeout",
    },
)
class VirtualServiceSpecHttp:
    def __init__(
        self,
        *,
        cors_policy: typing.Optional["VirtualServiceSpecHttpCorsPolicy"] = None,
        delegate: typing.Optional["VirtualServiceSpecHttpDelegate"] = None,
        fault: typing.Optional["VirtualServiceSpecHttpFault"] = None,
        headers: typing.Optional["VirtualServiceSpecHttpHeaders"] = None,
        match: typing.Optional[typing.Sequence["VirtualServiceSpecHttpMatch"]] = None,
        mirror: typing.Optional["VirtualServiceSpecHttpMirror"] = None,
        mirror_percent: typing.Optional[jsii.Number] = None,
        mirror_percentage: typing.Optional["VirtualServiceSpecHttpMirrorPercentage"] = None,
        name: typing.Optional[builtins.str] = None,
        redirect: typing.Optional["VirtualServiceSpecHttpRedirect"] = None,
        retries: typing.Optional["VirtualServiceSpecHttpRetries"] = None,
        rewrite: typing.Optional["VirtualServiceSpecHttpRewrite"] = None,
        route: typing.Optional[typing.Sequence["VirtualServiceSpecHttpRoute"]] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cors_policy: Cross-Origin Resource Sharing policy (CORS).
        :param delegate: 
        :param fault: Fault injection policy to apply on HTTP traffic at the client side.
        :param headers: 
        :param match: 
        :param mirror: 
        :param mirror_percent: Percentage of the traffic to be mirrored by the ``mirror`` field.
        :param mirror_percentage: Percentage of the traffic to be mirrored by the ``mirror`` field.
        :param name: The name assigned to the route for debugging purposes.
        :param redirect: A HTTP rule can either redirect or forward (default) traffic.
        :param retries: Retry policy for HTTP requests.
        :param rewrite: Rewrite HTTP URIs and Authority headers.
        :param route: A HTTP rule can either redirect or forward (default) traffic.
        :param timeout: Timeout for HTTP requests, default is disabled.

        :schema: VirtualServiceSpecHttp
        '''
        if isinstance(cors_policy, dict):
            cors_policy = VirtualServiceSpecHttpCorsPolicy(**cors_policy)
        if isinstance(delegate, dict):
            delegate = VirtualServiceSpecHttpDelegate(**delegate)
        if isinstance(fault, dict):
            fault = VirtualServiceSpecHttpFault(**fault)
        if isinstance(headers, dict):
            headers = VirtualServiceSpecHttpHeaders(**headers)
        if isinstance(mirror, dict):
            mirror = VirtualServiceSpecHttpMirror(**mirror)
        if isinstance(mirror_percentage, dict):
            mirror_percentage = VirtualServiceSpecHttpMirrorPercentage(**mirror_percentage)
        if isinstance(redirect, dict):
            redirect = VirtualServiceSpecHttpRedirect(**redirect)
        if isinstance(retries, dict):
            retries = VirtualServiceSpecHttpRetries(**retries)
        if isinstance(rewrite, dict):
            rewrite = VirtualServiceSpecHttpRewrite(**rewrite)
        self._values: typing.Dict[str, typing.Any] = {}
        if cors_policy is not None:
            self._values["cors_policy"] = cors_policy
        if delegate is not None:
            self._values["delegate"] = delegate
        if fault is not None:
            self._values["fault"] = fault
        if headers is not None:
            self._values["headers"] = headers
        if match is not None:
            self._values["match"] = match
        if mirror is not None:
            self._values["mirror"] = mirror
        if mirror_percent is not None:
            self._values["mirror_percent"] = mirror_percent
        if mirror_percentage is not None:
            self._values["mirror_percentage"] = mirror_percentage
        if name is not None:
            self._values["name"] = name
        if redirect is not None:
            self._values["redirect"] = redirect
        if retries is not None:
            self._values["retries"] = retries
        if rewrite is not None:
            self._values["rewrite"] = rewrite
        if route is not None:
            self._values["route"] = route
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def cors_policy(self) -> typing.Optional["VirtualServiceSpecHttpCorsPolicy"]:
        '''Cross-Origin Resource Sharing policy (CORS).

        :schema: VirtualServiceSpecHttp#corsPolicy
        '''
        result = self._values.get("cors_policy")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpCorsPolicy"], result)

    @builtins.property
    def delegate(self) -> typing.Optional["VirtualServiceSpecHttpDelegate"]:
        '''
        :schema: VirtualServiceSpecHttp#delegate
        '''
        result = self._values.get("delegate")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpDelegate"], result)

    @builtins.property
    def fault(self) -> typing.Optional["VirtualServiceSpecHttpFault"]:
        '''Fault injection policy to apply on HTTP traffic at the client side.

        :schema: VirtualServiceSpecHttp#fault
        '''
        result = self._values.get("fault")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpFault"], result)

    @builtins.property
    def headers(self) -> typing.Optional["VirtualServiceSpecHttpHeaders"]:
        '''
        :schema: VirtualServiceSpecHttp#headers
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpHeaders"], result)

    @builtins.property
    def match(self) -> typing.Optional[typing.List["VirtualServiceSpecHttpMatch"]]:
        '''
        :schema: VirtualServiceSpecHttp#match
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional[typing.List["VirtualServiceSpecHttpMatch"]], result)

    @builtins.property
    def mirror(self) -> typing.Optional["VirtualServiceSpecHttpMirror"]:
        '''
        :schema: VirtualServiceSpecHttp#mirror
        '''
        result = self._values.get("mirror")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpMirror"], result)

    @builtins.property
    def mirror_percent(self) -> typing.Optional[jsii.Number]:
        '''Percentage of the traffic to be mirrored by the ``mirror`` field.

        :schema: VirtualServiceSpecHttp#mirrorPercent
        '''
        result = self._values.get("mirror_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def mirror_percentage(
        self,
    ) -> typing.Optional["VirtualServiceSpecHttpMirrorPercentage"]:
        '''Percentage of the traffic to be mirrored by the ``mirror`` field.

        :schema: VirtualServiceSpecHttp#mirrorPercentage
        '''
        result = self._values.get("mirror_percentage")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpMirrorPercentage"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name assigned to the route for debugging purposes.

        :schema: VirtualServiceSpecHttp#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect(self) -> typing.Optional["VirtualServiceSpecHttpRedirect"]:
        '''A HTTP rule can either redirect or forward (default) traffic.

        :schema: VirtualServiceSpecHttp#redirect
        '''
        result = self._values.get("redirect")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpRedirect"], result)

    @builtins.property
    def retries(self) -> typing.Optional["VirtualServiceSpecHttpRetries"]:
        '''Retry policy for HTTP requests.

        :schema: VirtualServiceSpecHttp#retries
        '''
        result = self._values.get("retries")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpRetries"], result)

    @builtins.property
    def rewrite(self) -> typing.Optional["VirtualServiceSpecHttpRewrite"]:
        '''Rewrite HTTP URIs and Authority headers.

        :schema: VirtualServiceSpecHttp#rewrite
        '''
        result = self._values.get("rewrite")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpRewrite"], result)

    @builtins.property
    def route(self) -> typing.Optional[typing.List["VirtualServiceSpecHttpRoute"]]:
        '''A HTTP rule can either redirect or forward (default) traffic.

        :schema: VirtualServiceSpecHttp#route
        '''
        result = self._values.get("route")
        return typing.cast(typing.Optional[typing.List["VirtualServiceSpecHttpRoute"]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Timeout for HTTP requests, default is disabled.

        :schema: VirtualServiceSpecHttp#timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpCorsPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "allow_credentials": "allowCredentials",
        "allow_headers": "allowHeaders",
        "allow_methods": "allowMethods",
        "allow_origin": "allowOrigin",
        "allow_origins": "allowOrigins",
        "expose_headers": "exposeHeaders",
        "max_age": "maxAge",
    },
)
class VirtualServiceSpecHttpCorsPolicy:
    def __init__(
        self,
        *,
        allow_credentials: typing.Optional[builtins.bool] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origin: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Sequence["VirtualServiceSpecHttpCorsPolicyAllowOrigins"]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Cross-Origin Resource Sharing policy (CORS).

        :param allow_credentials: 
        :param allow_headers: 
        :param allow_methods: List of HTTP methods allowed to access the resource.
        :param allow_origin: The list of origins that are allowed to perform CORS requests.
        :param allow_origins: String patterns that match allowed origins.
        :param expose_headers: 
        :param max_age: 

        :schema: VirtualServiceSpecHttpCorsPolicy
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_credentials is not None:
            self._values["allow_credentials"] = allow_credentials
        if allow_headers is not None:
            self._values["allow_headers"] = allow_headers
        if allow_methods is not None:
            self._values["allow_methods"] = allow_methods
        if allow_origin is not None:
            self._values["allow_origin"] = allow_origin
        if allow_origins is not None:
            self._values["allow_origins"] = allow_origins
        if expose_headers is not None:
            self._values["expose_headers"] = expose_headers
        if max_age is not None:
            self._values["max_age"] = max_age

    @builtins.property
    def allow_credentials(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: VirtualServiceSpecHttpCorsPolicy#allowCredentials
        '''
        result = self._values.get("allow_credentials")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def allow_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpCorsPolicy#allowHeaders
        '''
        result = self._values.get("allow_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of HTTP methods allowed to access the resource.

        :schema: VirtualServiceSpecHttpCorsPolicy#allowMethods
        '''
        result = self._values.get("allow_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_origin(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of origins that are allowed to perform CORS requests.

        :schema: VirtualServiceSpecHttpCorsPolicy#allowOrigin
        '''
        result = self._values.get("allow_origin")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_origins(
        self,
    ) -> typing.Optional[typing.List["VirtualServiceSpecHttpCorsPolicyAllowOrigins"]]:
        '''String patterns that match allowed origins.

        :schema: VirtualServiceSpecHttpCorsPolicy#allowOrigins
        '''
        result = self._values.get("allow_origins")
        return typing.cast(typing.Optional[typing.List["VirtualServiceSpecHttpCorsPolicyAllowOrigins"]], result)

    @builtins.property
    def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpCorsPolicy#exposeHeaders
        '''
        result = self._values.get("expose_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_age(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpCorsPolicy#maxAge
        '''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpCorsPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpCorsPolicyAllowOrigins",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpCorsPolicyAllowOrigins:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpCorsPolicyAllowOrigins
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpCorsPolicyAllowOrigins#exact
        '''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpCorsPolicyAllowOrigins#prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpCorsPolicyAllowOrigins#regex
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpCorsPolicyAllowOrigins(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpDelegate",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class VirtualServiceSpecHttpDelegate:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name specifies the name of the delegate VirtualService.
        :param namespace: Namespace specifies the namespace where the delegate VirtualService resides.

        :schema: VirtualServiceSpecHttpDelegate
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name specifies the name of the delegate VirtualService.

        :schema: VirtualServiceSpecHttpDelegate#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace specifies the namespace where the delegate VirtualService resides.

        :schema: VirtualServiceSpecHttpDelegate#namespace
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpDelegate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpFault",
    jsii_struct_bases=[],
    name_mapping={"abort": "abort", "delay": "delay"},
)
class VirtualServiceSpecHttpFault:
    def __init__(
        self,
        *,
        abort: typing.Optional["VirtualServiceSpecHttpFaultAbort"] = None,
        delay: typing.Optional["VirtualServiceSpecHttpFaultDelay"] = None,
    ) -> None:
        '''Fault injection policy to apply on HTTP traffic at the client side.

        :param abort: 
        :param delay: 

        :schema: VirtualServiceSpecHttpFault
        '''
        if isinstance(abort, dict):
            abort = VirtualServiceSpecHttpFaultAbort(**abort)
        if isinstance(delay, dict):
            delay = VirtualServiceSpecHttpFaultDelay(**delay)
        self._values: typing.Dict[str, typing.Any] = {}
        if abort is not None:
            self._values["abort"] = abort
        if delay is not None:
            self._values["delay"] = delay

    @builtins.property
    def abort(self) -> typing.Optional["VirtualServiceSpecHttpFaultAbort"]:
        '''
        :schema: VirtualServiceSpecHttpFault#abort
        '''
        result = self._values.get("abort")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpFaultAbort"], result)

    @builtins.property
    def delay(self) -> typing.Optional["VirtualServiceSpecHttpFaultDelay"]:
        '''
        :schema: VirtualServiceSpecHttpFault#delay
        '''
        result = self._values.get("delay")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpFaultDelay"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpFault(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpFaultAbort",
    jsii_struct_bases=[],
    name_mapping={
        "grpc_status": "grpcStatus",
        "http2_error": "http2Error",
        "http_status": "httpStatus",
        "percentage": "percentage",
    },
)
class VirtualServiceSpecHttpFaultAbort:
    def __init__(
        self,
        *,
        grpc_status: typing.Optional[builtins.str] = None,
        http2_error: typing.Optional[builtins.str] = None,
        http_status: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional["VirtualServiceSpecHttpFaultAbortPercentage"] = None,
    ) -> None:
        '''
        :param grpc_status: GRPC status code to use to abort the request.
        :param http2_error: 
        :param http_status: HTTP status code to use to abort the Http request.
        :param percentage: Percentage of requests to be aborted with the error code provided.

        :schema: VirtualServiceSpecHttpFaultAbort
        '''
        if isinstance(percentage, dict):
            percentage = VirtualServiceSpecHttpFaultAbortPercentage(**percentage)
        self._values: typing.Dict[str, typing.Any] = {}
        if grpc_status is not None:
            self._values["grpc_status"] = grpc_status
        if http2_error is not None:
            self._values["http2_error"] = http2_error
        if http_status is not None:
            self._values["http_status"] = http_status
        if percentage is not None:
            self._values["percentage"] = percentage

    @builtins.property
    def grpc_status(self) -> typing.Optional[builtins.str]:
        '''GRPC status code to use to abort the request.

        :schema: VirtualServiceSpecHttpFaultAbort#grpcStatus
        '''
        result = self._values.get("grpc_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http2_error(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpFaultAbort#http2Error
        '''
        result = self._values.get("http2_error")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_status(self) -> typing.Optional[jsii.Number]:
        '''HTTP status code to use to abort the Http request.

        :schema: VirtualServiceSpecHttpFaultAbort#httpStatus
        '''
        result = self._values.get("http_status")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percentage(
        self,
    ) -> typing.Optional["VirtualServiceSpecHttpFaultAbortPercentage"]:
        '''Percentage of requests to be aborted with the error code provided.

        :schema: VirtualServiceSpecHttpFaultAbort#percentage
        '''
        result = self._values.get("percentage")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpFaultAbortPercentage"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpFaultAbort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpFaultAbortPercentage",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class VirtualServiceSpecHttpFaultAbortPercentage:
    def __init__(self, *, value: typing.Optional[jsii.Number] = None) -> None:
        '''Percentage of requests to be aborted with the error code provided.

        :param value: 

        :schema: VirtualServiceSpecHttpFaultAbortPercentage
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VirtualServiceSpecHttpFaultAbortPercentage#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpFaultAbortPercentage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpFaultDelay",
    jsii_struct_bases=[],
    name_mapping={
        "exponential_delay": "exponentialDelay",
        "fixed_delay": "fixedDelay",
        "percent": "percent",
        "percentage": "percentage",
    },
)
class VirtualServiceSpecHttpFaultDelay:
    def __init__(
        self,
        *,
        exponential_delay: typing.Optional[builtins.str] = None,
        fixed_delay: typing.Optional[builtins.str] = None,
        percent: typing.Optional[jsii.Number] = None,
        percentage: typing.Optional["VirtualServiceSpecHttpFaultDelayPercentage"] = None,
    ) -> None:
        '''
        :param exponential_delay: 
        :param fixed_delay: Add a fixed delay before forwarding the request.
        :param percent: Percentage of requests on which the delay will be injected (0-100).
        :param percentage: Percentage of requests on which the delay will be injected.

        :schema: VirtualServiceSpecHttpFaultDelay
        '''
        if isinstance(percentage, dict):
            percentage = VirtualServiceSpecHttpFaultDelayPercentage(**percentage)
        self._values: typing.Dict[str, typing.Any] = {}
        if exponential_delay is not None:
            self._values["exponential_delay"] = exponential_delay
        if fixed_delay is not None:
            self._values["fixed_delay"] = fixed_delay
        if percent is not None:
            self._values["percent"] = percent
        if percentage is not None:
            self._values["percentage"] = percentage

    @builtins.property
    def exponential_delay(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpFaultDelay#exponentialDelay
        '''
        result = self._values.get("exponential_delay")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fixed_delay(self) -> typing.Optional[builtins.str]:
        '''Add a fixed delay before forwarding the request.

        :schema: VirtualServiceSpecHttpFaultDelay#fixedDelay
        '''
        result = self._values.get("fixed_delay")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def percent(self) -> typing.Optional[jsii.Number]:
        '''Percentage of requests on which the delay will be injected (0-100).

        :schema: VirtualServiceSpecHttpFaultDelay#percent
        '''
        result = self._values.get("percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def percentage(
        self,
    ) -> typing.Optional["VirtualServiceSpecHttpFaultDelayPercentage"]:
        '''Percentage of requests on which the delay will be injected.

        :schema: VirtualServiceSpecHttpFaultDelay#percentage
        '''
        result = self._values.get("percentage")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpFaultDelayPercentage"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpFaultDelay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpFaultDelayPercentage",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class VirtualServiceSpecHttpFaultDelayPercentage:
    def __init__(self, *, value: typing.Optional[jsii.Number] = None) -> None:
        '''Percentage of requests on which the delay will be injected.

        :param value: 

        :schema: VirtualServiceSpecHttpFaultDelayPercentage
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VirtualServiceSpecHttpFaultDelayPercentage#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpFaultDelayPercentage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpHeaders",
    jsii_struct_bases=[],
    name_mapping={"request": "request", "response": "response"},
)
class VirtualServiceSpecHttpHeaders:
    def __init__(
        self,
        *,
        request: typing.Optional["VirtualServiceSpecHttpHeadersRequest"] = None,
        response: typing.Optional["VirtualServiceSpecHttpHeadersResponse"] = None,
    ) -> None:
        '''
        :param request: 
        :param response: 

        :schema: VirtualServiceSpecHttpHeaders
        '''
        if isinstance(request, dict):
            request = VirtualServiceSpecHttpHeadersRequest(**request)
        if isinstance(response, dict):
            response = VirtualServiceSpecHttpHeadersResponse(**response)
        self._values: typing.Dict[str, typing.Any] = {}
        if request is not None:
            self._values["request"] = request
        if response is not None:
            self._values["response"] = response

    @builtins.property
    def request(self) -> typing.Optional["VirtualServiceSpecHttpHeadersRequest"]:
        '''
        :schema: VirtualServiceSpecHttpHeaders#request
        '''
        result = self._values.get("request")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpHeadersRequest"], result)

    @builtins.property
    def response(self) -> typing.Optional["VirtualServiceSpecHttpHeadersResponse"]:
        '''
        :schema: VirtualServiceSpecHttpHeaders#response
        '''
        result = self._values.get("response")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpHeadersResponse"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpHeadersRequest",
    jsii_struct_bases=[],
    name_mapping={"add": "add", "remove": "remove", "set": "set"},
)
class VirtualServiceSpecHttpHeadersRequest:
    def __init__(
        self,
        *,
        add: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        set: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param add: 
        :param remove: 
        :param set: 

        :schema: VirtualServiceSpecHttpHeadersRequest
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if add is not None:
            self._values["add"] = add
        if remove is not None:
            self._values["remove"] = remove
        if set is not None:
            self._values["set"] = set

    @builtins.property
    def add(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpHeadersRequest#add
        '''
        result = self._values.get("add")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpHeadersRequest#remove
        '''
        result = self._values.get("remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def set(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpHeadersRequest#set
        '''
        result = self._values.get("set")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpHeadersRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpHeadersResponse",
    jsii_struct_bases=[],
    name_mapping={"add": "add", "remove": "remove", "set": "set"},
)
class VirtualServiceSpecHttpHeadersResponse:
    def __init__(
        self,
        *,
        add: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        set: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param add: 
        :param remove: 
        :param set: 

        :schema: VirtualServiceSpecHttpHeadersResponse
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if add is not None:
            self._values["add"] = add
        if remove is not None:
            self._values["remove"] = remove
        if set is not None:
            self._values["set"] = set

    @builtins.property
    def add(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpHeadersResponse#add
        '''
        result = self._values.get("add")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpHeadersResponse#remove
        '''
        result = self._values.get("remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def set(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpHeadersResponse#set
        '''
        result = self._values.get("set")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpHeadersResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpMatch",
    jsii_struct_bases=[],
    name_mapping={
        "authority": "authority",
        "gateways": "gateways",
        "headers": "headers",
        "ignore_uri_case": "ignoreUriCase",
        "method": "method",
        "name": "name",
        "port": "port",
        "query_params": "queryParams",
        "scheme": "scheme",
        "source_labels": "sourceLabels",
        "source_namespace": "sourceNamespace",
        "uri": "uri",
        "without_headers": "withoutHeaders",
    },
)
class VirtualServiceSpecHttpMatch:
    def __init__(
        self,
        *,
        authority: typing.Optional["VirtualServiceSpecHttpMatchAuthority"] = None,
        gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
        headers: typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchHeaders"]] = None,
        ignore_uri_case: typing.Optional[builtins.bool] = None,
        method: typing.Optional["VirtualServiceSpecHttpMatchMethod"] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        query_params: typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchQueryParams"]] = None,
        scheme: typing.Optional["VirtualServiceSpecHttpMatchScheme"] = None,
        source_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        source_namespace: typing.Optional[builtins.str] = None,
        uri: typing.Optional["VirtualServiceSpecHttpMatchUri"] = None,
        without_headers: typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchWithoutHeaders"]] = None,
    ) -> None:
        '''
        :param authority: 
        :param gateways: Names of gateways where the rule should be applied.
        :param headers: 
        :param ignore_uri_case: Flag to specify whether the URI matching should be case-insensitive.
        :param method: 
        :param name: The name assigned to a match.
        :param port: Specifies the ports on the host that is being addressed.
        :param query_params: Query parameters for matching.
        :param scheme: 
        :param source_labels: 
        :param source_namespace: Source namespace constraining the applicability of a rule to workloads in that namespace.
        :param uri: 
        :param without_headers: withoutHeader has the same syntax with the header, but has opposite meaning.

        :schema: VirtualServiceSpecHttpMatch
        '''
        if isinstance(authority, dict):
            authority = VirtualServiceSpecHttpMatchAuthority(**authority)
        if isinstance(method, dict):
            method = VirtualServiceSpecHttpMatchMethod(**method)
        if isinstance(scheme, dict):
            scheme = VirtualServiceSpecHttpMatchScheme(**scheme)
        if isinstance(uri, dict):
            uri = VirtualServiceSpecHttpMatchUri(**uri)
        self._values: typing.Dict[str, typing.Any] = {}
        if authority is not None:
            self._values["authority"] = authority
        if gateways is not None:
            self._values["gateways"] = gateways
        if headers is not None:
            self._values["headers"] = headers
        if ignore_uri_case is not None:
            self._values["ignore_uri_case"] = ignore_uri_case
        if method is not None:
            self._values["method"] = method
        if name is not None:
            self._values["name"] = name
        if port is not None:
            self._values["port"] = port
        if query_params is not None:
            self._values["query_params"] = query_params
        if scheme is not None:
            self._values["scheme"] = scheme
        if source_labels is not None:
            self._values["source_labels"] = source_labels
        if source_namespace is not None:
            self._values["source_namespace"] = source_namespace
        if uri is not None:
            self._values["uri"] = uri
        if without_headers is not None:
            self._values["without_headers"] = without_headers

    @builtins.property
    def authority(self) -> typing.Optional["VirtualServiceSpecHttpMatchAuthority"]:
        '''
        :schema: VirtualServiceSpecHttpMatch#authority
        '''
        result = self._values.get("authority")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpMatchAuthority"], result)

    @builtins.property
    def gateways(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Names of gateways where the rule should be applied.

        :schema: VirtualServiceSpecHttpMatch#gateways
        '''
        result = self._values.get("gateways")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchHeaders"]]:
        '''
        :schema: VirtualServiceSpecHttpMatch#headers
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchHeaders"]], result)

    @builtins.property
    def ignore_uri_case(self) -> typing.Optional[builtins.bool]:
        '''Flag to specify whether the URI matching should be case-insensitive.

        :schema: VirtualServiceSpecHttpMatch#ignoreUriCase
        '''
        result = self._values.get("ignore_uri_case")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def method(self) -> typing.Optional["VirtualServiceSpecHttpMatchMethod"]:
        '''
        :schema: VirtualServiceSpecHttpMatch#method
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpMatchMethod"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name assigned to a match.

        :schema: VirtualServiceSpecHttpMatch#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Specifies the ports on the host that is being addressed.

        :schema: VirtualServiceSpecHttpMatch#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def query_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchQueryParams"]]:
        '''Query parameters for matching.

        :schema: VirtualServiceSpecHttpMatch#queryParams
        '''
        result = self._values.get("query_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchQueryParams"]], result)

    @builtins.property
    def scheme(self) -> typing.Optional["VirtualServiceSpecHttpMatchScheme"]:
        '''
        :schema: VirtualServiceSpecHttpMatch#scheme
        '''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpMatchScheme"], result)

    @builtins.property
    def source_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpMatch#sourceLabels
        '''
        result = self._values.get("source_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def source_namespace(self) -> typing.Optional[builtins.str]:
        '''Source namespace constraining the applicability of a rule to workloads in that namespace.

        :schema: VirtualServiceSpecHttpMatch#sourceNamespace
        '''
        result = self._values.get("source_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uri(self) -> typing.Optional["VirtualServiceSpecHttpMatchUri"]:
        '''
        :schema: VirtualServiceSpecHttpMatch#uri
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpMatchUri"], result)

    @builtins.property
    def without_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchWithoutHeaders"]]:
        '''withoutHeader has the same syntax with the header, but has opposite meaning.

        :schema: VirtualServiceSpecHttpMatch#withoutHeaders
        '''
        result = self._values.get("without_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "VirtualServiceSpecHttpMatchWithoutHeaders"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpMatchAuthority",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchAuthority:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchAuthority
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchAuthority#exact
        '''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchAuthority#prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchAuthority#regex
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchAuthority(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpMatchHeaders",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchHeaders:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchHeaders
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchHeaders#exact
        '''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchHeaders#prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchHeaders#regex
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpMatchMethod",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchMethod:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchMethod
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchMethod#exact
        '''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchMethod#prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchMethod#regex
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpMatchQueryParams",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchQueryParams:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchQueryParams
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchQueryParams#exact
        '''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchQueryParams#prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchQueryParams#regex
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchQueryParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpMatchScheme",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchScheme:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchScheme
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchScheme#exact
        '''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchScheme#prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchScheme#regex
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchScheme(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpMatchUri",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchUri:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchUri
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchUri#exact
        '''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchUri#prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchUri#regex
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchUri(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpMatchWithoutHeaders",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class VirtualServiceSpecHttpMatchWithoutHeaders:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: 
        :param prefix: 
        :param regex: RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchWithoutHeaders
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchWithoutHeaders#exact
        '''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpMatchWithoutHeaders#prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''RE2 style regex-based match (https://github.com/google/re2/wiki/Syntax).

        :schema: VirtualServiceSpecHttpMatchWithoutHeaders#regex
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMatchWithoutHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpMirror",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port", "subset": "subset"},
)
class VirtualServiceSpecHttpMirror:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional["VirtualServiceSpecHttpMirrorPort"] = None,
        subset: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: The name of a service from the service registry.
        :param port: Specifies the port on the host that is being addressed.
        :param subset: The name of a subset within the service.

        :schema: VirtualServiceSpecHttpMirror
        '''
        if isinstance(port, dict):
            port = VirtualServiceSpecHttpMirrorPort(**port)
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port
        if subset is not None:
            self._values["subset"] = subset

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The name of a service from the service registry.

        :schema: VirtualServiceSpecHttpMirror#host
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional["VirtualServiceSpecHttpMirrorPort"]:
        '''Specifies the port on the host that is being addressed.

        :schema: VirtualServiceSpecHttpMirror#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpMirrorPort"], result)

    @builtins.property
    def subset(self) -> typing.Optional[builtins.str]:
        '''The name of a subset within the service.

        :schema: VirtualServiceSpecHttpMirror#subset
        '''
        result = self._values.get("subset")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMirror(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpMirrorPercentage",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class VirtualServiceSpecHttpMirrorPercentage:
    def __init__(self, *, value: typing.Optional[jsii.Number] = None) -> None:
        '''Percentage of the traffic to be mirrored by the ``mirror`` field.

        :param value: 

        :schema: VirtualServiceSpecHttpMirrorPercentage
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VirtualServiceSpecHttpMirrorPercentage#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMirrorPercentage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpMirrorPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class VirtualServiceSpecHttpMirrorPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        '''Specifies the port on the host that is being addressed.

        :param number: 

        :schema: VirtualServiceSpecHttpMirrorPort
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VirtualServiceSpecHttpMirrorPort#number
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpMirrorPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "authority": "authority",
        "derive_port": "derivePort",
        "port": "port",
        "redirect_code": "redirectCode",
        "scheme": "scheme",
        "uri": "uri",
    },
)
class VirtualServiceSpecHttpRedirect:
    def __init__(
        self,
        *,
        authority: typing.Optional[builtins.str] = None,
        derive_port: typing.Optional["VirtualServiceSpecHttpRedirectDerivePort"] = None,
        port: typing.Optional[jsii.Number] = None,
        redirect_code: typing.Optional[jsii.Number] = None,
        scheme: typing.Optional[builtins.str] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''A HTTP rule can either redirect or forward (default) traffic.

        :param authority: 
        :param derive_port: 
        :param port: On a redirect, overwrite the port portion of the URL with this value.
        :param redirect_code: 
        :param scheme: On a redirect, overwrite the scheme portion of the URL with this value.
        :param uri: 

        :schema: VirtualServiceSpecHttpRedirect
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if authority is not None:
            self._values["authority"] = authority
        if derive_port is not None:
            self._values["derive_port"] = derive_port
        if port is not None:
            self._values["port"] = port
        if redirect_code is not None:
            self._values["redirect_code"] = redirect_code
        if scheme is not None:
            self._values["scheme"] = scheme
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def authority(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpRedirect#authority
        '''
        result = self._values.get("authority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def derive_port(
        self,
    ) -> typing.Optional["VirtualServiceSpecHttpRedirectDerivePort"]:
        '''
        :schema: VirtualServiceSpecHttpRedirect#derivePort
        '''
        result = self._values.get("derive_port")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpRedirectDerivePort"], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''On a redirect, overwrite the port portion of the URL with this value.

        :schema: VirtualServiceSpecHttpRedirect#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def redirect_code(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VirtualServiceSpecHttpRedirect#redirectCode
        '''
        result = self._values.get("redirect_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''On a redirect, overwrite the scheme portion of the URL with this value.

        :schema: VirtualServiceSpecHttpRedirect#scheme
        '''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpRedirect#uri
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistionetworking.VirtualServiceSpecHttpRedirectDerivePort")
class VirtualServiceSpecHttpRedirectDerivePort(enum.Enum):
    '''
    :schema: VirtualServiceSpecHttpRedirectDerivePort
    '''

    FROM_PROTOCOL_DEFAULT = "FROM_PROTOCOL_DEFAULT"
    '''FROM_PROTOCOL_DEFAULT.'''
    FROM_REQUEST_PORT = "FROM_REQUEST_PORT"
    '''FROM_REQUEST_PORT.'''


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpRetries",
    jsii_struct_bases=[],
    name_mapping={
        "attempts": "attempts",
        "per_try_timeout": "perTryTimeout",
        "retry_on": "retryOn",
        "retry_remote_localities": "retryRemoteLocalities",
    },
)
class VirtualServiceSpecHttpRetries:
    def __init__(
        self,
        *,
        attempts: typing.Optional[jsii.Number] = None,
        per_try_timeout: typing.Optional[builtins.str] = None,
        retry_on: typing.Optional[builtins.str] = None,
        retry_remote_localities: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Retry policy for HTTP requests.

        :param attempts: Number of retries to be allowed for a given request.
        :param per_try_timeout: Timeout per attempt for a given request, including the initial call and any retries.
        :param retry_on: Specifies the conditions under which retry takes place.
        :param retry_remote_localities: Flag to specify whether the retries should retry to other localities.

        :schema: VirtualServiceSpecHttpRetries
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if attempts is not None:
            self._values["attempts"] = attempts
        if per_try_timeout is not None:
            self._values["per_try_timeout"] = per_try_timeout
        if retry_on is not None:
            self._values["retry_on"] = retry_on
        if retry_remote_localities is not None:
            self._values["retry_remote_localities"] = retry_remote_localities

    @builtins.property
    def attempts(self) -> typing.Optional[jsii.Number]:
        '''Number of retries to be allowed for a given request.

        :schema: VirtualServiceSpecHttpRetries#attempts
        '''
        result = self._values.get("attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def per_try_timeout(self) -> typing.Optional[builtins.str]:
        '''Timeout per attempt for a given request, including the initial call and any retries.

        :schema: VirtualServiceSpecHttpRetries#perTryTimeout
        '''
        result = self._values.get("per_try_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry_on(self) -> typing.Optional[builtins.str]:
        '''Specifies the conditions under which retry takes place.

        :schema: VirtualServiceSpecHttpRetries#retryOn
        '''
        result = self._values.get("retry_on")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry_remote_localities(self) -> typing.Optional[builtins.bool]:
        '''Flag to specify whether the retries should retry to other localities.

        :schema: VirtualServiceSpecHttpRetries#retryRemoteLocalities
        '''
        result = self._values.get("retry_remote_localities")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRetries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpRewrite",
    jsii_struct_bases=[],
    name_mapping={"authority": "authority", "uri": "uri"},
)
class VirtualServiceSpecHttpRewrite:
    def __init__(
        self,
        *,
        authority: typing.Optional[builtins.str] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Rewrite HTTP URIs and Authority headers.

        :param authority: rewrite the Authority/Host header with this value.
        :param uri: 

        :schema: VirtualServiceSpecHttpRewrite
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if authority is not None:
            self._values["authority"] = authority
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def authority(self) -> typing.Optional[builtins.str]:
        '''rewrite the Authority/Host header with this value.

        :schema: VirtualServiceSpecHttpRewrite#authority
        '''
        result = self._values.get("authority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''
        :schema: VirtualServiceSpecHttpRewrite#uri
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRewrite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpRoute",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "headers": "headers",
        "weight": "weight",
    },
)
class VirtualServiceSpecHttpRoute:
    def __init__(
        self,
        *,
        destination: typing.Optional["VirtualServiceSpecHttpRouteDestination"] = None,
        headers: typing.Optional["VirtualServiceSpecHttpRouteHeaders"] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param destination: 
        :param headers: 
        :param weight: Weight specifies the relative proportion of traffic to be forwarded to the destination.

        :schema: VirtualServiceSpecHttpRoute
        '''
        if isinstance(destination, dict):
            destination = VirtualServiceSpecHttpRouteDestination(**destination)
        if isinstance(headers, dict):
            headers = VirtualServiceSpecHttpRouteHeaders(**headers)
        self._values: typing.Dict[str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination
        if headers is not None:
            self._values["headers"] = headers
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def destination(self) -> typing.Optional["VirtualServiceSpecHttpRouteDestination"]:
        '''
        :schema: VirtualServiceSpecHttpRoute#destination
        '''
        result = self._values.get("destination")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpRouteDestination"], result)

    @builtins.property
    def headers(self) -> typing.Optional["VirtualServiceSpecHttpRouteHeaders"]:
        '''
        :schema: VirtualServiceSpecHttpRoute#headers
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpRouteHeaders"], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Weight specifies the relative proportion of traffic to be forwarded to the destination.

        :schema: VirtualServiceSpecHttpRoute#weight
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpRouteDestination",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port", "subset": "subset"},
)
class VirtualServiceSpecHttpRouteDestination:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional["VirtualServiceSpecHttpRouteDestinationPort"] = None,
        subset: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: The name of a service from the service registry.
        :param port: Specifies the port on the host that is being addressed.
        :param subset: The name of a subset within the service.

        :schema: VirtualServiceSpecHttpRouteDestination
        '''
        if isinstance(port, dict):
            port = VirtualServiceSpecHttpRouteDestinationPort(**port)
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port
        if subset is not None:
            self._values["subset"] = subset

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The name of a service from the service registry.

        :schema: VirtualServiceSpecHttpRouteDestination#host
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional["VirtualServiceSpecHttpRouteDestinationPort"]:
        '''Specifies the port on the host that is being addressed.

        :schema: VirtualServiceSpecHttpRouteDestination#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpRouteDestinationPort"], result)

    @builtins.property
    def subset(self) -> typing.Optional[builtins.str]:
        '''The name of a subset within the service.

        :schema: VirtualServiceSpecHttpRouteDestination#subset
        '''
        result = self._values.get("subset")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRouteDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpRouteDestinationPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class VirtualServiceSpecHttpRouteDestinationPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        '''Specifies the port on the host that is being addressed.

        :param number: 

        :schema: VirtualServiceSpecHttpRouteDestinationPort
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VirtualServiceSpecHttpRouteDestinationPort#number
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRouteDestinationPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpRouteHeaders",
    jsii_struct_bases=[],
    name_mapping={"request": "request", "response": "response"},
)
class VirtualServiceSpecHttpRouteHeaders:
    def __init__(
        self,
        *,
        request: typing.Optional["VirtualServiceSpecHttpRouteHeadersRequest"] = None,
        response: typing.Optional["VirtualServiceSpecHttpRouteHeadersResponse"] = None,
    ) -> None:
        '''
        :param request: 
        :param response: 

        :schema: VirtualServiceSpecHttpRouteHeaders
        '''
        if isinstance(request, dict):
            request = VirtualServiceSpecHttpRouteHeadersRequest(**request)
        if isinstance(response, dict):
            response = VirtualServiceSpecHttpRouteHeadersResponse(**response)
        self._values: typing.Dict[str, typing.Any] = {}
        if request is not None:
            self._values["request"] = request
        if response is not None:
            self._values["response"] = response

    @builtins.property
    def request(self) -> typing.Optional["VirtualServiceSpecHttpRouteHeadersRequest"]:
        '''
        :schema: VirtualServiceSpecHttpRouteHeaders#request
        '''
        result = self._values.get("request")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpRouteHeadersRequest"], result)

    @builtins.property
    def response(self) -> typing.Optional["VirtualServiceSpecHttpRouteHeadersResponse"]:
        '''
        :schema: VirtualServiceSpecHttpRouteHeaders#response
        '''
        result = self._values.get("response")
        return typing.cast(typing.Optional["VirtualServiceSpecHttpRouteHeadersResponse"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRouteHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpRouteHeadersRequest",
    jsii_struct_bases=[],
    name_mapping={"add": "add", "remove": "remove", "set": "set"},
)
class VirtualServiceSpecHttpRouteHeadersRequest:
    def __init__(
        self,
        *,
        add: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        set: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param add: 
        :param remove: 
        :param set: 

        :schema: VirtualServiceSpecHttpRouteHeadersRequest
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if add is not None:
            self._values["add"] = add
        if remove is not None:
            self._values["remove"] = remove
        if set is not None:
            self._values["set"] = set

    @builtins.property
    def add(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpRouteHeadersRequest#add
        '''
        result = self._values.get("add")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpRouteHeadersRequest#remove
        '''
        result = self._values.get("remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def set(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpRouteHeadersRequest#set
        '''
        result = self._values.get("set")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRouteHeadersRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecHttpRouteHeadersResponse",
    jsii_struct_bases=[],
    name_mapping={"add": "add", "remove": "remove", "set": "set"},
)
class VirtualServiceSpecHttpRouteHeadersResponse:
    def __init__(
        self,
        *,
        add: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        remove: typing.Optional[typing.Sequence[builtins.str]] = None,
        set: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param add: 
        :param remove: 
        :param set: 

        :schema: VirtualServiceSpecHttpRouteHeadersResponse
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if add is not None:
            self._values["add"] = add
        if remove is not None:
            self._values["remove"] = remove
        if set is not None:
            self._values["set"] = set

    @builtins.property
    def add(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpRouteHeadersResponse#add
        '''
        result = self._values.get("add")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def remove(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpRouteHeadersResponse#remove
        '''
        result = self._values.get("remove")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def set(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: VirtualServiceSpecHttpRouteHeadersResponse#set
        '''
        result = self._values.get("set")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecHttpRouteHeadersResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecTcp",
    jsii_struct_bases=[],
    name_mapping={"match": "match", "route": "route"},
)
class VirtualServiceSpecTcp:
    def __init__(
        self,
        *,
        match: typing.Optional[typing.Sequence["VirtualServiceSpecTcpMatch"]] = None,
        route: typing.Optional[typing.Sequence["VirtualServiceSpecTcpRoute"]] = None,
    ) -> None:
        '''
        :param match: 
        :param route: The destination to which the connection should be forwarded to.

        :schema: VirtualServiceSpecTcp
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if match is not None:
            self._values["match"] = match
        if route is not None:
            self._values["route"] = route

    @builtins.property
    def match(self) -> typing.Optional[typing.List["VirtualServiceSpecTcpMatch"]]:
        '''
        :schema: VirtualServiceSpecTcp#match
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional[typing.List["VirtualServiceSpecTcpMatch"]], result)

    @builtins.property
    def route(self) -> typing.Optional[typing.List["VirtualServiceSpecTcpRoute"]]:
        '''The destination to which the connection should be forwarded to.

        :schema: VirtualServiceSpecTcp#route
        '''
        result = self._values.get("route")
        return typing.cast(typing.Optional[typing.List["VirtualServiceSpecTcpRoute"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecTcpMatch",
    jsii_struct_bases=[],
    name_mapping={
        "destination_subnets": "destinationSubnets",
        "gateways": "gateways",
        "port": "port",
        "source_labels": "sourceLabels",
        "source_namespace": "sourceNamespace",
        "source_subnet": "sourceSubnet",
    },
)
class VirtualServiceSpecTcpMatch:
    def __init__(
        self,
        *,
        destination_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
        port: typing.Optional[jsii.Number] = None,
        source_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        source_namespace: typing.Optional[builtins.str] = None,
        source_subnet: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_subnets: IPv4 or IPv6 ip addresses of destination with optional subnet.
        :param gateways: Names of gateways where the rule should be applied.
        :param port: Specifies the port on the host that is being addressed.
        :param source_labels: 
        :param source_namespace: Source namespace constraining the applicability of a rule to workloads in that namespace.
        :param source_subnet: IPv4 or IPv6 ip address of source with optional subnet.

        :schema: VirtualServiceSpecTcpMatch
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if destination_subnets is not None:
            self._values["destination_subnets"] = destination_subnets
        if gateways is not None:
            self._values["gateways"] = gateways
        if port is not None:
            self._values["port"] = port
        if source_labels is not None:
            self._values["source_labels"] = source_labels
        if source_namespace is not None:
            self._values["source_namespace"] = source_namespace
        if source_subnet is not None:
            self._values["source_subnet"] = source_subnet

    @builtins.property
    def destination_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''IPv4 or IPv6 ip addresses of destination with optional subnet.

        :schema: VirtualServiceSpecTcpMatch#destinationSubnets
        '''
        result = self._values.get("destination_subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def gateways(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Names of gateways where the rule should be applied.

        :schema: VirtualServiceSpecTcpMatch#gateways
        '''
        result = self._values.get("gateways")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Specifies the port on the host that is being addressed.

        :schema: VirtualServiceSpecTcpMatch#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: VirtualServiceSpecTcpMatch#sourceLabels
        '''
        result = self._values.get("source_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def source_namespace(self) -> typing.Optional[builtins.str]:
        '''Source namespace constraining the applicability of a rule to workloads in that namespace.

        :schema: VirtualServiceSpecTcpMatch#sourceNamespace
        '''
        result = self._values.get("source_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_subnet(self) -> typing.Optional[builtins.str]:
        '''IPv4 or IPv6 ip address of source with optional subnet.

        :schema: VirtualServiceSpecTcpMatch#sourceSubnet
        '''
        result = self._values.get("source_subnet")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTcpMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecTcpRoute",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination", "weight": "weight"},
)
class VirtualServiceSpecTcpRoute:
    def __init__(
        self,
        *,
        destination: typing.Optional["VirtualServiceSpecTcpRouteDestination"] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param destination: 
        :param weight: Weight specifies the relative proportion of traffic to be forwarded to the destination.

        :schema: VirtualServiceSpecTcpRoute
        '''
        if isinstance(destination, dict):
            destination = VirtualServiceSpecTcpRouteDestination(**destination)
        self._values: typing.Dict[str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def destination(self) -> typing.Optional["VirtualServiceSpecTcpRouteDestination"]:
        '''
        :schema: VirtualServiceSpecTcpRoute#destination
        '''
        result = self._values.get("destination")
        return typing.cast(typing.Optional["VirtualServiceSpecTcpRouteDestination"], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Weight specifies the relative proportion of traffic to be forwarded to the destination.

        :schema: VirtualServiceSpecTcpRoute#weight
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTcpRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecTcpRouteDestination",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port", "subset": "subset"},
)
class VirtualServiceSpecTcpRouteDestination:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional["VirtualServiceSpecTcpRouteDestinationPort"] = None,
        subset: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: The name of a service from the service registry.
        :param port: Specifies the port on the host that is being addressed.
        :param subset: The name of a subset within the service.

        :schema: VirtualServiceSpecTcpRouteDestination
        '''
        if isinstance(port, dict):
            port = VirtualServiceSpecTcpRouteDestinationPort(**port)
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port
        if subset is not None:
            self._values["subset"] = subset

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The name of a service from the service registry.

        :schema: VirtualServiceSpecTcpRouteDestination#host
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional["VirtualServiceSpecTcpRouteDestinationPort"]:
        '''Specifies the port on the host that is being addressed.

        :schema: VirtualServiceSpecTcpRouteDestination#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional["VirtualServiceSpecTcpRouteDestinationPort"], result)

    @builtins.property
    def subset(self) -> typing.Optional[builtins.str]:
        '''The name of a subset within the service.

        :schema: VirtualServiceSpecTcpRouteDestination#subset
        '''
        result = self._values.get("subset")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTcpRouteDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecTcpRouteDestinationPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class VirtualServiceSpecTcpRouteDestinationPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        '''Specifies the port on the host that is being addressed.

        :param number: 

        :schema: VirtualServiceSpecTcpRouteDestinationPort
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VirtualServiceSpecTcpRouteDestinationPort#number
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTcpRouteDestinationPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecTls",
    jsii_struct_bases=[],
    name_mapping={"match": "match", "route": "route"},
)
class VirtualServiceSpecTls:
    def __init__(
        self,
        *,
        match: typing.Optional[typing.Sequence["VirtualServiceSpecTlsMatch"]] = None,
        route: typing.Optional[typing.Sequence["VirtualServiceSpecTlsRoute"]] = None,
    ) -> None:
        '''
        :param match: 
        :param route: The destination to which the connection should be forwarded to.

        :schema: VirtualServiceSpecTls
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if match is not None:
            self._values["match"] = match
        if route is not None:
            self._values["route"] = route

    @builtins.property
    def match(self) -> typing.Optional[typing.List["VirtualServiceSpecTlsMatch"]]:
        '''
        :schema: VirtualServiceSpecTls#match
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional[typing.List["VirtualServiceSpecTlsMatch"]], result)

    @builtins.property
    def route(self) -> typing.Optional[typing.List["VirtualServiceSpecTlsRoute"]]:
        '''The destination to which the connection should be forwarded to.

        :schema: VirtualServiceSpecTls#route
        '''
        result = self._values.get("route")
        return typing.cast(typing.Optional[typing.List["VirtualServiceSpecTlsRoute"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecTlsMatch",
    jsii_struct_bases=[],
    name_mapping={
        "destination_subnets": "destinationSubnets",
        "gateways": "gateways",
        "port": "port",
        "sni_hosts": "sniHosts",
        "source_labels": "sourceLabels",
        "source_namespace": "sourceNamespace",
    },
)
class VirtualServiceSpecTlsMatch:
    def __init__(
        self,
        *,
        destination_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
        port: typing.Optional[jsii.Number] = None,
        sni_hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        source_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_subnets: IPv4 or IPv6 ip addresses of destination with optional subnet.
        :param gateways: Names of gateways where the rule should be applied.
        :param port: Specifies the port on the host that is being addressed.
        :param sni_hosts: SNI (server name indicator) to match on.
        :param source_labels: 
        :param source_namespace: Source namespace constraining the applicability of a rule to workloads in that namespace.

        :schema: VirtualServiceSpecTlsMatch
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if destination_subnets is not None:
            self._values["destination_subnets"] = destination_subnets
        if gateways is not None:
            self._values["gateways"] = gateways
        if port is not None:
            self._values["port"] = port
        if sni_hosts is not None:
            self._values["sni_hosts"] = sni_hosts
        if source_labels is not None:
            self._values["source_labels"] = source_labels
        if source_namespace is not None:
            self._values["source_namespace"] = source_namespace

    @builtins.property
    def destination_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''IPv4 or IPv6 ip addresses of destination with optional subnet.

        :schema: VirtualServiceSpecTlsMatch#destinationSubnets
        '''
        result = self._values.get("destination_subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def gateways(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Names of gateways where the rule should be applied.

        :schema: VirtualServiceSpecTlsMatch#gateways
        '''
        result = self._values.get("gateways")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Specifies the port on the host that is being addressed.

        :schema: VirtualServiceSpecTlsMatch#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sni_hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''SNI (server name indicator) to match on.

        :schema: VirtualServiceSpecTlsMatch#sniHosts
        '''
        result = self._values.get("sni_hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: VirtualServiceSpecTlsMatch#sourceLabels
        '''
        result = self._values.get("source_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def source_namespace(self) -> typing.Optional[builtins.str]:
        '''Source namespace constraining the applicability of a rule to workloads in that namespace.

        :schema: VirtualServiceSpecTlsMatch#sourceNamespace
        '''
        result = self._values.get("source_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTlsMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecTlsRoute",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination", "weight": "weight"},
)
class VirtualServiceSpecTlsRoute:
    def __init__(
        self,
        *,
        destination: typing.Optional["VirtualServiceSpecTlsRouteDestination"] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param destination: 
        :param weight: Weight specifies the relative proportion of traffic to be forwarded to the destination.

        :schema: VirtualServiceSpecTlsRoute
        '''
        if isinstance(destination, dict):
            destination = VirtualServiceSpecTlsRouteDestination(**destination)
        self._values: typing.Dict[str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def destination(self) -> typing.Optional["VirtualServiceSpecTlsRouteDestination"]:
        '''
        :schema: VirtualServiceSpecTlsRoute#destination
        '''
        result = self._values.get("destination")
        return typing.cast(typing.Optional["VirtualServiceSpecTlsRouteDestination"], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Weight specifies the relative proportion of traffic to be forwarded to the destination.

        :schema: VirtualServiceSpecTlsRoute#weight
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTlsRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecTlsRouteDestination",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port", "subset": "subset"},
)
class VirtualServiceSpecTlsRouteDestination:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional["VirtualServiceSpecTlsRouteDestinationPort"] = None,
        subset: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: The name of a service from the service registry.
        :param port: Specifies the port on the host that is being addressed.
        :param subset: The name of a subset within the service.

        :schema: VirtualServiceSpecTlsRouteDestination
        '''
        if isinstance(port, dict):
            port = VirtualServiceSpecTlsRouteDestinationPort(**port)
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port
        if subset is not None:
            self._values["subset"] = subset

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The name of a service from the service registry.

        :schema: VirtualServiceSpecTlsRouteDestination#host
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional["VirtualServiceSpecTlsRouteDestinationPort"]:
        '''Specifies the port on the host that is being addressed.

        :schema: VirtualServiceSpecTlsRouteDestination#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional["VirtualServiceSpecTlsRouteDestinationPort"], result)

    @builtins.property
    def subset(self) -> typing.Optional[builtins.str]:
        '''The name of a subset within the service.

        :schema: VirtualServiceSpecTlsRouteDestination#subset
        '''
        result = self._values.get("subset")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTlsRouteDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.VirtualServiceSpecTlsRouteDestinationPort",
    jsii_struct_bases=[],
    name_mapping={"number": "number"},
)
class VirtualServiceSpecTlsRouteDestinationPort:
    def __init__(self, *, number: typing.Optional[jsii.Number] = None) -> None:
        '''Specifies the port on the host that is being addressed.

        :param number: 

        :schema: VirtualServiceSpecTlsRouteDestinationPort
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if number is not None:
            self._values["number"] = number

    @builtins.property
    def number(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: VirtualServiceSpecTlsRouteDestinationPort#number
        '''
        result = self._values.get("number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceSpecTlsRouteDestinationPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkloadEntry(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistionetworking.WorkloadEntry",
):
    '''
    :schema: WorkloadEntry
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["WorkloadEntrySpec"] = None,
    ) -> None:
        '''Defines a "WorkloadEntry" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: Configuration affecting VMs onboarded into the mesh. See more details at: https://istio.io/docs/reference/config/networking/workload-entry.html
        '''
        props = WorkloadEntryProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["WorkloadEntrySpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "WorkloadEntry".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: Configuration affecting VMs onboarded into the mesh. See more details at: https://istio.io/docs/reference/config/networking/workload-entry.html
        '''
        props = WorkloadEntryProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "WorkloadEntry".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistionetworking.WorkloadEntryProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class WorkloadEntryProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["WorkloadEntrySpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: Configuration affecting VMs onboarded into the mesh. See more details at: https://istio.io/docs/reference/config/networking/workload-entry.html

        :schema: WorkloadEntry
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = WorkloadEntrySpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: WorkloadEntry#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["WorkloadEntrySpec"]:
        '''Configuration affecting VMs onboarded into the mesh.

        See more details at: https://istio.io/docs/reference/config/networking/workload-entry.html

        :schema: WorkloadEntry#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["WorkloadEntrySpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadEntryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.WorkloadEntrySpec",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "labels": "labels",
        "locality": "locality",
        "network": "network",
        "ports": "ports",
        "service_account": "serviceAccount",
        "weight": "weight",
    },
)
class WorkloadEntrySpec:
    def __init__(
        self,
        *,
        address: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        locality: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
        service_account: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Configuration affecting VMs onboarded into the mesh.

        See more details at: https://istio.io/docs/reference/config/networking/workload-entry.html

        :param address: 
        :param labels: One or more labels associated with the endpoint.
        :param locality: The locality associated with the endpoint.
        :param network: 
        :param ports: Set of ports associated with the endpoint.
        :param service_account: 
        :param weight: The load balancing weight associated with the endpoint.

        :schema: WorkloadEntrySpec
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if address is not None:
            self._values["address"] = address
        if labels is not None:
            self._values["labels"] = labels
        if locality is not None:
            self._values["locality"] = locality
        if network is not None:
            self._values["network"] = network
        if ports is not None:
            self._values["ports"] = ports
        if service_account is not None:
            self._values["service_account"] = service_account
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''
        :schema: WorkloadEntrySpec#address
        '''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''One or more labels associated with the endpoint.

        :schema: WorkloadEntrySpec#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def locality(self) -> typing.Optional[builtins.str]:
        '''The locality associated with the endpoint.

        :schema: WorkloadEntrySpec#locality
        '''
        result = self._values.get("locality")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''
        :schema: WorkloadEntrySpec#network
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''Set of ports associated with the endpoint.

        :schema: WorkloadEntrySpec#ports
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''
        :schema: WorkloadEntrySpec#serviceAccount
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''The load balancing weight associated with the endpoint.

        :schema: WorkloadEntrySpec#weight
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadEntrySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkloadGroup(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistionetworking.WorkloadGroup",
):
    '''
    :schema: WorkloadGroup
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["WorkloadGroupSpec"] = None,
    ) -> None:
        '''Defines a "WorkloadGroup" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: Describes a collection of workload instances. See more details at: https://istio.io/docs/reference/config/networking/workload-group.html
        '''
        props = WorkloadGroupProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["WorkloadGroupSpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "WorkloadGroup".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: Describes a collection of workload instances. See more details at: https://istio.io/docs/reference/config/networking/workload-group.html
        '''
        props = WorkloadGroupProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "WorkloadGroup".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistionetworking.WorkloadGroupProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class WorkloadGroupProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["WorkloadGroupSpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: Describes a collection of workload instances. See more details at: https://istio.io/docs/reference/config/networking/workload-group.html

        :schema: WorkloadGroup
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = WorkloadGroupSpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: WorkloadGroup#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["WorkloadGroupSpec"]:
        '''Describes a collection of workload instances.

        See more details at: https://istio.io/docs/reference/config/networking/workload-group.html

        :schema: WorkloadGroup#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["WorkloadGroupSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.WorkloadGroupSpec",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "probe": "probe", "template": "template"},
)
class WorkloadGroupSpec:
    def __init__(
        self,
        *,
        metadata: typing.Optional["WorkloadGroupSpecMetadata"] = None,
        probe: typing.Optional["WorkloadGroupSpecProbe"] = None,
        template: typing.Optional["WorkloadGroupSpecTemplate"] = None,
    ) -> None:
        '''Describes a collection of workload instances.

        See more details at: https://istio.io/docs/reference/config/networking/workload-group.html

        :param metadata: Metadata that will be used for all corresponding ``WorkloadEntries``.
        :param probe: ``ReadinessProbe`` describes the configuration the user must provide for healthchecking on their workload.
        :param template: Template to be used for the generation of ``WorkloadEntry`` resources that belong to this ``WorkloadGroup``.

        :schema: WorkloadGroupSpec
        '''
        if isinstance(metadata, dict):
            metadata = WorkloadGroupSpecMetadata(**metadata)
        if isinstance(probe, dict):
            probe = WorkloadGroupSpecProbe(**probe)
        if isinstance(template, dict):
            template = WorkloadGroupSpecTemplate(**template)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if probe is not None:
            self._values["probe"] = probe
        if template is not None:
            self._values["template"] = template

    @builtins.property
    def metadata(self) -> typing.Optional["WorkloadGroupSpecMetadata"]:
        '''Metadata that will be used for all corresponding ``WorkloadEntries``.

        :schema: WorkloadGroupSpec#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional["WorkloadGroupSpecMetadata"], result)

    @builtins.property
    def probe(self) -> typing.Optional["WorkloadGroupSpecProbe"]:
        '''``ReadinessProbe`` describes the configuration the user must provide for healthchecking on their workload.

        :schema: WorkloadGroupSpec#probe
        '''
        result = self._values.get("probe")
        return typing.cast(typing.Optional["WorkloadGroupSpecProbe"], result)

    @builtins.property
    def template(self) -> typing.Optional["WorkloadGroupSpecTemplate"]:
        '''Template to be used for the generation of ``WorkloadEntry`` resources that belong to this ``WorkloadGroup``.

        :schema: WorkloadGroupSpec#template
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional["WorkloadGroupSpecTemplate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.WorkloadGroupSpecMetadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels"},
)
class WorkloadGroupSpecMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Metadata that will be used for all corresponding ``WorkloadEntries``.

        :param annotations: 
        :param labels: 

        :schema: WorkloadGroupSpecMetadata
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: WorkloadGroupSpecMetadata#annotations
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: WorkloadGroupSpecMetadata#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.WorkloadGroupSpecProbe",
    jsii_struct_bases=[],
    name_mapping={
        "exec": "exec",
        "failure_threshold": "failureThreshold",
        "http_get": "httpGet",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "tcp_socket": "tcpSocket",
        "timeout_seconds": "timeoutSeconds",
    },
)
class WorkloadGroupSpecProbe:
    def __init__(
        self,
        *,
        exec: typing.Optional["WorkloadGroupSpecProbeExec"] = None,
        failure_threshold: typing.Optional[jsii.Number] = None,
        http_get: typing.Optional["WorkloadGroupSpecProbeHttpGet"] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        tcp_socket: typing.Optional["WorkloadGroupSpecProbeTcpSocket"] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''``ReadinessProbe`` describes the configuration the user must provide for healthchecking on their workload.

        :param exec: Health is determined by how the command that is executed exited.
        :param failure_threshold: Minimum consecutive failures for the probe to be considered failed after having succeeded.
        :param http_get: 
        :param initial_delay_seconds: Number of seconds after the container has started before readiness probes are initiated.
        :param period_seconds: How often (in seconds) to perform the probe.
        :param success_threshold: Minimum consecutive successes for the probe to be considered successful after having failed.
        :param tcp_socket: Health is determined by if the proxy is able to connect.
        :param timeout_seconds: Number of seconds after which the probe times out.

        :schema: WorkloadGroupSpecProbe
        '''
        if isinstance(exec, dict):
            exec = WorkloadGroupSpecProbeExec(**exec)
        if isinstance(http_get, dict):
            http_get = WorkloadGroupSpecProbeHttpGet(**http_get)
        if isinstance(tcp_socket, dict):
            tcp_socket = WorkloadGroupSpecProbeTcpSocket(**tcp_socket)
        self._values: typing.Dict[str, typing.Any] = {}
        if exec is not None:
            self._values["exec"] = exec
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if http_get is not None:
            self._values["http_get"] = http_get
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if tcp_socket is not None:
            self._values["tcp_socket"] = tcp_socket
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def exec(self) -> typing.Optional["WorkloadGroupSpecProbeExec"]:
        '''Health is determined by how the command that is executed exited.

        :schema: WorkloadGroupSpecProbe#exec
        '''
        result = self._values.get("exec")
        return typing.cast(typing.Optional["WorkloadGroupSpecProbeExec"], result)

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive failures for the probe to be considered failed after having succeeded.

        :schema: WorkloadGroupSpecProbe#failureThreshold
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http_get(self) -> typing.Optional["WorkloadGroupSpecProbeHttpGet"]:
        '''
        :schema: WorkloadGroupSpecProbe#httpGet
        '''
        result = self._values.get("http_get")
        return typing.cast(typing.Optional["WorkloadGroupSpecProbeHttpGet"], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''Number of seconds after the container has started before readiness probes are initiated.

        :schema: WorkloadGroupSpecProbe#initialDelaySeconds
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[jsii.Number]:
        '''How often (in seconds) to perform the probe.

        :schema: WorkloadGroupSpecProbe#periodSeconds
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''Minimum consecutive successes for the probe to be considered successful after having failed.

        :schema: WorkloadGroupSpecProbe#successThreshold
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tcp_socket(self) -> typing.Optional["WorkloadGroupSpecProbeTcpSocket"]:
        '''Health is determined by if the proxy is able to connect.

        :schema: WorkloadGroupSpecProbe#tcpSocket
        '''
        result = self._values.get("tcp_socket")
        return typing.cast(typing.Optional["WorkloadGroupSpecProbeTcpSocket"], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Number of seconds after which the probe times out.

        :schema: WorkloadGroupSpecProbe#timeoutSeconds
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.WorkloadGroupSpecProbeExec",
    jsii_struct_bases=[],
    name_mapping={"command": "command"},
)
class WorkloadGroupSpecProbeExec:
    def __init__(
        self,
        *,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Health is determined by how the command that is executed exited.

        :param command: Command to run.

        :schema: WorkloadGroupSpecProbeExec
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if command is not None:
            self._values["command"] = command

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Command to run.

        :schema: WorkloadGroupSpecProbeExec#command
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecProbeExec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.WorkloadGroupSpecProbeHttpGet",
    jsii_struct_bases=[],
    name_mapping={
        "host": "host",
        "http_headers": "httpHeaders",
        "path": "path",
        "port": "port",
        "scheme": "scheme",
    },
)
class WorkloadGroupSpecProbeHttpGet:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        http_headers: typing.Optional[typing.Sequence["WorkloadGroupSpecProbeHttpGetHttpHeaders"]] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: Host name to connect to, defaults to the pod IP.
        :param http_headers: Headers the proxy will pass on to make the request.
        :param path: Path to access on the HTTP server.
        :param port: Port on which the endpoint lives.
        :param scheme: 

        :schema: WorkloadGroupSpecProbeHttpGet
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if http_headers is not None:
            self._values["http_headers"] = http_headers
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port
        if scheme is not None:
            self._values["scheme"] = scheme

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Host name to connect to, defaults to the pod IP.

        :schema: WorkloadGroupSpecProbeHttpGet#host
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_headers(
        self,
    ) -> typing.Optional[typing.List["WorkloadGroupSpecProbeHttpGetHttpHeaders"]]:
        '''Headers the proxy will pass on to make the request.

        :schema: WorkloadGroupSpecProbeHttpGet#httpHeaders
        '''
        result = self._values.get("http_headers")
        return typing.cast(typing.Optional[typing.List["WorkloadGroupSpecProbeHttpGetHttpHeaders"]], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path to access on the HTTP server.

        :schema: WorkloadGroupSpecProbeHttpGet#path
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port on which the endpoint lives.

        :schema: WorkloadGroupSpecProbeHttpGet#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''
        :schema: WorkloadGroupSpecProbeHttpGet#scheme
        '''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecProbeHttpGet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.WorkloadGroupSpecProbeHttpGetHttpHeaders",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class WorkloadGroupSpecProbeHttpGetHttpHeaders:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: 
        :param value: 

        :schema: WorkloadGroupSpecProbeHttpGetHttpHeaders
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :schema: WorkloadGroupSpecProbeHttpGetHttpHeaders#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''
        :schema: WorkloadGroupSpecProbeHttpGetHttpHeaders#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecProbeHttpGetHttpHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.WorkloadGroupSpecProbeTcpSocket",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port"},
)
class WorkloadGroupSpecProbeTcpSocket:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Health is determined by if the proxy is able to connect.

        :param host: 
        :param port: 

        :schema: WorkloadGroupSpecProbeTcpSocket
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''
        :schema: WorkloadGroupSpecProbeTcpSocket#host
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: WorkloadGroupSpecProbeTcpSocket#port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecProbeTcpSocket(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistionetworking.WorkloadGroupSpecTemplate",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "labels": "labels",
        "locality": "locality",
        "network": "network",
        "ports": "ports",
        "service_account": "serviceAccount",
        "weight": "weight",
    },
)
class WorkloadGroupSpecTemplate:
    def __init__(
        self,
        *,
        address: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        locality: typing.Optional[builtins.str] = None,
        network: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
        service_account: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Template to be used for the generation of ``WorkloadEntry`` resources that belong to this ``WorkloadGroup``.

        :param address: 
        :param labels: One or more labels associated with the endpoint.
        :param locality: The locality associated with the endpoint.
        :param network: 
        :param ports: Set of ports associated with the endpoint.
        :param service_account: 
        :param weight: The load balancing weight associated with the endpoint.

        :schema: WorkloadGroupSpecTemplate
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if address is not None:
            self._values["address"] = address
        if labels is not None:
            self._values["labels"] = labels
        if locality is not None:
            self._values["locality"] = locality
        if network is not None:
            self._values["network"] = network
        if ports is not None:
            self._values["ports"] = ports
        if service_account is not None:
            self._values["service_account"] = service_account
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''
        :schema: WorkloadGroupSpecTemplate#address
        '''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''One or more labels associated with the endpoint.

        :schema: WorkloadGroupSpecTemplate#labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def locality(self) -> typing.Optional[builtins.str]:
        '''The locality associated with the endpoint.

        :schema: WorkloadGroupSpecTemplate#locality
        '''
        result = self._values.get("locality")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''
        :schema: WorkloadGroupSpecTemplate#network
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''Set of ports associated with the endpoint.

        :schema: WorkloadGroupSpecTemplate#ports
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''
        :schema: WorkloadGroupSpecTemplate#serviceAccount
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''The load balancing weight associated with the endpoint.

        :schema: WorkloadGroupSpecTemplate#weight
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkloadGroupSpecTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DestinationRule",
    "DestinationRuleProps",
    "DestinationRuleSpec",
    "DestinationRuleSpecSubsets",
    "DestinationRuleSpecSubsetsTrafficPolicy",
    "DestinationRuleSpecSubsetsTrafficPolicyConnectionPool",
    "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttp",
    "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolHttpH2UpgradePolicy",
    "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcp",
    "DestinationRuleSpecSubsetsTrafficPolicyConnectionPoolTcpTcpKeepalive",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancer",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHash",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerConsistentHashHttpCookie",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSetting",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingDistribute",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerLocalityLbSettingFailover",
    "DestinationRuleSpecSubsetsTrafficPolicyLoadBalancerSimple",
    "DestinationRuleSpecSubsetsTrafficPolicyOutlierDetection",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettings",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPool",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttp",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcp",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancer",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsLoadBalancerSimple",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsOutlierDetection",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsPort",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTls",
    "DestinationRuleSpecSubsetsTrafficPolicyPortLevelSettingsTlsMode",
    "DestinationRuleSpecSubsetsTrafficPolicyTls",
    "DestinationRuleSpecSubsetsTrafficPolicyTlsMode",
    "DestinationRuleSpecSubsetsTrafficPolicyTunnel",
    "DestinationRuleSpecTrafficPolicy",
    "DestinationRuleSpecTrafficPolicyConnectionPool",
    "DestinationRuleSpecTrafficPolicyConnectionPoolHttp",
    "DestinationRuleSpecTrafficPolicyConnectionPoolHttpH2UpgradePolicy",
    "DestinationRuleSpecTrafficPolicyConnectionPoolTcp",
    "DestinationRuleSpecTrafficPolicyConnectionPoolTcpTcpKeepalive",
    "DestinationRuleSpecTrafficPolicyLoadBalancer",
    "DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHash",
    "DestinationRuleSpecTrafficPolicyLoadBalancerConsistentHashHttpCookie",
    "DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSetting",
    "DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingDistribute",
    "DestinationRuleSpecTrafficPolicyLoadBalancerLocalityLbSettingFailover",
    "DestinationRuleSpecTrafficPolicyLoadBalancerSimple",
    "DestinationRuleSpecTrafficPolicyOutlierDetection",
    "DestinationRuleSpecTrafficPolicyPortLevelSettings",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPool",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttp",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolHttpH2UpgradePolicy",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcp",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsConnectionPoolTcpTcpKeepalive",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancer",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHash",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerConsistentHashHttpCookie",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSetting",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingDistribute",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerLocalityLbSettingFailover",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsLoadBalancerSimple",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsOutlierDetection",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsPort",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsTls",
    "DestinationRuleSpecTrafficPolicyPortLevelSettingsTlsMode",
    "DestinationRuleSpecTrafficPolicyTls",
    "DestinationRuleSpecTrafficPolicyTlsMode",
    "DestinationRuleSpecTrafficPolicyTunnel",
    "DestinationRuleSpecWorkloadSelector",
    "EnvoyFilter",
    "EnvoyFilterProps",
    "EnvoyFilterSpec",
    "EnvoyFilterSpecConfigPatches",
    "EnvoyFilterSpecConfigPatchesApplyTo",
    "EnvoyFilterSpecConfigPatchesMatch",
    "EnvoyFilterSpecConfigPatchesMatchCluster",
    "EnvoyFilterSpecConfigPatchesMatchContext",
    "EnvoyFilterSpecConfigPatchesMatchListener",
    "EnvoyFilterSpecConfigPatchesMatchListenerFilterChain",
    "EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilter",
    "EnvoyFilterSpecConfigPatchesMatchListenerFilterChainFilterSubFilter",
    "EnvoyFilterSpecConfigPatchesMatchProxy",
    "EnvoyFilterSpecConfigPatchesMatchRouteConfiguration",
    "EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhost",
    "EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRoute",
    "EnvoyFilterSpecConfigPatchesMatchRouteConfigurationVhostRouteAction",
    "EnvoyFilterSpecConfigPatchesPatch",
    "EnvoyFilterSpecConfigPatchesPatchFilterClass",
    "EnvoyFilterSpecConfigPatchesPatchOperation",
    "EnvoyFilterSpecWorkloadSelector",
    "Gateway",
    "GatewayProps",
    "GatewaySpec",
    "GatewaySpecServers",
    "GatewaySpecServersPort",
    "GatewaySpecServersTls",
    "GatewaySpecServersTlsMaxProtocolVersion",
    "GatewaySpecServersTlsMinProtocolVersion",
    "GatewaySpecServersTlsMode",
    "ProxyConfig",
    "ProxyConfigProps",
    "ProxyConfigSpec",
    "ProxyConfigSpecImage",
    "ProxyConfigSpecSelector",
    "ServiceEntry",
    "ServiceEntryProps",
    "ServiceEntrySpec",
    "ServiceEntrySpecEndpoints",
    "ServiceEntrySpecLocation",
    "ServiceEntrySpecPorts",
    "ServiceEntrySpecResolution",
    "ServiceEntrySpecWorkloadSelector",
    "Sidecar",
    "SidecarProps",
    "SidecarSpec",
    "SidecarSpecEgress",
    "SidecarSpecEgressCaptureMode",
    "SidecarSpecEgressPort",
    "SidecarSpecIngress",
    "SidecarSpecIngressCaptureMode",
    "SidecarSpecIngressPort",
    "SidecarSpecIngressTls",
    "SidecarSpecIngressTlsMaxProtocolVersion",
    "SidecarSpecIngressTlsMinProtocolVersion",
    "SidecarSpecIngressTlsMode",
    "SidecarSpecOutboundTrafficPolicy",
    "SidecarSpecOutboundTrafficPolicyEgressProxy",
    "SidecarSpecOutboundTrafficPolicyEgressProxyPort",
    "SidecarSpecOutboundTrafficPolicyMode",
    "SidecarSpecWorkloadSelector",
    "VirtualService",
    "VirtualServiceProps",
    "VirtualServiceSpec",
    "VirtualServiceSpecHttp",
    "VirtualServiceSpecHttpCorsPolicy",
    "VirtualServiceSpecHttpCorsPolicyAllowOrigins",
    "VirtualServiceSpecHttpDelegate",
    "VirtualServiceSpecHttpFault",
    "VirtualServiceSpecHttpFaultAbort",
    "VirtualServiceSpecHttpFaultAbortPercentage",
    "VirtualServiceSpecHttpFaultDelay",
    "VirtualServiceSpecHttpFaultDelayPercentage",
    "VirtualServiceSpecHttpHeaders",
    "VirtualServiceSpecHttpHeadersRequest",
    "VirtualServiceSpecHttpHeadersResponse",
    "VirtualServiceSpecHttpMatch",
    "VirtualServiceSpecHttpMatchAuthority",
    "VirtualServiceSpecHttpMatchHeaders",
    "VirtualServiceSpecHttpMatchMethod",
    "VirtualServiceSpecHttpMatchQueryParams",
    "VirtualServiceSpecHttpMatchScheme",
    "VirtualServiceSpecHttpMatchUri",
    "VirtualServiceSpecHttpMatchWithoutHeaders",
    "VirtualServiceSpecHttpMirror",
    "VirtualServiceSpecHttpMirrorPercentage",
    "VirtualServiceSpecHttpMirrorPort",
    "VirtualServiceSpecHttpRedirect",
    "VirtualServiceSpecHttpRedirectDerivePort",
    "VirtualServiceSpecHttpRetries",
    "VirtualServiceSpecHttpRewrite",
    "VirtualServiceSpecHttpRoute",
    "VirtualServiceSpecHttpRouteDestination",
    "VirtualServiceSpecHttpRouteDestinationPort",
    "VirtualServiceSpecHttpRouteHeaders",
    "VirtualServiceSpecHttpRouteHeadersRequest",
    "VirtualServiceSpecHttpRouteHeadersResponse",
    "VirtualServiceSpecTcp",
    "VirtualServiceSpecTcpMatch",
    "VirtualServiceSpecTcpRoute",
    "VirtualServiceSpecTcpRouteDestination",
    "VirtualServiceSpecTcpRouteDestinationPort",
    "VirtualServiceSpecTls",
    "VirtualServiceSpecTlsMatch",
    "VirtualServiceSpecTlsRoute",
    "VirtualServiceSpecTlsRouteDestination",
    "VirtualServiceSpecTlsRouteDestinationPort",
    "WorkloadEntry",
    "WorkloadEntryProps",
    "WorkloadEntrySpec",
    "WorkloadGroup",
    "WorkloadGroupProps",
    "WorkloadGroupSpec",
    "WorkloadGroupSpecMetadata",
    "WorkloadGroupSpecProbe",
    "WorkloadGroupSpecProbeExec",
    "WorkloadGroupSpecProbeHttpGet",
    "WorkloadGroupSpecProbeHttpGetHttpHeaders",
    "WorkloadGroupSpecProbeTcpSocket",
    "WorkloadGroupSpecTemplate",
]

publication.publish()
