import discord
import os
from discord.ext import commands

class Messageedit(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message_edit(self, before, after):
    if before.author == self.bot.user:
      return
    # Get channel ID
    channel = self.bot.get_channel(int(os.getenv('bot_channel_edited_message')))
    embed = discord.Embed(color=0x3f48cc)
    embed.set_author(name=before.author, icon_url=before.author.display_avatar.url)
    attachment_urls = ' | '.join([attachment.url for attachment in before.attachments])
    # Show embed message
    if len(before.embeds) > 0:
      edited_content = "**Embed message**"
    else:
      edited_content = before.content
    if len(after.embeds) > 0:
      edited_content = "**Embed message**"
    else:
      edited_content = after.content
    if attachment_urls:
      attachment_text = f"｜[attachment]({attachment_urls})"
    else:
      attachment_text = ""
    # Send the message when they have edited the server with this bot added
    if not isinstance(before.channel, discord.channel.DMChannel):
      embed.add_field(name="Message edited", value=f"- **Original content:** {before.content}{attachment_text}\n- **Edited content:** {edited_content}{attachment_text}\n- **Edited time:** {after.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n- **Edited at:** {before.guild.name}")
      await channel.send(embed=embed)

def setup(bot):
  bot.add_cog(Messagesedit(bot))