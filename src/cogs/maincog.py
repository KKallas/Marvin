from discord.ext import commands
from discord import app_commands
import discord

class MainCog(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        #tree = self.bot.tree

    #@commands.command(pass_context=True)
    @app_commands.command(
        name="acommand",
        description="Command description here",
        #guild=app_commands.Guild(id=1085329951978438727)
    )
    async def acommand(self, interaction, argument:str):
       await interaction.response.send_message("Stuff")        

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)
        guild = discord.Object(id="1085329951978438727")
        await self.bot.tree.sync(guild=guild)
        

async def setup(bot):
    await bot.add_cog(MainCog(bot), guilds=[discord.Object(id="1085329951978438727")])
    