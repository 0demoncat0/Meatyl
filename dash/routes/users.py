from flask import Blueprint, redirect, url_for, render_template, current_app
from dash import discord
from dash.api import userdata

users = Blueprint('users', __name__)



@users.route("/create")
def createuser():
    user = discord.fetch_user()
    userdata.create_user(user.name, user.email, user.id, user.discriminator)
    return render_template("dashboard.html", user=user, panellink=current_app.config['PTERO_APP_KEY'])

