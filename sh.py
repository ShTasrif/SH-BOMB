import requests

from requests.structures import CaseInsensitiveDict

import os

import sys

import time


os.system("clear")

red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"

logo=(green+"""
   _____ _    _            ____   ____  __  __ ____  
  / ____| |  | |          |  _ \ / __ \|  \/  |  _ \ 
 | (___ | |__| |  ______  | |_) | |  | | \  / | |_) |
  \___ \|  __  | |TASRIF| |  _ <| |  | | |\/| |  _ < 
  ____) | |  | |          | |_) | |__| | |  | | |_) |
 |_____/|_|  |_|          |____/ \____/|_|  |_|____/ """)
 

line=(yellow+"======================================================")
tversion=(cyan+"\t\t     Version : 1.0.4 ")

line2=("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~")
 
dtls=(yellow+"\t\t𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐁𝐲: 𝐌𝐃 𝐓𝐀𝐒𝐑𝐈𝐅 𝐇𝐎𝐒𝐒𝐄𝐍 \n \t\tYoutube.com/tasrifmultimedia \n \t\tFb.com/tasrif.hossen.shuvo\n \t\tGithub.com/ShTasrif")

note=(red+"Note: I wont be responsible fo any illigal activites.")

print(logo)

print(" ")

print(dtls)

print(tversion)

print(line)

print(note)

print(line)

print(" \t\tOur Tool has been changed")

os.system("cd $HOME && rm -rf SH-BOMB && git clone https://github.com/ShTasrif/cybersh && cd cybersh && python main.py")

