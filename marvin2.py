import discord
from discord import app_commands

import sys
from io import StringIO

import openai

with open('discord.token', 'r') as file:
    file_content = file.read()
TOKEN = file_content

with open('openai.token', 'r') as file:
    file_content = file.read()
openai.api_key = file_content

# Create a dictionary to store user-defined variables
user_variables = {}

import odoo
oi = odoo.odooInterface(user_variables)


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)



@tree.command(
        name = "odoo_query",
        description = "execute python query in odoo server to get operational data from odoo",
        guild=discord.Object(id=1085329951978438727),
        )
async def exec_odoo(interaction, input_string: str):
    print("debug 1: input string: "+input_string)
    answer = oi.query_string(input_string)
    await interaction.response.send_message('```json\n'+str(answer)+'```')


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
    
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'assistant', 'content':'you are chatgpt ai assisnt who can answer all sorts of questions and write python code'},
            {'role':'user','content':message.content}],
        temperature=0.5,
    )
    
    await message.channel.send(response.choices[0].message.content)

client.run(TOKEN)