import discord
from discord.ext import commands

class MathCommands(commands.Cog, name='Math Commands'):
    '''These are basic math commands anyone can use'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a + b)

    @commands.command()
    async def sub(self, ctx, a: int, b: int):
        await ctx.send(a - b)

    @commands.command()
    async def mult(self, ctx, a: int, b: int):
        await ctx.send(a * b)
    
def setup(bot):
    bot.add_cog(MathCommands(bot))