# MyForge(Forgeadm)

Welcome to MyForge.
Please be aware, that this is a hack piggybacking off [Prometheus](https://prometheus.io/), [Minecraft exporter,](https://github.com/deathowl/minecraft-exporter) systemd, dbus and many open source libraries (see requirements.txt).

There is no guarantee it will work for you, it works for us, and we are happy with it.

There is absolutely no warranty that your server and all your data will not disappear if you use this service, because it was made super haphazardly, applying glue to places where needed and taking html templates from floating around on the web, while consuming moderate amounts of alcohol.
However if you want to use it, we highly recommend to do so, using our systemd service for your forge instance found under extras/minecraft.service
To run this process please use systemd also with the extras/myforge.service unit.
Make sure your Forge server has RCON enabled for user mode settings and backup features.

# Run it (Are you sure? Ok then)
* Have a prometheus instance, that is collecting data from minecraft-exporter
* Clone the repo
*  pip3 install -r requirements.txt
* place systemd units in place
* Chenge systemd unit accordingly (Rcon and forge dirs, dir of myforge)
* systemctl daemon-reload
* systemctl start arkadmin
* add Nginx in front FFS


# Features
* Save world from the web-ui
* Start/stop the Forge instance
* op/de-op/set gamemode for any online player
* See charts about your minecraft instane
* List installed mods
* Admire the snowflakes on the landingpage

# Screenshots:

![charts](https://github.com/deathowl/forgeadm/raw/master/screenhots/charts.png)
![user management](https://github.com/deathowl/forgeadm/raw/master/screenhots/usermgmt.png)



# Credits
Made by deathowl and samlindev.
Inspired by Hajmalka, because "The server is dooooown"

