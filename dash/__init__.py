from flask import Flask
from dash.config import Config
from flask_discord import DiscordOAuth2Session
import os

import dash

discord = DiscordOAuth2Session()

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"
    os.environ["FLASK_ENV"] = "development"
    
    from dash.routes.index import index
    from dash.routes.users import users
    from dash.routes.dashboard import dashboard
    from dash.routes.servers import server 
    from dash.errors.handlers import errors

    app.register_blueprint(index)
    app.register_blueprint(users)
    app.register_blueprint(dashboard)
    app.register_blueprint(errors)
    app.register_blueprint(server)
    app.discord = DiscordOAuth2Session(app)

    discord.init_app(app)

    return app
