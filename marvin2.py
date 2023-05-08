import discord
from discord import app_commands

import sys
from io import StringIO

with open('discord.token', 'r') as file:
    file_content = file.read()
TOKEN = file_content

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(
        name = "run", 
        description = "Execute python command in bot and amswer with standard IO", 
        guild=discord.Object(id=1085329951978438727),
        ) 
async def exec_python(interaction, input_string: str):
    """
    Execute python command in bot and amswer with standard IO

    Args:
        input_string (str): Python command in qoutes as singe string to execute
    """
    redirected_output = None
    local_error = None

    try:
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        exec(input_string,globals(),locals())
        sys.stdout = old_stdout
    except Exception as e:
        local_error = e

    answer = local_error
    if redirected_output is not None:
        if local_error is None:
            answer = redirected_output.getvalue()
    
    if answer is None or answer == "":
        answer = "No output"
    await interaction.response.send_message(answer)


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1085329951978438727))
    print("Ready!")

client.run(TOKEN)