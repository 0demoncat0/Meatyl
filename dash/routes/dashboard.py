from flask import Blueprint, redirect, url_for, render_template, current_app
from dash import discord
from flask_discord import requires_authorization
dashboard = Blueprint('dashboard', __name__)


@dashboard.route("/login")
def login():
	return discord.create_session()

@dashboard.route('/callback')
def callback():
    discord.callback()
    return redirect(url_for('index.home'))


@dashboard.route('/dashboard')
@requires_authorization
def dash():
    user = discord.fetch_user()
    return render_template("dashboard.html", user=user, panellink=current_app.config['PTERO_APP_KEY'])

@dashboard.route("/logout")
def logout():
    discord.revoke()
    return redirect(url_for('index.home'))