import discord
import subprocess
from discord_slash import SlashCommand
from dotenv import load_dotenv

load_dotenv()
with open('discord.token', 'r') as file:
    file_content = file.read()
TOKEN = file_content

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(str(message))
    if message.content.startswith('/run'):
        
        # Extract the command from the message content
        command = message.content.split(' ')[1:]
        try:
            # Execute the command using subprocess
            output = subprocess.check_output(command, shell=True, universal_newlines=True)
            # Send the output back to the Discord channel
            await message.channel.send(output)
        except subprocess.CalledProcessError as e:
            await message.channel.send(f"Error: {e.output}")

client.run(TOKEN)