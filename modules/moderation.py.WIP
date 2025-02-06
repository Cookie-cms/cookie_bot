import disnake
from disnake.ext import commands
from config import guild, reportchat
import random
import embed as embeds
# from mysql import connect_to_database
import requests

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def mod(inter, self):
        ...

    @mod.sub_command(name='report', description='report to user', guild_ids=[guild])
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def report(self, inter, user: disnake.User, reason: str):
        await inter.response.send_message(embed=embeds.success("Reported", f"{user.mention} has been reported with {reason}"), ephemeral=True)
        
        # Get the channel object and then send the message
        channel = self.bot.get_channel(int(reportchat))
        if channel:
            await channel.send(embed=embeds.danger("Report",f"{inter.user.mention} reported {user.mention} with ``{reason}``"))
        else:
            # Channel not found
            await inter.followup.send("Error: Channel not found.", ephemeral=True)

    @mod.sub_command(name='mute', description='mute user', guild_ids=[guild])
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def mute(self, inter, user: disnake.User, reason: str, expire: str):
        await inter.response.send_message(embed=embeds.success("cleared", f"This command nothing do"), ephemeral=True)

    @mod.sub_command(name='unmute', description='mute user', guild_ids=[guild])
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def unmute(self, inter, user: disnake.User, reason: str):
        await inter.response.send_message(embed=embeds.success("cleared", f"This command nothing do"), ephemeral=True)

    @mod.sub_command(name='ban', description='mute user', guild_ids=[guild])
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def ban(self, inter, user: disnake.User, reason: str, expire: str):
        await inter.response.send_message(embed=embeds.success("cleared", f"This command nothing do"), ephemeral=True)

    @mod.sub_command(name='unban', description='mute user', guild_ids=[guild])
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def unban(self, inter, user: disnake.User, reason: str):
        await inter.response.send_message(embed=embeds.success("cleared", f"This command nothing do"), ephemeral=True)

    @mod.sub_command(name='clear', description='clear chat', guild_ids=[guild])
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def unban(self, inter, msgs):
        await inter.response.send_message(embed=embeds.success("cleared", f"This command nothing do"), ephemeral=True)

def setup(bot):
    bot.add_cog(moderation(bot))
