from discord.ext import commands
import discord

import asyncio
import os
"""
discord.token

one line, raw text of the token
"""
print(os.getcwd())
with open('discord.token', 'r') as file:
    file_content = file.read()
TOKEN = file_content


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents, application_id="1085322151583825951")

asyncio.run(bot.load_extension("cogs.maincog"))

bot.run(TOKEN)