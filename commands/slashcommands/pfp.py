import discord
from discord.ext import commands
from discord import app_commands

class PfpCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="pfp", description="Show member's avatar.") # Show the profile picture
  @app_commands.describe(member="Select a specific user.")
  async def pfp(self, interaction: discord.Interaction, member: discord.User = None):
    if interaction.guild is not None and not self.bot.command_states.get(str(interaction.guild.id), {}).get("pfp", True):
      embed = discord.Embed(title="This command has been disabled on this server.", color=0x3f48cc)
      await interaction.response.send_message(embed=embed, ephemeral=True)
      return
    ctx = interaction
    await interaction.response.defer(ephemeral = False)
    # If the `member` value is empty, it will show their avatar that they have sent
    if member == None:
      member = ctx.user
    # Show the username and their profile picture
    embed = discord.Embed(title=f"{member}", color=0x3f48cc)
    # If the profile picture is empty, it will show the Discord logo
    if member.display_avatar != None:
      embed.set_image(url=member.display_avatar.url)
    await interaction.followup.send(embed=embed)

def setup(bot):
  bot.add_cog(PfpCommandSlash(bot))