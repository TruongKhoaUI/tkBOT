import discord
import json
import os
from discord.ext import commands

class RankresetCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="rankreset", description="Reset points for all members.")
  async def rankreset(self, ctx):
    async with ctx.typing():
      if ctx.guild:
        if not ctx.author.guild_permissions.administrator:
          embed = discord.Embed(title="Leaderboard reset points", description="You don't have permission to use this command.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
        else:
          with open(os.getenv('leaderboard_directory'), 'r') as f:
            points = json.load(f)
          points[str(ctx.guild.id)] = {}
          with open(os.getenv('leaderboard_directory'), 'w') as f:
            json.dump(points, f)
          embed = discord.Embed(title="Leaderboard reset points", description="All points have reset to 0 for all members on this server.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
      else:
        embed = discord.Embed(title="Leaderboard reset points", description="You can't use this command when you're in DM.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author = False)

def setup(bot):
  bot.add_cog(RankresetCommand(bot))