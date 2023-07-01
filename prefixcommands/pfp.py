import discord
from discord.ext import commands
from typing import Union

class PfpCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command() # Show the profile picture
  async def pfp(self, ctx, member:Union[discord.Member, discord.User, int] = None):
    async with ctx.typing():
      if isinstance(member, int):
        # Get profile picture from a user when they are not in the guild
        try:
          member = await self.bot.fetch_user(member)
        # It will show this message when the user ID is invaild
        except discord.errors.NotFound:          
          embed = discord.Embed(title="Profile Picture", description="Invalid user ID or username.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
      # If the `member` value is empty, it will show their avatar that they have sent
      elif member == None:
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

def setup(bot):
  bot.add_cog(PfpCommand(bot))