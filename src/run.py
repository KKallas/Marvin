from discord.ext import commands
import discord

import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents, application_id="1085322151583825951")

asyncio.run(bot.load_extension("cogs.maincog"))

bot.run("MTA4NTMyMjE1MTU4MzgyNTk1MQ.G-T-RH.3omyFywwErilL_Ca9JKQD3BUXpG_olk64lCot0")