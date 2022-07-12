from http import client
import discord
from discord.ext import commands

class BasicCommands(commands.Cog, name='Basic Commands'):
    '''These are basic commands anyone can use'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, message=None):
        await ctx.message.delete()
        await ctx.send(message)
    
    @commands.Cog.listener() 
    async def on_member_join(member):
        channel = discord.get_channel(970381040403218472) # replace id with the welcome channel's id
        await channel.send(f"{member} has arrived!")
    
def setup(bot):
    bot.add_cog(BasicCommands(bot))