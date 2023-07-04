import discord
from discord.ext import commands
from discord import app_commands

class PollCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @app_commands.command(name="poll", description="Create a poll")
  @app_commands.describe(question="Enter your question.")
  @app_commands.describe(answer1="Enter the first answer.")
  @app_commands.describe(answer2="Enter the second answer.")
  @app_commands.describe(answer3="Enter the third answer.")
  @app_commands.describe(answer4="Enter the fourth answer.")
  @app_commands.describe(answer5="Enter the fifth answer.")
  async def poll(self, interaction: discord.Interaction, *, question: str, answer1: str, answer2: str, answer3: str = None, answer4: str = None, answer5: str = None):
    await interaction.response.defer(ephemeral=False)
    ctx = interaction
    options = [answer1, answer2, answer3, answer4, answer5]
    emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    poll_message = ""
    for i, option in enumerate(options):
      if option:
        poll_message += f"{emojis[i]}: {option}\n"
    poll_embed = discord.Embed(title="Poll question", description=f"**{question}**", color=0x3f48cc)
    poll_embed.set_author(name=f"{ctx.user}'s poll", icon_url=ctx.user.avatar.url)
    for i, option in enumerate(options):
      if option:
        poll_embed.add_field(name="", value=f"{emojis[i]}: {option}", inline=False)
    poll_message = await interaction.followup.send(embed=poll_embed)
    for i in range(len(options)):
      if options[i]:
        await poll_message.add_reaction(emojis[i])

def setup(bot):
  bot.add_cog(PollCommandSlash(bot))