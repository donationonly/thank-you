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
    return now_pacific.strftime("%H:%M:%S")

def banner(str):
    os.system("cls||clear")
    __banner__ = pyfiglet.figlet_format(str, font="slant", justify="center")
    print(red + __banner__)
    print(f"{purple}Donation Scripts")
    print(f"{white}Update {red}10/07/2022")
    print(f"{white}Trophy & Crown Duplicator For Stumbe Guys\n")

    print(f"{white}Format : [Time] Username | Trophy | Crown ")
    print(f"{yellow}Setelah memasukan delay tidak muncul apa apa, berarti auth token sudah expired!")
    print(f"{white}")


def start():
    banner("")
    input_auth = input(f"Enter your auth token : ")
    print("""Round List
1. Round 1 ( 10 Trophy)
2. Round 2 ( 20 Trophy )
3. Round 3 ( Crown )""")
    round_input = input(f"Select you round : ")
    delay_input = input(f"Enter Delay ( in second ) : ")

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
                print(f"{white}[{white}{logTime()}{white}] {white}{req_game['User']['Username']} {white}| {req_game['User']['Country']} {white}| {req_game['User']['SkillRating']} {white}| {req_game['User']['Crowns']}")
        except:
            continue

if __name__=="__main__":
    start()
