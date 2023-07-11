import discord
import json
import os
from discord.ext import commands
from discord import app_commands

class RankresetCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="rankreset", description="Reset points for all members.")
  @app_commands.describe(member="Select a user to reset points for the specific user.")
  async def rankreset(self, interaction: discord.Interaction, member:discord.User = None):
    if interaction.guild is not None and not self.bot.command_states.get(str(interaction.guild.id), {}).get("rankreset", True):
      embed = discord.Embed(title="This command has been disabled on this server.", color=0x3f48cc)
      await interaction.response.send_message(embed=embed, ephemeral=True)
      return 
    ctx = interaction
    await interaction.response.defer(ephemeral = False)
    if ctx.guild:
      if not ctx.user.guild_permissions.administrator:
        embed = discord.Embed(title="Leaderboard reset points", description="You don't have permission to use this command.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
        return
      if isinstance(member, int):
        # Get userinfo from a user when they are not in the guild
        try:
          member = await self.bot.fetch_user(member)
        # It will show this message when the user ID is invaild
        except discord.errors.NotFound:
          embed = discord.Embed(title="User Information", description="Invalid user ID or username.", color=0x3f48cc)
          await interaction.followup.send(embed=embed)
          return         
      if member is None:
        with open(os.getenv('leaderboard_directory'), 'r') as f:
          points = json.load(f)
        points[str(ctx.guild.id)] = {}
        with open(os.getenv('leaderboard_directory'), 'w') as f:
          json.dump(points, f)
        embed = discord.Embed(title="Leaderboard reset points", description="All points have reset to 0 for all members on this server.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
      else:
        with open(os.getenv('leaderboard_directory'), 'r') as f:
          points = json.load(f)
        points[str(ctx.guild.id)].pop(str(member.id), None)
        with open(os.getenv('leaderboard_directory'), 'w') as f:
          json.dump(points, f)
        embed = discord.Embed(title="Leaderboard reset points", description=f"{member}'s points have been reset to 0.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)                
    else:
      embed = discord.Embed(title="Leaderboard reset points", description="You can't use this command when you're in DM.", color=0x3f48cc)
      await interaction.followup.send(embed=embed)

def setup(bot):
  bot.add_cog(RankresetCommandSlash(bot))