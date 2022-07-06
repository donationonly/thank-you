import pyfiglet
import requests
import os
from time import sleep
from datetime import datetime
from pytz import timezone
from colorama import Fore, init

red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
white = Fore.WHITE
magenta = Fore.LIGHTMAGENTA_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
purple = Fore.MAGENTA
black = Fore.BLACK

init(autoreset=True)

def logTime():
    now_utc = datetime.now(timezone('UTC'))
    now_pacific = now_utc.astimezone(timezone("Asia/Jakarta"))
    return now_pacific.strftime("%H:%M")

def banner(str):
    os.system("cls||clear")
    __banner__ = pyfiglet.figlet_format(str, font="slant", justify="center")
    print(red + __banner__)
    print(f"{white}Tools by {purple}!@#$")
    print(f"{white}Update {red}06/07/2022")
    print(f"{white}Trophy & Crown Duplicator For Stumbe Guys\n")


def start():
    banner("")
    input_auth = input(f"Enter your auth token : ")
    print("""Round List
1. Round 1 ( 10 Trophy)
2. Round 2 ( 20 Trophy )
3. Round 3 ( Crown )""")
    round_input = input(f"Enter round (1, 2, 3) : ")
    delay_input = input(f"Enter Delay (ex: 1 = 1second) : ")

    while True:
        try:
            sleep(int(delay_input))
            req_game = requests.get(f"http://kitkabackend.eastus.cloudapp.azure.com:5010/round/finishv2/{round_input}", headers={
                "authorization": input_auth
            }).json()
            if "BANNED" in str(req_game):
                print(f"{red}Account Got Banned!")
                break
            elif "SERVER_ERROR" in str(req_game):
                continue
            elif "User" in str(req_game):
                print(f"{red}[{white}{logTime()}{red}] {white}Nickname: {magenta}{req_game['User']['Username']} {white}| Country: {blue}{req_game['User']['Country']} {white}| Trophy: {green}{req_game['User']['SkillRating']} {white}| Crown: {yellow}{req_game['User']['Crowns']}")
        except:
            continue

if __name__=="__main__":
    start()
