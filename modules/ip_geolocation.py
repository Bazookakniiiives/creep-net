import requests
from core.utils import *

def run():
    title()
    ip = input("[$] Enter IP: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        printOk(f"IP: {r['query']}")
        printOk(f"Country: {r['country']}")
        printOk(f"City: {r['city']}")
        printOk(f"ISP: {r['isp']}")
        printOk(f"Coords: {r['lat']}, {r['lon']}")
    except Exception as e:
        printNotOk(str(e))
    pause()
