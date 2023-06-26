import discord
from discord.ext import commands
from discord import app_commands

class EchoCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="echo", description="Repeat the message.") # Repeat the message
  @app_commands.describe(message="Enter a keyword.")
  async def echo(self, interaction: discord.Interaction, *, message: str):
    await interaction.response.defer(ephemeral = False)
    message = message
    # Send the same message from the author
    await interaction.followup.send(f"{message}")

def setup(bot):
  bot.add_cog(EchoCommandSlash(bot))