import discord
from discord.ext import commands

class EchoCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="echo", description="Repeat a message.")
  async def echo(self, ctx, *, message=None):
    async with ctx.typing():
      if message is None:
        embed = discord.Embed(title="Please enter a keyword!", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author=False)
      else:
        await ctx.reply(message, mention_author=False)

def setup(bot):
  bot.add_cog(EchoCommand(bot))