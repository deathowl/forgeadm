import os

SERVER_PASS = os.environ.get("ARKPASS", "asdasd")
PORT = int(os.environ.get("PORT", 5000))
DEBUG = os.environ.get("FLASK_DEBUG", False)
SECRET_KEY = "asdasdsdsdda123123"
RCON_HOST = os.environ.get("RCON_HOST")
RCON_PORT = os.environ.get("RCON_HOST")
RCON_PASS = os.environ.get("RCON_PASSWORD")
PROMETHEUS_HOST = os.environ.get("PROMETHEUS_HOST")
PROMETHEUS_PORT = os.environ.get("PROMETHEUS_PORT")
FORGEDIR = os.environ.get("FORGE_DIR", "/opt/forge")
GMODES = {0: "survival", 1: "creative", 2: "adventure"}
