from prometheus_api_client import Metric, MetricsList, PrometheusConnect
import datetime


class PrometheusClient:
    def __init__(self, promhost, promport):
        self.prom = PrometheusConnect(
            url="http://%s:%s" % (promhost, promport), disable_ssl=True
        )

    def get_ticktime(self):
        return self.__get_metric_for_last_five_mins("overall_ticktime")[0].get("values")

    def get_dim_ticktime(self):
        result = {}
        dim_ticktimes = self.__get_metric_for_last_five_mins("dim_ticktime")
        for dimension in dim_ticktimes:
            result[dimension.get("metric").get("dimension_name")] = dimension.get(
                "values"
            )
        return result

    def get_players(self):
        players = []
        for p in self.prom.custom_query("player_playtime"):
            players.append(p.get("metric").get("player"))
        return players

    def get_tps(self):
        return self.__get_metric_for_last_five_mins("overall_tps")[0].get("values")

    def get_dim_tps(self):
        result = {}
        dim_tps = self.__get_metric_for_last_five_mins("dim_tps")
        for dimension in dim_tps:
            result[dimension.get("metric").get("dimension_name")] = dimension.get(
                "values"
            )
        return result

    def __get_metric_for_last_five_mins(self, metricname):
        return self.prom.get_metric_range_data(
            metric_name=metricname,
            start_time=datetime.datetime.now()
            - datetime.timedelta(minutes=5),
            end_time=datetime.datetime.now(),
        )
