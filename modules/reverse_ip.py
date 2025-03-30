import requests
from core.utils import *

def run():
    title()
    ip = input("[$] Enter IP: ")
    try:
        r = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}")
        printOk(r.text)
    except Exception as e:
        printNotOk(str(e))
    pause()
