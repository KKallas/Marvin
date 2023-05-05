import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'MTA4NTMyMjE1MTU4MzgyNTk1MQ.GUXsn2.cX_MXeuiU6JnpmuxoF-XW1eQ6OU1MCe5OcVfSM'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)