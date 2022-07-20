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
    
    @commands.command()
    async def verify(self, ctx):
        '''
        Gives the verify role within the "Sunset Servers" server.
        '''
        member = ctx.message.author
        for guild_role in member.guild.roles:
          if guild_role.name == "verified":
            role = guild_role
        await member.add_roles(role)

    @commands.command(description="Bots latency.")
    async def ping(self, ctx):
        '''
        Sends how fast the bot is running.
        '''
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! My latency is {latency}ms.")

    @commands.command()
    async def servers(self, ctx):
        '''
        Shows how many servers the bot has joined.
        '''
        servers = list(self.bot.guilds)
        await ctx.send(f"I have joined over {str(len(servers))} servers.")

def setup(bot):
    bot.add_cog(BasicCommands(bot))