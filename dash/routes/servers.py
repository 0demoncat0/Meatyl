from flask import Blueprint, redirect, url_for, render_template, current_app
from flask.globals import request
from dash import discord
from dash.api import server
import json
from flask_discord import requires_authorization

server = Blueprint('server', __name__)

@server.route("/servers/create",methods=['GET', 'POST'])
@requires_authorization
def createserver():
    name = request.args.get("name")
    ram = request.args.get("ram")
    disk = request.args.get("disk")
    cpu = request.args.get("cpu")
    location = request.args.get("location")
    egg = request.args.get("egg")
    user = discord.fetch_user
    with open('settings.json', 'r') as f:
        set = json.load(f)

    for key,value in set['eggs'].items():
        if key == egg:
            id = value['info']['egg']
            im = value['info']['docker_image']
            start = value['info']['startup']
        else:
            print(f"No such egg.`{egg}`")
            return "Contact Administrator."

    for key,value in set['locations'].items():
        if value['name'] == location:
            location = key
        else:
            print(f"No such location `{location}`")
            return "Contact Administrator."
    server.create_server(name=name,user=user.id,ram=ram,disk=disk,cpu=cpu,eggid=id,location=location,image=im,startup=start)
@server.route("/server/delete")
@requires_authorization
def deleteserver():
    user = discord.fetch_user

@server.route("/server/modify")
@requires_authorization
def modifyserver():
    user = discord.fetch_user

@server.route("/server/start")
@requires_authorization
def startserver():
    user = discord.fetch_user

@server.route("/server/stop")
@requires_authorization
def stopserver():
    user = discord.fetch_user

@server.route("/servers/new")
@requires_authorization
def newserver():
    user = discord.fetch_user
    egnames = []
    locatnames = []
    with open('settings.json', 'r') as f:
        set = json.load(f)

    for key,value in set['eggs'].items():
        h = value['display']
        egnames.append(h)

    for key,value in set['locations'].items():
        f = value['name']
        locatnames.append(f)
    return render_template("create.html", user=user, egnames=egnames, locatnames=locatnames, panellink=current_app.config['PTERO_APP_KEY'])
