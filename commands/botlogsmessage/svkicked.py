import discord
import os
from discord.ext import commands

class Serverkick(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_guild_remove(self, guild):
    botkickedid = self.bot.get_channel(int(os.getenv('bot_channel_kicked_id')))
    embed = discord.Embed(title="Server Kicked", description=f"I was kicked from **{guild.name}** by server owner is **{guild.owner}**.", color=0x3f48cc)
    if guild.icon:
      embed.set_thumbnail(url=guild.icon.url)
    else:
      embed.set_thumbnail(url=None)
    await botkickedid.send(embed=embed)

def setup(bot):
  bot.add_cog(Serverkick(bot))