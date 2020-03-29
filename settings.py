import os

SERVER_PASS = os.environ.get("ARKPASS", "asdasd")
PORT = int(os.environ.get("PORT", 5000))
DEBUG = os.environ.get("FLASK_DEBUG", False)
SECRET_KEY = "asdasdsdsdda123123"
