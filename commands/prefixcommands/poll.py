import discord
from discord.ext import commands

class PollCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(name="poll", description="Create a poll")
  async def poll(self, ctx, *, poll_input):
    async with ctx.typing():
      options = poll_input.split("|")
      question = options[0].strip()
      choices = [choice.strip() for choice in options[1:]]
      if len(choices) is None:
        embed = discord.Embed(title="Poll question", description="The reaction must be required for the question.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author = False)
      if len(choices) > 5:
        embed = discord.Embed(title="Poll question", description="You can only provide a maximum of 5 options.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author = False)
        return
      emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
      poll_message = ""
      for i, choice in enumerate(choices):
        poll_message += f"{emojis[i]}: {choice}\n"
      poll_embed = discord.Embed(title="Poll question", description=f"**{question}**", color=0x3f48cc)
      poll_embed.set_author(name=f"{ctx.author}'s poll", icon_url=ctx.author.avatar.url)
      for i, choice in enumerate(choices):
        poll_embed.add_field(name="", value=f"{emojis[i]}: {choice}", inline=False)
      poll_message = await ctx.reply(embed=poll_embed, mention_author = False)
      for i in range(len(choices)):
        await poll_message.add_reaction(emojis[i])

def setup(bot):
  bot.add_cog(PollCommand(bot))