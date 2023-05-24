import discord
from discord import app_commands

import sys
from io import StringIO
import asyncio

import openai

with open('discord.token', 'r') as file:
    file_content = file.read()
TOKEN = file_content

with open('openai.token', 'r') as file:
    file_content = file.read()
openai.api_key = file_content

# Create a dictionary to store user-defined variables
user_variables = {}

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)   

@tree.command(
        name = "save",
        description= "Save action or interface object for the Marvin bot",
        guild=discord.Object(id=1085329951978438727),
        )
async def save_python(interaction, input_string: str):
    """Save linked discord first attachment as local script for later execution
    Todo:
        If the string is valid discord message string
        Validation - signing

    Args:
        input_string (str): link to discord messgae that has the script file as 1st attachment
    """
    message_link = input_string.split('/')
    server_id = int(message_link[4])
    channel_id = int(message_link[5])
    mesg_id = int(message_link[6])

    server = client.get_guild(server_id)
    channel = server.get_channel(channel_id)

    print(channel_id)

    if channel:
        message = await channel.fetch_message(mesg_id)
        await message.attachments[0].save("tmp/"+message.attachments[0].filename)
        await interaction.response.send_message("file saved: "+message.attachments[0].filename)
    else:
        await interaction.response.send_message("could not save the file")

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