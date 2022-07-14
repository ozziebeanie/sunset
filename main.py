import os
import discord
from discord.ext import commands
import tokenid
from pretty_help import PrettyHelp

bot = commands.Bot(
	command_prefix=["s!", "r!"],  # Change to desired prefix
	case_insensitive=True,
    status=discord.Status.do_not_disturb, # Sets the bots status to DND
    activity = discord.Streaming(name="r!help or s!help", url="https://www.twitch.tv/ozziebeanie"), # Sets the bots activity to Streaming and sets watch button to twitch channel
    help_command=PrettyHelp()
)

bot.author_id = 797147193907740702 # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

extensions = [
	'cogs.developer_commands', 'cogs.basic_commands', 'cogs.fun_commands', 'cogs.math_commands', 'cogs.voice_commands',  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.
 
bot.run(tokenid.token)  # Starts the bot