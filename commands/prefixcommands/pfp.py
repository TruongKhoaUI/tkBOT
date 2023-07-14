import discord
from discord.ext import commands

class PfpCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="pfp", description="Show member's avatar.") # Show the profile picture
  async def pfp(self, ctx, member:discord.User = None):
    async with ctx.typing():
      try:
        # If the `member` value is empty, it will show their avatar that they have sent
        if member == None:
          member = ctx.author
        # Check the guild user
        if isinstance(member, discord.Member):
          # If the profile picture is empty, it will show the Discord logo
          if member.display_avatar is not None:
            # Show the username and their profile picture
            embed = discord.Embed(title=f"{member}", color=0x3f48cc)
            embed.set_image(url=member.display_avatar.url)
          else:
            # Show the username and their profile picture
            embed = discord.Embed(title=f"{member}", color=0x3f48cc)
            embed.set_image(url=None)
        else:
          # If the profile picture is empty, it will show the Discord logo
          if member.display_avatar is not None:
            embed = discord.Embed(title=f"{member}", color=0x3f48cc)
            embed.set_image(url=member.display_avatar.url)
          else:
            embed = discord.Embed(title=f"{member}", color=0x3f48cc)
            embed.set_image(url=None)
        await ctx.reply(embed=embed, mention_author = False)
      except Exception:
        embed = discord.Embed(title="Profile Picture", description="Invalid user ID or username.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author = False)              

def setup(bot):
  bot.add_cog(PfpCommand(bot))