import discord
import os
from discord.ext import commands

class Messagedelete(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message_delete(self, message):
    if message.author == self.bot.user:
      return
    # Get channel ID
    channel = self.bot.get_channel(int(os.getenv('bot_channel_deleted_message')))
    embed = discord.Embed(color=0x3f48cc)
    embed.set_author(name=message.author, icon_url=message.author.display_avatar.url)
    attachment_urls = ' | '.join([attachment.url for attachment in message.attachments])
    # Show embed message
    if len(message.embeds) > 0:
      content = "**Embed message**"
    else:
      content = message.content
    if attachment_urls:
      attachment_text = f"｜[attachment]({attachment_urls})"
    else:
      attachment_text = ""
    # Send the message when they have deleted from the server with this bot added
    if not isinstance(message.channel, discord.channel.DMChannel):
      embed.add_field(name="Message deleted", value=f"- **Content:** {message.content}{attachment_text}\n- **Deleted time:** {message.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n- **Deleted at:** {message.guild.name}")
      await channel.send(embed=embed)

def setup(bot):
  bot.add_cog(Messagedelete(bot))