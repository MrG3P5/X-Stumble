#!/usr/bin/env python3
# Created By X - MrG3P5

import pyfiglet
import requests
import os
from threading import Thread
from colorama import Fore, init
from random import randint

# Config
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
white = Fore.WHITE
ATTEMP_R1 = 0
ATTEMP_R2 = 0
ATTEMP_R3 = 0
init(autoreset=True)

def banner(str):
    os.system("cls||clear")
    __banner__ = pyfiglet.figlet_format(str, font="slant", justify="center")
    print(red + __banner__)
    print(f"\t\t\t{red}[ {white}Created By X - MrG3P5 {red}]")
    print(f"\t\t{red}[ {white}This tools for auto win in game stumble{red} ]\n")

def start(token):
    global ATTEMP_R1, ATTEMP_R2, ATTEMP_R3
    banner("X - Stumble")

    while True:
        try:
            random_round = randint(1, 3)
            req_game = requests.get(f"http://kitkabackend.eastus.cloudapp.azure.com:5010/round/finishv2/{random_round}", headers={
                "authorization": token
            }).json()
            if "BANNED" in str(req_game):
                print(f"{red}[{yellow}*{red}] {white}Account Got Banned")
            elif "SERVER_ERROR" in str(req_game):
                continue
            elif "User" in str(req_game):
                print(f"{red}[{white}*{red}] {white}Nickname: {green}{req_game['User']['Username']} {white}| Country: {green}{req_game['User']['Country']} {white}| Trophy: {green}{req_game['User']['SkillRating']} {white}| Crown: {green}{req_game['User']['Crowns']}")
        except:
            if random_round == 1:
                if ATTEMP_R1 == 5 and ATTEMP_R2 == 5 and ATTEMP_R3 == 5:
                    print(f"{red}[{yellow}*{red}] {white}Wrong cookie or Expired cookie!")
                    break
                else:
                    ATTEMP_R1 += 1
                    continue
            elif random_round == 2:
                if ATTEMP_R2 == 5 and ATTEMP_R2 == 5 and ATTEMP_R3 == 5:
                    print(f"{red}[{yellow}*{red}] {white}Wrong cookie or Expired cookie!")
                    break
                else:
                    ATTEMP_R2 += 1
                    continue
            elif random_round == 3:
                if ATTEMP_R3 == 5 and ATTEMP_R2 == 5 and ATTEMP_R3 == 5:
                    print(f"{red}[{yellow}*{red}] {white}Wrong cookie or Expired cookie!")
                    break
                else:
                    ATTEMP_R3 += 1
                    continue

if __name__=="__main__":
    banner("X - Stumble")
    input_auth = input(f"{red}[{white}?{red}] {white}Enter your auth token : ")
    t = Thread(target=start, args=(input_auth,))
    t.start()
