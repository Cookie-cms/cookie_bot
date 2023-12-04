import disnake
import os
from config import TOKEN
from disnake.ext import commands
import embed as embeds

# from mysql import cursor

bot = commands.InteractionBot(intents=disnake.Intents.all())
# logging.basicConfig(level=logging.INFO)
@bot.event
async def on_ready():
    print("The bot is ready!")
    await bot.change_presence(activity=disnake.Activity(), status=disnake.Status.idle)
    print(f"Logged in as {bot.user} in {len(bot.guilds)} guilds")
    # print(f"Status: {bot.status}")

@bot.event
async def on_slash_command_error(inter, error):
    if isinstance(error, commands.CommandOnCooldown):
        await inter.response.send_message(embed=embeds.createCooldownEmbed(round(error.retry_after)), ephemeral=True, delete_after=error.retry_after)


ignored_files = ['']


import os

def load_extensions_from_directory(directory):
    ignored_files = []  # Убедитесь, что у вас есть этот список или определите его заранее
    for filename in os.listdir(directory):
        if filename.endswith('.py') and filename != '__init__.py' and filename not in ignored_files:
            extension_path = os.path.relpath(os.path.join(directory, filename)).replace(os.sep, '.')[:-3]
            try:
                bot.load_extension(extension_path)
                print(f'Extension loaded: {extension_path}')
            except Exception as e:
                print(f'Skipped loading extension {extension_path}: {str(e)}')

# Specify the directory where extensions are located
extension_directory = 'modules'
load_extensions_from_directory(extension_directory)

# bot.load_extension('modules.utils.profile')
bot.run(TOKEN)