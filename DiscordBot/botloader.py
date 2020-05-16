# Github Discord Bot Loader
# Open Source Code Dont Remove Credits
# Made by DevVexil3#0909 // vexil.xyz
#######################################

#Imports#

import os
import loadedONE as ox
#from loadedONE import
import colorama
from colorama import Fore
colorama.init()
########################################

ui = f"""
{Fore.LIGHTMAGENTA_EX}      
    __  ___      ____  _ __                    __         
   /  |/  /_  __/ / /_(_) /   ____  ____ _____/ /__  _____
  / /|_/ / / / / / __/ / /   / __ \/ __ `/ __  / _ \/ ___/
 / /  / / /_/ / / /_/ / /___/ /_/ / /_/ / /_/ /  __/ /    
/_/  /_/\__,_/_/\__/_/_____/\____/\__,_/\__,_/\___/_/                                         
{Fore.RESET}
"""
select = f"""
{Fore.CYAN}
Load the bot token [1-6]
{Fore.RESET}
"""




def Menu(ui, select):
    print(ui)
    print(select)
    tok = input("> ")
    if tok == "1":
        print("Loaded one")
        ox()
    elif tok == "2":
        print("Loaded two")
    else:
        print("Not a valid option")





Menu(ui, select)

