import discord
from discord.ext import commands
from discord import app_commands

class EchoCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="echo", description="Repeat a message.") # Repeat the message
  @app_commands.describe(message="Enter a keyword.")
  async def echo(self, interaction: discord.Interaction, *, message: str):
    if not self.bot.command_states.get(str(interaction.guild.id), {}).get("echo", True):
      embed = discord.Embed(title="This command has been disabled on this server.", color=0x3f48cc)
      await interaction.response.send_message(embed=embed, ephemeral=True)
      return
    await interaction.response.defer(ephemeral=False)
    # Send the same message from the author
    await interaction.followup.send(message)

def setup(bot):
  bot.add_cog(EchoCommandSlash(bot))
