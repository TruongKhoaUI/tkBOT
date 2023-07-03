import discord
import wikipedia
import urllib.parse
from discord.ext import commands

class WikidiscoveryCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="wikidiscovery", description="Discorver information from Wikipedia.") # Discorvery in Wikipedia
  async def wikidiscovery(self, ctx, *, search=None):
    async with ctx.typing():
      wikisearch = urllib.parse.quote(search)
      # If the `search` value is empty, it will send a message that needs a keyword on that value
      if search is None:
        embed = discord.Embed(title="Please provide a information to let us requests!", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author = False)
      else:
        try:
          # Search the word that the user requests
          summary = wikipedia.summary(search, auto_suggest=False, redirect=True)
          embed = discord.Embed(title=f"Searched for {search}\nhttps://en.wikipedia.org/wiki/{wikisearch}", description=f"{summary}", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
        # This message will be sent if the keyword you provived is have a lot of options
        except wikipedia.exceptions.DisambiguationError as e:
          embed = discord.Embed(title=f"Searched for {search}\nhttps://en.wikipedia.org/wiki/{wikisearch}", description=f"{e}", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
        # This message will be sent if the keyword you provived is not available on Wikipedia
        except wikipedia.exceptions.PageError:
          embed = discord.Embed(title=f"Searched for {search}\nhttps://en.wikipedia.org/wiki/{wikisearch}", description="The information you provided doesn't match any query.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)

def setup(bot):
  bot.add_cog(WikidiscoveryCommand(bot))