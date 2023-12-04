import disnake
from disnake.ext import commands
from config import guild, reportchat
import random
import embed as embeds
# from mysql import connect_to_database
import requests

class project(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.user_command(name='profile', description='report to user', guild_ids=[guild])
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def profile(self, inter, user: disnake.User,):
        await inter.response.send_message(embed=embeds.success("cleared", f"This command nothing do"), ephemeral=True)
        
    @commands.slash_command()
    async def profile(inter, self):
        ...

    @profile.sub_command(name='profile_ds', description='check profile by profile ds', guild_ids=[guild])
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def chk_ds(self, inter, user: disnake.User):
        await inter.response.send_message(embed=embeds.success("cleared", f"This command nothing do"), ephemeral=True)

    @profile.sub_command(name='profile_name', description='check profile by profile username', guild_ids=[guild])
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def chk_name(self, inter, user):
        await inter.response.send_message(embed=embeds.success("cleared", f"This command nothing do"), ephemeral=True)

def setup(bot):
    bot.add_cog(project(bot))
