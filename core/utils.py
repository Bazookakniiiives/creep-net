import os, sys
from colorama import Fore, init
init(autoreset=True)

def clear(): os.system('cls' if os.name == 'nt' else 'clear')
def title():
    if os.name == 'nt': os.system('title CreepNET')
    else:
        sys.stdout.write("\x1b]2;CreepNET\x07")
        sys.stdout.flush()
def pause(): input(Fore.LIGHTBLUE_EX + "\n[$] Press ENTER to continue... "); clear()
def printOk(msg): print(Fore.LIGHTGREEN_EX + "[+] " + msg)
def printNotOk(msg): print(Fore.LIGHTRED_EX + "[!] " + msg)
def printWarn(msg): print(Fore.LIGHTYELLOW_EX + "[-] " + msg)
def println(msg): print(Fore.LIGHTBLUE_EX + "[$] " + msg)
