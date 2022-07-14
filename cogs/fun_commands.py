import discord
from discord.ext import commands

class FunCommands(commands.Cog):
    """
    Contains fun commands, activities and more!
    """
    def __init__(self, bot,):
        self.bot = bot

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        '''
        Hugs the chosen person.
        '''
        embed = discord.Embed(title=f"```{ctx.author.name}``` hugged ```{member.name}```")
        embed.set_image(url="https://cdn.weeb.sh/images/rJv2H5adf.gif")
        await ctx.send(embed=embed)

    @commands.command()
    async def middle(self, ctx, member: discord.Member):
        '''
        Sticks up the middle finger to the chosen person.
        '''
        embed = discord.Embed(title=f"{ctx.author.name} Stuck Up Middle Finger At {member.name}")
        embed.set_image(url="https://c.tenor.com/szJmB0ISf7UAAAAM/anime-girl.gif")
        await ctx.send(embed=embed)


    @commands.command()
    async def wave(self, ctx, member: discord.Member):
        '''
        Waves at the chosen person.
        '''
      embed = discord.Embed(title=f"{ctx.author.name} waved at {member.name}")
      embed.set_image(url="https://c.tenor.com/uGN3n2O03GIAAAAC/anime-wave.gif")
      await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, member: discord.Member):
        '''
        Kills the chosen person.
        '''
        embed = discord.Embed(title=f"{ctx.author.name} has killed {member.name}", color=0xc70e0e)
        embed.set_image(url="https://cdn.weeb.sh/images/HyXTiyKw-.gif")
        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        '''
        Kisses the chosen person.
        '''
        embed = discord.Embed(title=f"{ctx.author.name} kissed {member.name}", color=0xc70e0e)
        embed.set_image        (url="https://cdn.weeb.sh/images/BJSdQRtFZ.gif")
        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        '''
        Slaps the chosen person.
        '''
        embed = discord.Embed(title=f"{ctx.author.name} slapped {member.name}", color=0xc70e0e)
        embed.set_image        (url="https://cdn.weeb.sh/images/SJdXoVguf.gif")
        await ctx.send(embed=embed)

    @commands.command()
    async def carry(self, ctx, member: discord.Member):
        '''
        Carries the chosen person.
        '''
        embed = discord.Embed(title=f"{ctx.author.name} is carrying {member.name}. Looks Like They Want Down", color=0xc70e0e)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FunCommands(bot))