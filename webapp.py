from flask import Flask
from flask_login import LoginManager
from settings import SERVER_PASS, PORT, DEBUG, SECRET_KEY
from auth import User


def create_app():
    app = Flask(__name__)

    app.config["SERVER_PASS"] = SERVER_PASS
    app.config["SECRET_KEY"] = SECRET_KEY
    login_manager = LoginManager()

    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(email):
        user = User()
        return user

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app


application = create_app()

if __name__ == "__main__":
    application.run("0.0.0.0", port=PORT, debug=DEBUG)
