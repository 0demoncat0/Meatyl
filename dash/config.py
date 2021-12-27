from dash.api  import configfile

class Config:
    SECRET_KEY = configfile.clientSecret

    DISCORD_CLIENT_ID = configfile.clientID
    DISCORD_CLIENT_SECRET = configfile.clientSecret
    DISCORD_REDIRECT_URI = configfile.redirectURI
    #DISCORD_BOT_TOKEN = configfile.

    PTERO_URL = configfile.pteroURL
    PTERO_APP_KEY = configfile.pteroAppKey

    WEB_PORT = configfile.webport
    WEB_TITLE = configfile.webtitle
