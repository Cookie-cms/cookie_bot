import disnake
from disnake.ext import commands
from disnake import Option
# from config import guild, reportchat
import random
import embed as embeds
# from mysql import connect_to_database
# import requests
class project(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.user_command(name='profile', description='report to user',)
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def profile(self, inter, user: disnake.User,):
        await inter.response.send_message(embed=embeds.success("cleared", f"This command nothing do"), ephemeral=True)
        
    @commands.slash_command()
    async def profile(inter, self):
        ...

    @profile.sub_command(name='profile_ds', description='check profile by profile ds', )
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def chk_ds(self, inter, user: disnake.User):
        await inter.response.send_message(embed=embeds.success("cleared", f"This command nothing do"), ephemeral=True)

    @profile.sub_command(name='profile_name', description='check profile by profile username', )
    @commands.cooldown(rate= 1, per= 10, type= commands.BucketType.member)
    async def chk_name(self, inter, user):
        await inter.response.send_message(embed=embeds.success("cleared", f"This command nothing do"), ephemeral=True)

    valid_choices = commands.option_enum(["1 LVL", "2 LVL", "3 LVL"])

    @commands.slash_command(name='promote', description='Promote a user')
    async def promote(
        self,
        inter,
        user: disnake.User = commands.Param(description="The user to promote"),
        level: int = commands.Param(
            description="Promotion level",
            choices={"1 LVL": 1, "2 LVL": 2, "3 LVL": 3}
        ),
        expire: int = commands.Param(description="Expiration time in minutes")
    ):
        """Promote a user to a specific level with expiration time."""
        embed = disnake.Embed(
            title="Promotion",
            description=f"User {user} promoted to level {level} with expiration {expire} minutes",
            color=disnake.Color.green()
        )
        await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(project(bot))
