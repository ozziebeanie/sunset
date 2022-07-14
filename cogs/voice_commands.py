import discord
from discord.ext import commands

class VoiceCommands(commands.Cog, name='Voice Commands'):
    '''These are basic commands anyone can use'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        '''
        Makes the bot join a vc.
        '''
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        '''
        Makes the bot leave the vc it's in.
        '''
        channel = ctx.author.voice.channel
        await ctx.voice_client.disconnect()
    
def setup(bot):
    bot.add_cog(VoiceCommands(bot))