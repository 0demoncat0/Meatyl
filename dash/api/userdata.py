from flask import current_app

import json
import requests
from urllib.parse import quote
import sqlite3

def checkIfUserExists(discordEmail):
    url = f"{current_app.config['PTERO_URL']}/api/application/users?filter{str(quote(f'={discordEmail}'))}"
    headers = {
        "Authorization": f"Bearer {current_app.config['PTERO_APP_KEY']}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers).json()['data']
    

def create_user(discordUsername, discordEmail, discordUserID, discorddic):

    # Main function #

    url =  f"{current_app.config['PTERO_URL']}/api/application/users"
    headers = {
        "Authorization": f"Bearer {current_app.config['PTERO_APP_KEY']}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    payload = '{"email": "'+str(discordEmail)+'","username": "'+str(discordUserID)+'","first_name": "'+str(discordUsername)+'","last_name": "'+str(discorddic)+'"}'

    requests.request('POST', url, data=payload, headers=headers)
    headers2 = {
    "Authorization": f"Bearer {current_app.config['PTERO_APP_KEY']}",
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
    data2=requests.get(f"{current_app.config['PTERO_URL']}/api/application/users?filter[email]{str(f'={discordEmail}')}", headers=headers2)
    response = data2.json()
    if data2.status_code == 200:
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute(f"SELECT id FROM main WHERE username = {discordUserID}")
        result = cursor.fetchone()
        if result == None:
            sql = ("INSERT INTO main(id, username) VALUES (?, ?)")
            for i in response["data"]:
                id = i["attributes"]["id"]
                val = (id, discordUserID)
                cursor.execute(sql,val)
        else:
            pass
        db.commit()
        cursor.close()
        db.close()
    else:
        print("meow")
