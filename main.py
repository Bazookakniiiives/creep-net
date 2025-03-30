import sys, time
from core.utils import *
from core.banner import banner

from modules import (
    ip_geolocation, domain_whois, dns_lookup, reverse_ip,
    web_screenshot, username_search, metadata_extract,
    email_verify, google_dorks, pastebin_search
)

def main():
    funcs = {
        "1": ip_geolocation.run,
        "2": domain_whois.run,
        "3": dns_lookup.run,
        "4": reverse_ip.run,
        "5": web_screenshot.run,
        "6": username_search.run,
        "7": metadata_extract.run,
        "8": email_verify.run,
        "9": google_dorks.run,
        "10": pastebin_search.run
    }

    while True:
        title()
        clear()
        banner()
        choice = input("\n[$] Choice (1-10): ").strip()
        if choice in funcs:
            clear()
            funcs[choice]()
        else:
            printNotOk("Invalid choice.")
            pause()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        println("Exiting...")
        time.sleep(1)
        sys.exit(1)
    except Exception as e:
        printNotOk("Error: " + str(e))
        input()
