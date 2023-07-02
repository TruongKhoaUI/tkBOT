import discord
import json
from discord.ext import commands

class ResetpointsCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="resetpoints", description="Reset points for all members.")
  async def resetpoints(self, ctx):
    async with ctx.typing():
      if ctx.guild:
        if not ctx.author.guild_permissions.administrator:
          embed = discord.Embed(title="Leaderboard reset points", description="You don't have permission to use this command.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
        else:
          with open('/home/runner/level.json', 'r') as f:
            points = json.load(f)
          points[str(ctx.guild.id)] = {}
          with open('/home/runner/level.json', 'w') as f:
            json.dump(points, f)
          embed = discord.Embed(title="Leaderboard reset points", description="All points have reset to 0 for all members on this server.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
      else:
        embed = discord.Embed(title="Leaderboard reset points", description="You can't use this command when you're in DM.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author = False)

def setup(bot):
  bot.add_cog(ResetpointsCommand(bot))