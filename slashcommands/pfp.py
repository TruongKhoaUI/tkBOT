import discord
from discord.ext import commands
from discord import app_commands
from typing import Union

class PfpCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="pfp", description="Show member's avatar.") # Show the profile picture
  @app_commands.describe(member="Select a specific user.")
  async def pfp(self, interaction: discord.Interaction, member: discord.User = None):
    ctx = interaction
    await interaction.response.defer(ephemeral = False)
    # If the `member` value is empty, it will show their avatar that they have sent
    if member == None:
      member = ctx.user
    # Get profile picture from a user when they are not in the guild
    if isinstance(member, int):
      user = await self.bot.fetch_user(member.id)
    else:
      user = member
    # Show the username and their profile picture
    embed = discord.Embed(title=f"{user}", color=0x3f48cc)
    # If the profile picture is empty, it will show the Discord logo
    if user.display_avatar != None:
      embed.set_image(url=user.display_avatar.url)
    await interaction.followup.send(embed=embed)

def setup(bot):
  bot.add_cog(PfpCommandSlash(bot))