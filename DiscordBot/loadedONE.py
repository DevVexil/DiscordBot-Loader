# This is the script for your bot 1
# Credits to DevVexil
# rackcrate.com for amazing servers

import discord # For discord
from discord.ext import commands # For discord
import logging # For logging
from pathlib import Path # For paths
import json


cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

secret_file = json.load(open(cwd+'./tokens.json'))
bot = commands.Bot(command_prefix='-', case_insensitive=True)
bot.config_token = secret_file['token']

@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: -\n-----")
    print("-----\nLogged in as: {} : {}\n-----\nMy current prefix is: -\n-----".format(bot.user.name, bot.user.id))
    await bot.change_presence(activity=discord.Game(name=f"Hi, my names {bot.user.name}.\nUse - to interact with me!"))


bot.run(bot.config_token)
