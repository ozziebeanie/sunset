from http import client
import discord
from discord.ext import commands

class BasicCommands(commands.Cog, name='Basic Commands'):
    '''These are basic commands anyone can use'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, message=None):
        '''
        Makes the bot say something.
        '''
        await ctx.message.delete()
        await ctx.send(message)
    
    
def setup(bot):
    bot.add_cog(BasicCommands(bot))