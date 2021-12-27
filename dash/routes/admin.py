from flask import Blueprint, redirect, url_for, render_template, current_app
from dash import discord
from flask_discord import requires_authorization

admin = Blueprint('admin', __name__)

@admin.route("admin")
@requires_authorization
def admin():
    user = discord.fetch_user

@admin.route("admin/server/delete")
@requires_authorization
def admin_delete_server():
    user = discord.fetch_user

@admin.route("admin/add/resources")
@requires_authorization
def admin_add():
    user = discord.fetch_user
