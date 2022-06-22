#!/usr/bin/env python3
# Created By X - MrG3P5
import pyfiglet
import requests
import os
from datetime import datetime
from pytz import timezone
from colorama import Fore, init
from utils import topCrownLocal, topCrownGlobal, topRankGlobal, topRankLocal

# Config
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
white = Fore.WHITE

init(autoreset=True)

def logTime():
    now_utc = datetime.now(timezone('UTC'))
    now_pacific = now_utc.astimezone(timezone("Asia/Jakarta"))
    return now_pacific.strftime("%H:%M:%S")

def banner(str):
    os.system("cls||clear")
    __banner__ = pyfiglet.figlet_format(str, font="slant", justify="center")
    print(red + __banner__)
    print(f"\t\t\t{red}[ {white}Created By X - MrG3P5 {red}]")
    print(f"\t\t{red}[ {white}This tools for auto win in game stumble{red} ]\n")

def start():
    banner("X - Stumble")
    input_auth = input(f"{red}[{white}?{red}] {white}Enter your auth token : ")
    round_input = input(f"{red}[{white}?{red}] {white}Enter round (1, 2, 3) : ")

    while True:
        try:
            req_game = requests.get(f"http://kitkabackend.eastus.cloudapp.azure.com:5010/round/finishv2/{round_input}", headers={
                "authorization": input_auth
            }).json()
            if "BANNED" in str(req_game):
                print(f"{red}[{yellow}*{red}] {white}Account Got Banned")
                break
            elif "SERVER_ERROR" in str(req_game):
                continue
            elif "User" in str(req_game):
                print(f"{red}[{white}{logTime()}{red}] {white}Nickname: {green}{req_game['User']['Username']} {white}| Country: {green}{req_game['User']['Country']} {white}| Trophy: {green}{req_game['User']['SkillRating']} {white}| Crown: {green}{req_game['User']['Crowns']}")
                print(f"{red}[{white}{logTime()}{red}] {white}CrownLocal: {green}{topCrownLocal(req_game['User']['Username'])}{white} | CrownGlobal: {green}{topCrownGlobal(req_game['User']['Username'])}{white} | RankLocal: {green}{topRankLocal(req_game['User']['Username'])}{white} | RankGlobal: {green}{topRankGlobal(req_game['User']['Username'])}")
        except:
            continue

if __name__=="__main__":
    start()
