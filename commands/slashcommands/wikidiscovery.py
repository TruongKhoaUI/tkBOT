import discord
import wikipedia
import urllib.parse
from discord.ext import commands
from discord import app_commands

class WikidiscoveryCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="wikidiscovery", description="Discorver information from Wikipedia.") # Discorvery in Wikipedia
  @app_commands.describe(search="Enter a keyword to request a information.")
  async def wikidiscovery(self, interaction: discord.Interaction, search: str):
    if not self.bot.command_states.get(str(interaction.guild.id), {}).get("wikidiscovery", True):
      embed = discord.Embed(title="This command has been disabled on this server.", color=0x3f48cc)
      await interaction.response.send_message(embed=embed, ephemeral=True)
      return    
    await interaction.response.defer(ephemeral = False)
    wikisearch = urllib.parse.quote(search)
    try:
      # Search the word that the user requests
      summary = wikipedia.summary(search, auto_suggest=False, redirect=True)
      embed = discord.Embed(title=f"Searched for {search}\nhttps://en.wikipedia.org/wiki/{wikisearch}", description=f"{summary}", color=0x3f48cc)
      await interaction.followup.send(embed=embed)
    # This message will be sent if the keyword you provived is have a lot of options
    except wikipedia.exceptions.DisambiguationError as e:
      embed = discord.Embed(title=f"Searched for {search}\nhttps://en.wikipedia.org/wiki/{wikisearch}", description=f"{e}", color=0x3f48cc)
      await interaction.followup.send(embed=embed)
    # This message will be sent if the keyword you provived is not available on Wikipedia
    except wikipedia.exceptions.PageError:
      embed = discord.Embed(title=f"Searched for {search}\nhttps://en.wikipedia.org/wiki/{wikisearch}", description="The information you provided doesn't match any query.", color=0x3f48cc)
      await interaction.followup.send(embed=embed)

def setup(bot):
  bot.add_cog(WikidiscoveryCommandSlash(bot))