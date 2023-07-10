import discord
import json
import os
from discord.ext import commands
from discord import app_commands

class RankresetCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="rankreset", description="Reset points for all members.")
  async def rankreset(self, interaction: discord.Interaction):
    if not self.bot.command_states.get(str(interaction.guild.id), {}).get("rankreset", True):
      embed = discord.Embed(title="This command has been disabled on this server.", color=0x3f48cc)
      await interaction.response.send_message(embed=embed, ephemeral=True)
      return    
    ctx = interaction
    await interaction.response.defer(ephemeral = False)
    if ctx.guild:
      if not ctx.user.guild_permissions.administrator:
        embed = discord.Embed(title="Leaderboard reset points", description="You don't have permission to use this command.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
      else:
        with open(os.getenv('leaderboard_directory'), 'r') as f:
          points = json.load(f)
        points[str(ctx.guild.id)] = {}
        with open(os.getenv('leaderboard_directory'), 'w') as f:
          json.dump(points, f)
        embed = discord.Embed(title="Leaderboard reset points", description="All points have reset to 0 for all members on this server.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
    else:
      embed = discord.Embed(title="Leaderboard reset points", description="You can't use this command when you're in DM.", color=0x3f48cc)
      await interaction.followup.send(embed=embed)

def setup(bot):
  bot.add_cog(RankresetCommandSlash(bot))