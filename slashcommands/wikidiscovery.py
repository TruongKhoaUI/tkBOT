import discord
import wikipedia
from discord.ext import commands
from discord import app_commands

class WikidiscoveryCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="wikidiscovery", description="Discorver information from Wikipedia.") # Discorvery in Wikipedia
  @app_commands.describe(search="Enter a keyword.")
  async def wikidiscovery(self, interaction: discord.Interaction, search: str):
    try:
      # Search the word that the user requests
      summary = wikipedia.summary(search, auto_suggest=False, redirect=True)
      embed = discord.Embed(title=f"Searched for {search}", description=f"{summary}", color=0x3f48cc)
      embed.set_footer(text="Some information may not correctly. Based on Wikipedia.")
      await interaction.response.send_message(embed=embed)
    # This message will be sent if the keyword you provived is have a lot of options
    except wikipedia.exceptions.DisambiguationError as e:
      embed = discord.Embed(title=f"Searched for {search}", description=f"{e}", color=0x3f48cc)
      await interaction.response.send_message(embed=embed)
    # This message will be sent if the keyword you provived is not available on Wikipedia
    except wikipedia.exceptions.PageError:
      embed = discord.Embed(title=f"Searched for {search}", description="The information you provided doesn't match any query.", color=0x3f48cc)
      await interaction.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(WikidiscoveryCommandSlash(bot))