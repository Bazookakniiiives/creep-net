import requests
from core.utils import *

def run():
    title()
    url = input("[$] Enter URL: ")
    try:
        key = "demo"
        r = requests.get(f"https://shot.screenshotapi.net/screenshot?token={key}&url={url}&output=image&file_type=png")
        printOk(f"Screenshot URL: {r.url}")
    except Exception as e:
        printNotOk(str(e))
    pause()
