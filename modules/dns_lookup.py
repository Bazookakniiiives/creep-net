import dns.resolver
from core.utils import *

def run():
    title()
    domain = input("[$] Enter domain: ")
    try:
        for t in ["A", "MX", "TXT"]:
            res = dns.resolver.resolve(domain, t, raise_on_no_answer=False)
            for r in res: printOk(f"{t}: {r.to_text()}")
    except Exception as e:
        printNotOk(str(e))
    pause()
