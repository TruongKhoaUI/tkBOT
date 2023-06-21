import discord
import json
from discord.ext import commands
from discord import app_commands

class ResetpointsCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="resetpoints", description="Reset points for all members.")
  async def resetpoints(self, interaction: discord.Interaction):
    ctx = interaction
    if ctx.guild:
      if not ctx.user.guild_permissions.administrator:
        embed = discord.Embed(title="Leaderboard reset points", description="You don't have permission to use this command.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
      else:
        with open('level.json', 'r') as f:
          points = json.load(f)
        points[str(ctx.guild.id)] = {}
        with open('level.json', 'w') as f:
          json.dump(points, f)
        embed = discord.Embed(title="Leaderboard reset points", description="All points have reset to 0 for all members on this server.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
    else:
      embed = discord.Embed(title="Leaderboard reset points", description="You can't use this command when you're in DM.", color=0x3f48cc)
      await interaction.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(ResetpointsCommandSlash(bot))