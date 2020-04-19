from flask import Blueprint, request, redirect, url_for, jsonify

from service import ForgeService
from flask_login import login_required
from prometheus import PrometheusClient

metrics = Blueprint("metrics", __name__)
prom = PrometheusClient("mcr.samlindev.eu", 9090)


@metrics.route("/metrics/tps")
@login_required
def tps():
    return jsonify(prom.get_tps())

@metrics.route("/metrics/ticktime")
@login_required
def ticktime():
    return jsonify(prom.get_ticktime())

@metrics.route("/metrics/dim_tps")
@login_required
def dim_tps():
    return jsonify(prom.get_dim_tps())


@metrics.route("/metrics/dim_ticktime")
@login_required
def dim_ticktime():
    return jsonify(prom.get_dim_ticktime())

