import discord
import requests
from discord.ext import commands

class PingCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="ping", description="Show the time the bot responds.") # Show the time the bot responds
  async def ping(self, ctx):      
    async with ctx.typing():
      # Get the Discord API time response
      response = requests.get('https://discord.com')
      # Get the bot time response
      api_latency = round(response.elapsed.total_seconds() * 1000)
      embed = discord.Embed(title="Pong! 🏓", description=f"- Bot Latency: {round(self.bot.latency * 1000)} ms\n- API Latency: {api_latency} ms", color=0x3f48cc)
      await ctx.reply(embed=embed, mention_author = False)

def setup(bot):
  bot.add_cog(PingCommand(bot))