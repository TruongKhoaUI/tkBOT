import discord
import os
from discord.ext import commands

class Serverjoin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    botinvitedid = self.bot.get_channel(int(os.getenv('bot_channel_invited_id')))
    embed = discord.Embed(title="Server Invited", description=f"I was invited to **{guild.name}** by server owner is **{guild.owner}**.", color=0x3f48cc)
    if guild.icon:
      embed.set_thumbnail(url=guild.icon.url)
    else:
      embed.set_thumbnail(url=None)
    await botinvitedid.send(embed=embed)

def setup(bot):
  bot.add_cog(Serverjoin(bot))