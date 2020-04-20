from flask import Blueprint, render_template, request, redirect, url_for
import manager
from service import ForgeService
from flask_login import login_required

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/server")
@login_required
def server():
    service_status = ForgeService().status()
    mods=manager.Manager("/opt/forge").get_installed_mods()
    #service_status = b'active'.decode("utf-8") 
    return render_template("server.html", service_status=service_status, installed_mods=mods)

@main.route("/server", methods=["POST"])
@login_required
def server_manage():
    desired_status = int(request.values.get("status"))
    if desired_status == 0:
        ForgeService().stop()
    else:
        ForgeService().start()
    return redirect(url_for("main.server"))
