import cdk8s_plus_24 as kplus

from cdk8s import App, Chart, ApiObjectMetadata
from constructs import Construct

from imports.io.istio.networking import Gateway, GatewaySpec,\
    GatewaySpecServers, GatewaySpecServersPort, VirtualService, \
    VirtualServiceSpec, VirtualServiceSpecHttp, VirtualServiceSpecHttpMatch, \
    VirtualServiceSpecHttpMatchUri, VirtualServiceSpecHttpRoute, \
    VirtualServiceSpecHttpRouteDestination, \
    VirtualServiceSpecHttpRouteDestinationPort


class HelloWorldChart(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Create a service
        service = kplus.Service(
            self, "Service",
            metadata=ApiObjectMetadata(
                labels={"app": "helloworld", "service": "helloworld"}),
            ports=[kplus.ServicePort(name="http", port=5000)]
        )
        service.select_label(key="app", value="helloworld")

        # Create `v1` and `v2` deployments
        [self.deployment(v) for v in ["v1", "v2"]]

        # Create istio gateway
        gateway = Gateway(
            self, "Gateway",
            spec=GatewaySpec(
                selector={"istio": "ingressgateway"},
                servers=[
                    GatewaySpecServers(
                        port=GatewaySpecServersPort(
                            number=80, name="http", protocol="HTTP"),
                        hosts=["*"]
                    )
                ]
            )
        )

        # Create istio virtual service
        VirtualService(
            self, "VirtualService",
            spec=VirtualServiceSpec(
                hosts=["*"],
                gateways=[gateway.name],
                http=[
                    VirtualServiceSpecHttp(
                        match=[
                            VirtualServiceSpecHttpMatch(
                                uri=VirtualServiceSpecHttpMatchUri(
                                    exact="/hello")
                            )
                        ],
                        route=[
                            VirtualServiceSpecHttpRoute(
                                destination=VirtualServiceSpecHttpRouteDestination(
                                    host="helloworld",
                                    port=VirtualServiceSpecHttpRouteDestinationPort(
                                        number=5000)
                                )
                            )
                        ]
                    )
                ]
            )
        )

    def deployment(self, version: str):
        # Labels for metadata
        labels = {"app": "helloworld", "version": version}

        # Resource request
        cpu_request = kplus.CpuResources(request=kplus.Cpu.millis(100))

        # Create a deployment
        kplus.Deployment(
            self, f"Deployment-{version}",
            replicas=1,
            metadata=ApiObjectMetadata(labels=labels),
            pod_metadata=ApiObjectMetadata(labels=labels),
            containers=[
                kplus.ContainerProps(
                    name="helloworld",
                    image=f"docker.io/istio/examples-helloworld-{version}",
                    image_pull_policy=kplus.ImagePullPolicy.IF_NOT_PRESENT,
                    port=5000,
                    resources=kplus.ContainerResources(cpu=cpu_request)
                )
            ]
        )


if __name__ == "__main__":
    app = App()
    HelloWorldChart(app, "helloworld")

    app.synth()
