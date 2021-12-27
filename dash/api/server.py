import requests
from dash.api import configfile
purl = configfile.pteroURL
pkey = configfile.pteroAppKey

def create_server(name:str,user:int,ram:int,disk:int,cpu:int,eggid:int,location:int,image,startup):
    furl = purl + "/api/application/nodes/1/allocations"
    headers = {
        "Authorization": f"Bearer {pkey}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response1 = requests.request('GET', furl, headers=headers)
    data1 = response1.json()
    for keyval1 in data1["data"]:
        fa = keyval1["attributes"]
        if False == fa['assigned']:
            ipid = fa["id"]
        else:
            return "Not enough allocations left on node to assing server"
    url = purl + "/api/application/servers"
    headers = {
        "Authorization": f"Bearer {pkey}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    payload = """{
    "name": "%s",
    "user": %s,
    "egg": %s,
    "docker_image": "%s",
    "startup": "%s",
    "environment": {
        "BUNGEE_VERSION": " ",
        "SERVER_JARFILE": " "
    },
    "limits": {
        "memory": %s,
        "swap": 0,
        "disk": %s,
        "io": 500,
        "cpu": %s
    },
    "feature_limits": {
        "databases": 0,
        "backups": 0
    },
    "allocation": {
        "default": %s
    }
    }""" % (name,user,eggid,image,startup,ram,disk,cpu,ipid)
