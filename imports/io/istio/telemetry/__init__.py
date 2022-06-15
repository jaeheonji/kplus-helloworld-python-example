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


class Telemetry(
    cdk8s.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="ioistiotelemetry.Telemetry",
):
    '''
    :schema: Telemetry
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["TelemetrySpec"] = None,
    ) -> None:
        '''Defines a "Telemetry" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: Telemetry configuration for workloads. See more details at: https://istio.io/docs/reference/config/telemetry.html
        '''
        props = TelemetryProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest") # type: ignore[misc]
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["TelemetrySpec"] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "Telemetry".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: Telemetry configuration for workloads. See more details at: https://istio.io/docs/reference/config/telemetry.html
        '''
        props = TelemetryProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> cdk8s.GroupVersionKind:
        '''Returns the apiVersion and kind for "Telemetry".'''
        return typing.cast(cdk8s.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetryProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class TelemetryProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[cdk8s.ApiObjectMetadata] = None,
        spec: typing.Optional["TelemetrySpec"] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: Telemetry configuration for workloads. See more details at: https://istio.io/docs/reference/config/telemetry.html

        :schema: Telemetry
        '''
        if isinstance(metadata, dict):
            metadata = cdk8s.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = TelemetrySpec(**spec)
        self._values: typing.Dict[str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[cdk8s.ApiObjectMetadata]:
        '''
        :schema: Telemetry#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[cdk8s.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["TelemetrySpec"]:
        '''Telemetry configuration for workloads.

        See more details at: https://istio.io/docs/reference/config/telemetry.html

        :schema: Telemetry#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["TelemetrySpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpec",
    jsii_struct_bases=[],
    name_mapping={
        "access_logging": "accessLogging",
        "metrics": "metrics",
        "selector": "selector",
        "tracing": "tracing",
    },
)
class TelemetrySpec:
    def __init__(
        self,
        *,
        access_logging: typing.Optional[typing.Sequence["TelemetrySpecAccessLogging"]] = None,
        metrics: typing.Optional[typing.Sequence["TelemetrySpecMetrics"]] = None,
        selector: typing.Optional["TelemetrySpecSelector"] = None,
        tracing: typing.Optional[typing.Sequence["TelemetrySpecTracing"]] = None,
    ) -> None:
        '''Telemetry configuration for workloads.

        See more details at: https://istio.io/docs/reference/config/telemetry.html

        :param access_logging: Optional.
        :param metrics: Optional.
        :param selector: Optional.
        :param tracing: Optional.

        :schema: TelemetrySpec
        '''
        if isinstance(selector, dict):
            selector = TelemetrySpecSelector(**selector)
        self._values: typing.Dict[str, typing.Any] = {}
        if access_logging is not None:
            self._values["access_logging"] = access_logging
        if metrics is not None:
            self._values["metrics"] = metrics
        if selector is not None:
            self._values["selector"] = selector
        if tracing is not None:
            self._values["tracing"] = tracing

    @builtins.property
    def access_logging(
        self,
    ) -> typing.Optional[typing.List["TelemetrySpecAccessLogging"]]:
        '''Optional.

        :schema: TelemetrySpec#accessLogging
        '''
        result = self._values.get("access_logging")
        return typing.cast(typing.Optional[typing.List["TelemetrySpecAccessLogging"]], result)

    @builtins.property
    def metrics(self) -> typing.Optional[typing.List["TelemetrySpecMetrics"]]:
        '''Optional.

        :schema: TelemetrySpec#metrics
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional[typing.List["TelemetrySpecMetrics"]], result)

    @builtins.property
    def selector(self) -> typing.Optional["TelemetrySpecSelector"]:
        '''Optional.

        :schema: TelemetrySpec#selector
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional["TelemetrySpecSelector"], result)

    @builtins.property
    def tracing(self) -> typing.Optional[typing.List["TelemetrySpecTracing"]]:
        '''Optional.

        :schema: TelemetrySpec#tracing
        '''
        result = self._values.get("tracing")
        return typing.cast(typing.Optional[typing.List["TelemetrySpecTracing"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecAccessLogging",
    jsii_struct_bases=[],
    name_mapping={
        "disabled": "disabled",
        "filter": "filter",
        "match": "match",
        "providers": "providers",
    },
)
class TelemetrySpecAccessLogging:
    def __init__(
        self,
        *,
        disabled: typing.Optional[builtins.bool] = None,
        filter: typing.Optional["TelemetrySpecAccessLoggingFilter"] = None,
        match: typing.Optional["TelemetrySpecAccessLoggingMatch"] = None,
        providers: typing.Optional[typing.Sequence["TelemetrySpecAccessLoggingProviders"]] = None,
    ) -> None:
        '''
        :param disabled: Controls logging.
        :param filter: Optional.
        :param match: Allows tailoring of logging behavior to specific conditions.
        :param providers: Optional.

        :schema: TelemetrySpecAccessLogging
        '''
        if isinstance(filter, dict):
            filter = TelemetrySpecAccessLoggingFilter(**filter)
        if isinstance(match, dict):
            match = TelemetrySpecAccessLoggingMatch(**match)
        self._values: typing.Dict[str, typing.Any] = {}
        if disabled is not None:
            self._values["disabled"] = disabled
        if filter is not None:
            self._values["filter"] = filter
        if match is not None:
            self._values["match"] = match
        if providers is not None:
            self._values["providers"] = providers

    @builtins.property
    def disabled(self) -> typing.Optional[builtins.bool]:
        '''Controls logging.

        :schema: TelemetrySpecAccessLogging#disabled
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def filter(self) -> typing.Optional["TelemetrySpecAccessLoggingFilter"]:
        '''Optional.

        :schema: TelemetrySpecAccessLogging#filter
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional["TelemetrySpecAccessLoggingFilter"], result)

    @builtins.property
    def match(self) -> typing.Optional["TelemetrySpecAccessLoggingMatch"]:
        '''Allows tailoring of logging behavior to specific conditions.

        :schema: TelemetrySpecAccessLogging#match
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional["TelemetrySpecAccessLoggingMatch"], result)

    @builtins.property
    def providers(
        self,
    ) -> typing.Optional[typing.List["TelemetrySpecAccessLoggingProviders"]]:
        '''Optional.

        :schema: TelemetrySpecAccessLogging#providers
        '''
        result = self._values.get("providers")
        return typing.cast(typing.Optional[typing.List["TelemetrySpecAccessLoggingProviders"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecAccessLogging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecAccessLoggingFilter",
    jsii_struct_bases=[],
    name_mapping={"expression": "expression"},
)
class TelemetrySpecAccessLoggingFilter:
    def __init__(self, *, expression: typing.Optional[builtins.str] = None) -> None:
        '''Optional.

        :param expression: CEL expression for selecting when requests/connections should be logged.

        :schema: TelemetrySpecAccessLoggingFilter
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if expression is not None:
            self._values["expression"] = expression

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''CEL expression for selecting when requests/connections should be logged.

        :schema: TelemetrySpecAccessLoggingFilter#expression
        '''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecAccessLoggingFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecAccessLoggingMatch",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode"},
)
class TelemetrySpecAccessLoggingMatch:
    def __init__(
        self,
        *,
        mode: typing.Optional["TelemetrySpecAccessLoggingMatchMode"] = None,
    ) -> None:
        '''Allows tailoring of logging behavior to specific conditions.

        :param mode: 

        :schema: TelemetrySpecAccessLoggingMatch
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def mode(self) -> typing.Optional["TelemetrySpecAccessLoggingMatchMode"]:
        '''
        :schema: TelemetrySpecAccessLoggingMatch#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["TelemetrySpecAccessLoggingMatchMode"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecAccessLoggingMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistiotelemetry.TelemetrySpecAccessLoggingMatchMode")
class TelemetrySpecAccessLoggingMatchMode(enum.Enum):
    '''
    :schema: TelemetrySpecAccessLoggingMatchMode
    '''

    CLIENT_AND_SERVER = "CLIENT_AND_SERVER"
    '''CLIENT_AND_SERVER.'''
    CLIENT = "CLIENT"
    '''CLIENT.'''
    SERVER = "SERVER"
    '''SERVER.'''


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecAccessLoggingProviders",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class TelemetrySpecAccessLoggingProviders:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param name: Required.

        :schema: TelemetrySpecAccessLoggingProviders
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Required.

        :schema: TelemetrySpecAccessLoggingProviders#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecAccessLoggingProviders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecMetrics",
    jsii_struct_bases=[],
    name_mapping={"overrides": "overrides", "providers": "providers"},
)
class TelemetrySpecMetrics:
    def __init__(
        self,
        *,
        overrides: typing.Optional[typing.Sequence["TelemetrySpecMetricsOverrides"]] = None,
        providers: typing.Optional[typing.Sequence["TelemetrySpecMetricsProviders"]] = None,
    ) -> None:
        '''
        :param overrides: Optional.
        :param providers: Optional.

        :schema: TelemetrySpecMetrics
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if overrides is not None:
            self._values["overrides"] = overrides
        if providers is not None:
            self._values["providers"] = providers

    @builtins.property
    def overrides(
        self,
    ) -> typing.Optional[typing.List["TelemetrySpecMetricsOverrides"]]:
        '''Optional.

        :schema: TelemetrySpecMetrics#overrides
        '''
        result = self._values.get("overrides")
        return typing.cast(typing.Optional[typing.List["TelemetrySpecMetricsOverrides"]], result)

    @builtins.property
    def providers(
        self,
    ) -> typing.Optional[typing.List["TelemetrySpecMetricsProviders"]]:
        '''Optional.

        :schema: TelemetrySpecMetrics#providers
        '''
        result = self._values.get("providers")
        return typing.cast(typing.Optional[typing.List["TelemetrySpecMetricsProviders"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecMetricsOverrides",
    jsii_struct_bases=[],
    name_mapping={
        "disabled": "disabled",
        "match": "match",
        "tag_overrides": "tagOverrides",
    },
)
class TelemetrySpecMetricsOverrides:
    def __init__(
        self,
        *,
        disabled: typing.Optional[builtins.bool] = None,
        match: typing.Optional["TelemetrySpecMetricsOverridesMatch"] = None,
        tag_overrides: typing.Optional[typing.Mapping[builtins.str, "TelemetrySpecMetricsOverridesTagOverrides"]] = None,
    ) -> None:
        '''
        :param disabled: Optional.
        :param match: Match allows provides the scope of the override.
        :param tag_overrides: Optional.

        :schema: TelemetrySpecMetricsOverrides
        '''
        if isinstance(match, dict):
            match = TelemetrySpecMetricsOverridesMatch(**match)
        self._values: typing.Dict[str, typing.Any] = {}
        if disabled is not None:
            self._values["disabled"] = disabled
        if match is not None:
            self._values["match"] = match
        if tag_overrides is not None:
            self._values["tag_overrides"] = tag_overrides

    @builtins.property
    def disabled(self) -> typing.Optional[builtins.bool]:
        '''Optional.

        :schema: TelemetrySpecMetricsOverrides#disabled
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def match(self) -> typing.Optional["TelemetrySpecMetricsOverridesMatch"]:
        '''Match allows provides the scope of the override.

        :schema: TelemetrySpecMetricsOverrides#match
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional["TelemetrySpecMetricsOverridesMatch"], result)

    @builtins.property
    def tag_overrides(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "TelemetrySpecMetricsOverridesTagOverrides"]]:
        '''Optional.

        :schema: TelemetrySpecMetricsOverrides#tagOverrides
        '''
        result = self._values.get("tag_overrides")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "TelemetrySpecMetricsOverridesTagOverrides"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecMetricsOverrides(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecMetricsOverridesMatch",
    jsii_struct_bases=[],
    name_mapping={"custom_metric": "customMetric", "metric": "metric", "mode": "mode"},
)
class TelemetrySpecMetricsOverridesMatch:
    def __init__(
        self,
        *,
        custom_metric: typing.Optional[builtins.str] = None,
        metric: typing.Optional["TelemetrySpecMetricsOverridesMatchMetric"] = None,
        mode: typing.Optional["TelemetrySpecMetricsOverridesMatchMode"] = None,
    ) -> None:
        '''Match allows provides the scope of the override.

        :param custom_metric: Allows free-form specification of a metric.
        :param metric: One of the well-known Istio Standard Metrics.
        :param mode: 

        :schema: TelemetrySpecMetricsOverridesMatch
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_metric is not None:
            self._values["custom_metric"] = custom_metric
        if metric is not None:
            self._values["metric"] = metric
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def custom_metric(self) -> typing.Optional[builtins.str]:
        '''Allows free-form specification of a metric.

        :schema: TelemetrySpecMetricsOverridesMatch#customMetric
        '''
        result = self._values.get("custom_metric")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric(self) -> typing.Optional["TelemetrySpecMetricsOverridesMatchMetric"]:
        '''One of the well-known Istio Standard Metrics.

        :schema: TelemetrySpecMetricsOverridesMatch#metric
        '''
        result = self._values.get("metric")
        return typing.cast(typing.Optional["TelemetrySpecMetricsOverridesMatchMetric"], result)

    @builtins.property
    def mode(self) -> typing.Optional["TelemetrySpecMetricsOverridesMatchMode"]:
        '''
        :schema: TelemetrySpecMetricsOverridesMatch#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["TelemetrySpecMetricsOverridesMatchMode"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecMetricsOverridesMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistiotelemetry.TelemetrySpecMetricsOverridesMatchMetric")
class TelemetrySpecMetricsOverridesMatchMetric(enum.Enum):
    '''One of the well-known Istio Standard Metrics.

    :schema: TelemetrySpecMetricsOverridesMatchMetric
    '''

    ALL_METRICS = "ALL_METRICS"
    '''ALL_METRICS.'''
    REQUEST_COUNT = "REQUEST_COUNT"
    '''REQUEST_COUNT.'''
    REQUEST_DURATION = "REQUEST_DURATION"
    '''REQUEST_DURATION.'''
    REQUEST_SIZE = "REQUEST_SIZE"
    '''REQUEST_SIZE.'''
    RESPONSE_SIZE = "RESPONSE_SIZE"
    '''RESPONSE_SIZE.'''
    TCP_OPENED_CONNECTIONS = "TCP_OPENED_CONNECTIONS"
    '''TCP_OPENED_CONNECTIONS.'''
    TCP_CLOSED_CONNECTIONS = "TCP_CLOSED_CONNECTIONS"
    '''TCP_CLOSED_CONNECTIONS.'''
    TCP_SENT_BYTES = "TCP_SENT_BYTES"
    '''TCP_SENT_BYTES.'''
    TCP_RECEIVED_BYTES = "TCP_RECEIVED_BYTES"
    '''TCP_RECEIVED_BYTES.'''
    GRPC_REQUEST_MESSAGES = "GRPC_REQUEST_MESSAGES"
    '''GRPC_REQUEST_MESSAGES.'''
    GRPC_RESPONSE_MESSAGES = "GRPC_RESPONSE_MESSAGES"
    '''GRPC_RESPONSE_MESSAGES.'''


@jsii.enum(jsii_type="ioistiotelemetry.TelemetrySpecMetricsOverridesMatchMode")
class TelemetrySpecMetricsOverridesMatchMode(enum.Enum):
    '''
    :schema: TelemetrySpecMetricsOverridesMatchMode
    '''

    CLIENT_AND_SERVER = "CLIENT_AND_SERVER"
    '''CLIENT_AND_SERVER.'''
    CLIENT = "CLIENT"
    '''CLIENT.'''
    SERVER = "SERVER"
    '''SERVER.'''


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecMetricsOverridesTagOverrides",
    jsii_struct_bases=[],
    name_mapping={"operation": "operation", "value": "value"},
)
class TelemetrySpecMetricsOverridesTagOverrides:
    def __init__(
        self,
        *,
        operation: typing.Optional["TelemetrySpecMetricsOverridesTagOverridesOperation"] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param operation: Operation controls whether or not to update/add a tag, or to remove it.
        :param value: Value is only considered if the operation is ``UPSERT``.

        :schema: TelemetrySpecMetricsOverridesTagOverrides
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if operation is not None:
            self._values["operation"] = operation
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def operation(
        self,
    ) -> typing.Optional["TelemetrySpecMetricsOverridesTagOverridesOperation"]:
        '''Operation controls whether or not to update/add a tag, or to remove it.

        :schema: TelemetrySpecMetricsOverridesTagOverrides#operation
        '''
        result = self._values.get("operation")
        return typing.cast(typing.Optional["TelemetrySpecMetricsOverridesTagOverridesOperation"], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value is only considered if the operation is ``UPSERT``.

        :schema: TelemetrySpecMetricsOverridesTagOverrides#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecMetricsOverridesTagOverrides(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="ioistiotelemetry.TelemetrySpecMetricsOverridesTagOverridesOperation"
)
class TelemetrySpecMetricsOverridesTagOverridesOperation(enum.Enum):
    '''Operation controls whether or not to update/add a tag, or to remove it.

    :schema: TelemetrySpecMetricsOverridesTagOverridesOperation
    '''

    UPSERT = "UPSERT"
    '''UPSERT.'''
    REMOVE = "REMOVE"
    '''REMOVE.'''


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecMetricsProviders",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class TelemetrySpecMetricsProviders:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param name: Required.

        :schema: TelemetrySpecMetricsProviders
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Required.

        :schema: TelemetrySpecMetricsProviders#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecMetricsProviders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecSelector",
    jsii_struct_bases=[],
    name_mapping={"match_labels": "matchLabels"},
)
class TelemetrySpecSelector:
    def __init__(
        self,
        *,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Optional.

        :param match_labels: 

        :schema: TelemetrySpecSelector
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :schema: TelemetrySpecSelector#matchLabels
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecTracing",
    jsii_struct_bases=[],
    name_mapping={
        "custom_tags": "customTags",
        "disable_span_reporting": "disableSpanReporting",
        "match": "match",
        "providers": "providers",
        "random_sampling_percentage": "randomSamplingPercentage",
        "use_request_id_for_trace_sampling": "useRequestIdForTraceSampling",
    },
)
class TelemetrySpecTracing:
    def __init__(
        self,
        *,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, "TelemetrySpecTracingCustomTags"]] = None,
        disable_span_reporting: typing.Optional[builtins.bool] = None,
        match: typing.Optional["TelemetrySpecTracingMatch"] = None,
        providers: typing.Optional[typing.Sequence["TelemetrySpecTracingProviders"]] = None,
        random_sampling_percentage: typing.Optional[jsii.Number] = None,
        use_request_id_for_trace_sampling: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param custom_tags: Optional.
        :param disable_span_reporting: Controls span reporting.
        :param match: Allows tailoring of behavior to specific conditions.
        :param providers: Optional.
        :param random_sampling_percentage: 
        :param use_request_id_for_trace_sampling: 

        :schema: TelemetrySpecTracing
        '''
        if isinstance(match, dict):
            match = TelemetrySpecTracingMatch(**match)
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_tags is not None:
            self._values["custom_tags"] = custom_tags
        if disable_span_reporting is not None:
            self._values["disable_span_reporting"] = disable_span_reporting
        if match is not None:
            self._values["match"] = match
        if providers is not None:
            self._values["providers"] = providers
        if random_sampling_percentage is not None:
            self._values["random_sampling_percentage"] = random_sampling_percentage
        if use_request_id_for_trace_sampling is not None:
            self._values["use_request_id_for_trace_sampling"] = use_request_id_for_trace_sampling

    @builtins.property
    def custom_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "TelemetrySpecTracingCustomTags"]]:
        '''Optional.

        :schema: TelemetrySpecTracing#customTags
        '''
        result = self._values.get("custom_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "TelemetrySpecTracingCustomTags"]], result)

    @builtins.property
    def disable_span_reporting(self) -> typing.Optional[builtins.bool]:
        '''Controls span reporting.

        :schema: TelemetrySpecTracing#disableSpanReporting
        '''
        result = self._values.get("disable_span_reporting")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def match(self) -> typing.Optional["TelemetrySpecTracingMatch"]:
        '''Allows tailoring of behavior to specific conditions.

        :schema: TelemetrySpecTracing#match
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional["TelemetrySpecTracingMatch"], result)

    @builtins.property
    def providers(
        self,
    ) -> typing.Optional[typing.List["TelemetrySpecTracingProviders"]]:
        '''Optional.

        :schema: TelemetrySpecTracing#providers
        '''
        result = self._values.get("providers")
        return typing.cast(typing.Optional[typing.List["TelemetrySpecTracingProviders"]], result)

    @builtins.property
    def random_sampling_percentage(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: TelemetrySpecTracing#randomSamplingPercentage
        '''
        result = self._values.get("random_sampling_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def use_request_id_for_trace_sampling(self) -> typing.Optional[builtins.bool]:
        '''
        :schema: TelemetrySpecTracing#useRequestIdForTraceSampling
        '''
        result = self._values.get("use_request_id_for_trace_sampling")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecTracing(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecTracingCustomTags",
    jsii_struct_bases=[],
    name_mapping={
        "environment": "environment",
        "header": "header",
        "literal": "literal",
    },
)
class TelemetrySpecTracingCustomTags:
    def __init__(
        self,
        *,
        environment: typing.Optional["TelemetrySpecTracingCustomTagsEnvironment"] = None,
        header: typing.Optional["TelemetrySpecTracingCustomTagsHeader"] = None,
        literal: typing.Optional["TelemetrySpecTracingCustomTagsLiteral"] = None,
    ) -> None:
        '''
        :param environment: Environment adds the value of an environment variable to each span.
        :param header: 
        :param literal: Literal adds the same, hard-coded value to each span.

        :schema: TelemetrySpecTracingCustomTags
        '''
        if isinstance(environment, dict):
            environment = TelemetrySpecTracingCustomTagsEnvironment(**environment)
        if isinstance(header, dict):
            header = TelemetrySpecTracingCustomTagsHeader(**header)
        if isinstance(literal, dict):
            literal = TelemetrySpecTracingCustomTagsLiteral(**literal)
        self._values: typing.Dict[str, typing.Any] = {}
        if environment is not None:
            self._values["environment"] = environment
        if header is not None:
            self._values["header"] = header
        if literal is not None:
            self._values["literal"] = literal

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional["TelemetrySpecTracingCustomTagsEnvironment"]:
        '''Environment adds the value of an environment variable to each span.

        :schema: TelemetrySpecTracingCustomTags#environment
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional["TelemetrySpecTracingCustomTagsEnvironment"], result)

    @builtins.property
    def header(self) -> typing.Optional["TelemetrySpecTracingCustomTagsHeader"]:
        '''
        :schema: TelemetrySpecTracingCustomTags#header
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional["TelemetrySpecTracingCustomTagsHeader"], result)

    @builtins.property
    def literal(self) -> typing.Optional["TelemetrySpecTracingCustomTagsLiteral"]:
        '''Literal adds the same, hard-coded value to each span.

        :schema: TelemetrySpecTracingCustomTags#literal
        '''
        result = self._values.get("literal")
        return typing.cast(typing.Optional["TelemetrySpecTracingCustomTagsLiteral"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecTracingCustomTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecTracingCustomTagsEnvironment",
    jsii_struct_bases=[],
    name_mapping={"default_value": "defaultValue", "name": "name"},
)
class TelemetrySpecTracingCustomTagsEnvironment:
    def __init__(
        self,
        *,
        default_value: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Environment adds the value of an environment variable to each span.

        :param default_value: Optional.
        :param name: Name of the environment variable from which to extract the tag value.

        :schema: TelemetrySpecTracingCustomTagsEnvironment
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if default_value is not None:
            self._values["default_value"] = default_value
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def default_value(self) -> typing.Optional[builtins.str]:
        '''Optional.

        :schema: TelemetrySpecTracingCustomTagsEnvironment#defaultValue
        '''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the environment variable from which to extract the tag value.

        :schema: TelemetrySpecTracingCustomTagsEnvironment#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecTracingCustomTagsEnvironment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecTracingCustomTagsHeader",
    jsii_struct_bases=[],
    name_mapping={"default_value": "defaultValue", "name": "name"},
)
class TelemetrySpecTracingCustomTagsHeader:
    def __init__(
        self,
        *,
        default_value: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_value: Optional.
        :param name: Name of the header from which to extract the tag value.

        :schema: TelemetrySpecTracingCustomTagsHeader
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if default_value is not None:
            self._values["default_value"] = default_value
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def default_value(self) -> typing.Optional[builtins.str]:
        '''Optional.

        :schema: TelemetrySpecTracingCustomTagsHeader#defaultValue
        '''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the header from which to extract the tag value.

        :schema: TelemetrySpecTracingCustomTagsHeader#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecTracingCustomTagsHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecTracingCustomTagsLiteral",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class TelemetrySpecTracingCustomTagsLiteral:
    def __init__(self, *, value: typing.Optional[builtins.str] = None) -> None:
        '''Literal adds the same, hard-coded value to each span.

        :param value: The tag value to use.

        :schema: TelemetrySpecTracingCustomTagsLiteral
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The tag value to use.

        :schema: TelemetrySpecTracingCustomTagsLiteral#value
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecTracingCustomTagsLiteral(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecTracingMatch",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode"},
)
class TelemetrySpecTracingMatch:
    def __init__(
        self,
        *,
        mode: typing.Optional["TelemetrySpecTracingMatchMode"] = None,
    ) -> None:
        '''Allows tailoring of behavior to specific conditions.

        :param mode: 

        :schema: TelemetrySpecTracingMatch
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def mode(self) -> typing.Optional["TelemetrySpecTracingMatchMode"]:
        '''
        :schema: TelemetrySpecTracingMatch#mode
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["TelemetrySpecTracingMatchMode"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecTracingMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="ioistiotelemetry.TelemetrySpecTracingMatchMode")
class TelemetrySpecTracingMatchMode(enum.Enum):
    '''
    :schema: TelemetrySpecTracingMatchMode
    '''

    CLIENT_AND_SERVER = "CLIENT_AND_SERVER"
    '''CLIENT_AND_SERVER.'''
    CLIENT = "CLIENT"
    '''CLIENT.'''
    SERVER = "SERVER"
    '''SERVER.'''


@jsii.data_type(
    jsii_type="ioistiotelemetry.TelemetrySpecTracingProviders",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class TelemetrySpecTracingProviders:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param name: Required.

        :schema: TelemetrySpecTracingProviders
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Required.

        :schema: TelemetrySpecTracingProviders#name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetrySpecTracingProviders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Telemetry",
    "TelemetryProps",
    "TelemetrySpec",
    "TelemetrySpecAccessLogging",
    "TelemetrySpecAccessLoggingFilter",
    "TelemetrySpecAccessLoggingMatch",
    "TelemetrySpecAccessLoggingMatchMode",
    "TelemetrySpecAccessLoggingProviders",
    "TelemetrySpecMetrics",
    "TelemetrySpecMetricsOverrides",
    "TelemetrySpecMetricsOverridesMatch",
    "TelemetrySpecMetricsOverridesMatchMetric",
    "TelemetrySpecMetricsOverridesMatchMode",
    "TelemetrySpecMetricsOverridesTagOverrides",
    "TelemetrySpecMetricsOverridesTagOverridesOperation",
    "TelemetrySpecMetricsProviders",
    "TelemetrySpecSelector",
    "TelemetrySpecTracing",
    "TelemetrySpecTracingCustomTags",
    "TelemetrySpecTracingCustomTagsEnvironment",
    "TelemetrySpecTracingCustomTagsHeader",
    "TelemetrySpecTracingCustomTagsLiteral",
    "TelemetrySpecTracingMatch",
    "TelemetrySpecTracingMatchMode",
    "TelemetrySpecTracingProviders",
]

publication.publish()
