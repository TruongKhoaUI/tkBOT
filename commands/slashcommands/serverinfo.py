import discord
from discord.ext import commands
from discord import app_commands

class ServerinfoCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="serverinfo", description="View the current server you're in.") # View server information
  async def serverinfo(self, interaction: discord.Interaction):
    ctx = interaction  
    await interaction.response.defer(ephemeral = False)
    if ctx.guild:
      current_server = ctx.guild
      # View the guild you're in
      embed = discord.Embed(title=f"{current_server.name}", description=f"\n- 👤｜Server Owner: {current_server.owner}\n- 🆔｜Server ID: {current_server.id}\n- 📅｜Created on: {current_server.created_at.strftime('%a %d %B %Y, %I:%M %p')}\n- 👥｜Members in total: {current_server.member_count} member(s)\n- 🥇｜Roles in total: {len(current_server.roles)} role(s)\n- 💬｜Channels in total: {len(current_server.channels)} channel(s)\n- 🔊｜Voice channels in total: {len(current_server.voice_channels)} voice channel(s)\n- ✅｜Verification Level: {current_server.verification_level}", color=0x3f48cc)
      # View the guild but if the server icon is empty, it won't show any images
      if current_server.icon is not None:
        embed.set_thumbnail(url=current_server.icon.url)
      else:
        embed.set_thumbnail(url=None)
    # If you are in DM, it will send this message
    else:
      embed = discord.Embed(title="Server Information", description="You are not on any server. Try to go to any server and use this command.", color=0x3f48cc)
    await interaction.followup.send(embed=embed)

def setup(bot):
  bot.add_cog(ServerinfoCommandSlash(bot))