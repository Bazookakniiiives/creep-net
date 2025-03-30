import requests
from core.utils import *

def run():
    title()
    key = input("[$] Enter pastebin raw ID or keyword: ")
    try:
        r = requests.get(f"https://pastebin.com/raw/{key}")
        if r.status_code == 200:
            printOk("Leak found:"); print(r.text)
        else:
            printWarn("Not found.")
    except Exception as e:
        printNotOk(str(e))
    pause()
