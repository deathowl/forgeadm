from flask import Blueprint, render_template, request, redirect, url_for, flash
import manager
from service import ForgeService
from flask_login import login_required
from settings import FORGEDIR, RCON_HOST, RCON_PORT, RCON_PASS
import rcon

main = Blueprint("main", __name__)
r_con = rcon.RCon(
    RCON_HOST, RCON_PORT, RCON_PASS, {}
)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/server")
@login_required
def server():
    service_status = ForgeService().status()
    mods = manager.Manager(FORGEDIR).get_installed_mods()
    # service_status = b'active'.decode("utf-8")
    return render_template(
        "server.html", service_status=service_status, installed_mods=mods
    )


@main.route("/server", methods=["POST"])
@login_required
def server_manage():
    desired_status = int(request.values.get("status"))
    if desired_status == 0:
        ForgeService().stop()
    else:
        ForgeService().start()
    return redirect(url_for("main.server"))

@main.route("/trigger-save", methods=["POST"])
@login_required
def trigger_save():
    r_con.trigger_save()
    flash("Save triggered")
    return redirect(url_for("main.server"))