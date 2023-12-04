import disnake
from disnake.ext import commands
from config import welcomechat
class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(welcomechat)) # Replace with the actual ID of the channel where you want to send the welcome message
        
        message = f"Welcome here {member.mention}"

        await channel.send(message)


def setup(bot):
    bot.add_cog(Welcome(bot))