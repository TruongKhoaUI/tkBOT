import discord
from discord.ext import commands
from discord import app_commands

class PollCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="poll", description="Generate your question to the members.") # Create a daily question
  @app_commands.describe(question="Send a question.")
  async def poll(self, interaction: discord.Interaction, question: str):
    ctx = interaction
    if ctx.guild:
      author = ctx.user
      # Create a poll
      embed = discord.Embed(title=f"Poll Questions", color=0x3f48cc)
      embed.add_field(name=f"Question by {author}:", value=f"- {question}", inline=False)
      # Add the reactions
      msg = await ctx.channel.send(embed=embed)
      await msg.add_reaction('👍')
      await msg.add_reaction('🤷')
      await msg.add_reaction('👎')
    else:
      embed = discord.Embed(title=f"Poll Questions", description="Please create a question for the member on the specific server.", color=0x3f48cc)
      await interaction.response.send_message(embed=embed)
      
def setup(bot):
  bot.add_cog(PollCommandSlash(bot))