import whois
from core.utils import *

def run():
    title()
    domain = input("[$] Enter domain: ")
    try:
        w = whois.whois(domain)
        for k, v in w.items(): printOk(f"{k}: {v}")
    except Exception as e:
        printNotOk(str(e))
    pause()
