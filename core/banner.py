from colorama import Fore

def banner():
    print(Fore.LIGHTCYAN_EX + """
 ██████╗██████╗ ███████╗███████╗██████╗ ███╗   ██╗███████╗████████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║██╔════╝╚══██╔══╝
██║     ██████╔╝█████╗  █████╗  ██████╔╝██╔██╗ ██║█████╗     ██║   
██║     ██╔══██╗██╔══╝  ██╔══╝  ██╔═══╝ ██║╚██╗██║██╔══╝     ██║   
╚██████╗██║  ██║███████╗███████╗██║     ██║ ╚████║███████╗   ██║   
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝  ╚═══╝╚══════╝   ╚═╝   
    """)
    print(Fore.LIGHTMAGENTA_EX + "Github - https://github.com/MyArchiveProjects/creep-net\n")
    print(Fore.LIGHTMAGENTA_EX + "[1] IP Geolocation   [2] Domain WHOIS    [3] DNS Lookup")
    print(Fore.LIGHTMAGENTA_EX + "[4] Reverse IP       [5] Web Screenshot  [6] Username Search")
    print(Fore.LIGHTMAGENTA_EX + "[7] Metadata Extract [8] Email Verifier  [9] Google Dorks")
    print(Fore.LIGHTMAGENTA_EX + "[10] Pastebin Search")
