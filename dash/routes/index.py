from flask import Blueprint, render_template, redirect, url_for, current_app
from flask_discord import requires_authorization
import sqlite3

index = Blueprint('index', __name__)

@index.route("/")
def home():
    if current_app.discord.authorized:
        user = current_app.discord.fetch_user()
        headers = {
            "Authorization": f"Bearer {current_app.config['PTERO_APP_KEY']}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute(f"SELECT id FROM main WHERE username = {user.id}")
        result = cursor.fetchone()
        if result != None:
            return render_template("dashboard.html", user=user, panellink=current_app.config['PTERO_APP_KEY'])
        else:
            print("Creating one more user.")
            return redirect(url_for("users.createuser"))       
    else:
        return render_template("index.html")
