import dns.resolver, re
from core.utils import *

def run():
    title()
    email = input("[$] Enter email: ")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        printNotOk("Invalid format"); pause(); return
    domain = email.split("@")[1]
    try:
        mx = dns.resolver.resolve(domain, "MX")
        for r in mx: printOk(f"MX: {r.exchange}")
    except Exception as e:
        printNotOk(str(e))
    pause()
