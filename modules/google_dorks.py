from core.utils import *

def run():
    title()
    target = input("[$] Enter target (site): ")
    dorks = [
        f"site:{target} inurl:admin",
        f"site:{target} intitle:index.of",
        f"site:{target} ext:sql | ext:xml",
        f"site:{target} intext:password"
    ]
    for d in dorks: printOk(d)
    pause()
