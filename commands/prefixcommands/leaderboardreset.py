import discord
import json
import os
from typing import Union
from discord.ext import commands

class LeaderboardresetCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="leaderboardreset", description="Reset points for all members.")
  async def leaderboardreset(self, ctx, member: Union[discord.Member, discord.User, int] = None):
    async with ctx.typing():
      if ctx.guild:
        if not ctx.author.guild_permissions.administrator:
          embed = discord.Embed(title="Leaderboard reset points", description="You don't have permission to use this command.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
        try:
          if isinstance(member, int):
            member = await self.bot.fetch_user(member)
        # It will show this message when the user ID is invaild
        except discord.errors.NotFound:
          embed = discord.Embed(title="User Information", description="Invalid user ID or username.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author=False)
          return          
        if member is None:
          with open(os.getenv('leaderboard_directory'), 'r') as f:
            points = json.load(f)
          points[str(ctx.guild.id)] = {}
          with open(os.getenv('leaderboard_directory'), 'w') as f:
            json.dump(points, f)
          embed = discord.Embed(title="Leaderboard reset points", description="All points have reset to 0 for all members on this server.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)         
        else:
          with open(os.getenv('leaderboard_directory'), 'r') as f:
            points = json.load(f)
          points[str(ctx.guild.id)].pop(str(member.id), None)
          with open(os.getenv('leaderboard_directory'), 'w') as f:
            json.dump(points, f)
          embed = discord.Embed(title="Leaderboard reset points", description=f"{member}'s points have been reset to 0.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author=False)          
      else:
        embed = discord.Embed(title="Leaderboard reset points", description="You can't use this command when you're in DM.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author = False)

def setup(bot):
  bot.add_cog(LeaderboardresetCommand(bot))