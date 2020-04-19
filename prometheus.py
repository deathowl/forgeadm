from prometheus_api_client import Metric, MetricsList, PrometheusConnect

class PrometheusClient():
    def __init__(self, promhost, promport):
        pc = PrometheusConnect(url="http://prometheus-route-aiops-prod-prometheus-predict.cloud.paas.psi.redhat.com", disable_ssl=True)
