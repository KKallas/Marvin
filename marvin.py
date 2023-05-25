import discord
from discord import app_commands

import sys
from io import StringIO
import asyncio

import openai
import os

with open('discord.token', 'r') as file:
    file_content = file.read()
TOKEN = file_content

with open('openai.token', 'r') as file:
    file_content = file.read()
openai.api_key = file_content

# Create a dictionary to store user-defined variables in python enviorment
user_variables = {}

# Create a dictionary for keeping the Marvin Inetrfaces and Actions in neat order
marvin_scripts = {}

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)   

def python_validator(file_path:str):
    """tries to compile the python, if any errors occur returns false otherwise true

    Args:
        file_path (str): full path to the file

    Returns:
        bool: true if can be compiled by local pyhton, otherwise false
    """
    try:
        with open(file_path, "r") as file:
            # Try compiling the file
            compile(file.read(), file_path, "exec")
            return True

    except (SyntaxError, FileNotFoundError):
        return False


@tree.command(
        name = "save",
        description= "Save action or interface object for the Marvin bot",
        guild=discord.Object(id=1085329951978438727),
        )
async def save_python(interaction, attachment_message_link: str):
    """Save linked discord first attachment as local script for later execution

    Todo:
        -[ ] If the string is valid discord message string
        -[ ] Validation - signing

    Args:
        attachment_message_link (str): link to discord messgae that has the script file as 1st attachment
    """

    # split the link up into ids
    message_link = attachment_message_link.split('/')
    server_id = int(message_link[4])
    channel_id = int(message_link[5])
    mesg_id = int(message_link[6])

    # get server object
    server = client.get_guild(server_id)

    # get channel object
    channel = server.get_channel(channel_id)
    if channel==None:
        await interaction.response.send_message("could not get on the channel of the message")
        return

    # get message object
    message = await channel.fetch_message(mesg_id)
    if message==None:
        await interaction.response.send_message("could not get the message")
        return

    await message.attachments[0].save("tmp/"+message.attachments[0].filename)

    if python_validator()

    await interaction.response.send_message("file saved: "+message.attachments[0].filename)

@tree.command(
        name = "load",
        description= "Load action or interface object from the Marvin bot by name",
        guild=discord.Object(id=1085329951978438727),
        )
async def load_python(interaction, action_name: str):
    """Load Marvin custom scrip by name from bot server
    You can get the list of file by /list

    Args:
        action_name (str): file name with extension

    """
    file_path = "tmp/"+action_name
    try:
        with open(file_path, "rb") as file:
            discord_file = discord.File(file)
            await interaction.response.send_message(file=discord_file)
    except Exception as e:
        await interaction.response.send_message("could not find the file...")

@tree.command(
        name = "list",
        description= "List all custom python files",
        guild=discord.Object(id=1085329951978438727),
        )
async def load_python(interaction):
    """List full contents of the tmp folder"""
    folder_path = "tmp/"
    file_list = os.listdir(folder_path)
    await interaction.response.send_message("all available python actions for me: ```"+str(file_list)+"```")

@tree.command(
        name = "python", 
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
        globals().update(user_variables)
        exec(input_string,globals(),locals())
        user_variables.update(locals())
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

@client.event
async def on_message(message):
    if message.author.bot == True:
        return
    
    async with message.channel.typing():
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role':'assistant', 'content':'you are chatgpt ai assisnt who can answer all sorts of questions and write python code'},
                {'role':'user','content':message.content}],
            temperature=0.5,
        )
        while not response.choices[0].message.content.strip():
            await asyncio.sleep(2)
            response = openai.Completion.fetch(response.id)

        await message.channel.send(response.choices[0].message.content)

client.run(TOKEN)