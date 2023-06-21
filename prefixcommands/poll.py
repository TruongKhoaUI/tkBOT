import discord
from discord.ext import commands

class PollCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command() # Create a daily question
  async def poll(self, ctx, *, question=None):
    async with ctx.typing():
      if ctx.guild:
        author = ctx.author
        # If the `question` value is empty, it will send a message that needs a keyword on that value
        if question is None:
          embed = discord.Embed(title="Poll Questions", description="**Please put a question!**", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author=False)
        else:
          await ctx.message.delete()
          # Create a poll
          embed = discord.Embed(title=f"Poll Questions", color=0x3f48cc)
          embed.add_field(name=f"Question by {author}:", value=f"- {question}", inline=False)
          msg = await ctx.send(embed=embed, mention_author=False)
          # Add the reactions
          await msg.add_reaction('👍')
          await msg.add_reaction('🤷')
          await msg.add_reaction('👎')
      else:
        embed = discord.Embed(title=f"Poll Questions", description="Please create a question for the member on the specific server.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author = False)

def setup(bot):
  bot.add_cog(PollCommand(bot))