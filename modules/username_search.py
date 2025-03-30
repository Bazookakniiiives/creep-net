import requests
from core.utils import *

def run():
    title()
    name = input("[$] Enter username: ")
    for site in ["github.com", "twitter.com", "instagram.com"]:
        url = f"https://{site}/{name}"
        try:
            r = requests.get(url)
            if r.status_code == 200: printOk(f"Found: {url}")
            else: printWarn(f"Not found: {url}")
        except: printNotOk(f"Error: {url}")
    pause()
