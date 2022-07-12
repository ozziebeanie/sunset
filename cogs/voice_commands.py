import discord
from discord.ext import commands

class VoiceCommands(commands.Cog, name='Voice Commands'):
    '''These are basic commands anyone can use'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        channel = ctx.author.voice.channel
        await ctx.voice_client.disconnect()
    
def setup(bot):
    bot.add_cog(VoiceCommands(bot))