from flask import Blueprint, render_template, request, redirect, url_for, request, flash

from prometheus import PrometheusClient
from flask_login import login_required
import rcon
import settings

usermgmt = Blueprint("usermgmt", __name__)
prom = PrometheusClient("localhost", 9090)
r_con = rcon.RCon(
    settings.RCON_HOST, settings.RCON_PORT, settings.RCON_PASS, settings.GMODES
)


@usermgmt.route("/usermgmt")
@login_required
def manage_userw():
    users = prom.get_players()
    return render_template("usermgmt.html", users=users, modes=settings.GMODES)


@usermgmt.route("/userop", methods=["POST"])
@login_required
def opuser():
    user = request.form.get("user")
    r_con.op_player(user)
    flash("User opped")
    return redirect("/usermgmt")


@usermgmt.route("/userdeop", methods=["POST"])
@login_required
def deopuser():
    user = request.form.get("user")
    r_con.deop_player(user)
    flash("User de-opped")
    return redirect("/usermgmt")


@usermgmt.route("/gamemode", methods=["POST"])
@login_required
def switch_gamemode():
    user = request.form.get("user")
    gmode = int(request.form.get("gmode"))
    flash("Gamemode changed for %s to %s " % (user, settings.GMODES[gmode]))

    r_con.set_gamemode_for_player(user, gmode)
    return redirect("/usermgmt")
