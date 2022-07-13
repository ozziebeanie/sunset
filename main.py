import os
import discord
from discord.ext import commands
import tokenid
import activitya
from pretty_help import PrettyHelp

bot = commands.Bot(
	command_prefix=["s!", "r!"],  # Change to desired prefix
	case_insensitive=True,
    status=discord.Status.idle,
    activity=activitya.activity,
    help_command=PrettyHelp()
)

bot.author_id = 797147193907740702 # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier
    #await bot.change_presence(status=discord.Status.do_not_disturb)

extensions = [
	'cogs.developer_commands', 'cogs.basic_commands', 'cogs.fun_commands', 'cogs.math_commands', 'cogs.voice_commands',  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

ending_note = "The ending note from {ctx.bot.user.name}\nFor command {help.clean_prefix}{help.invoked_with}"
 
bot.run(tokenid.token)  # Starts the bot