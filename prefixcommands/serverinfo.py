import discord
from discord.ext import commands

class ServerinfoCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command() # View server information
  async def serverinfo(self, ctx):
    async with ctx.typing():
      if ctx.guild:
        current_server = ctx.guild
        # View the guild you're in
        embed = discord.Embed(title=f"{current_server.name}", description=f"\n- 👤｜Server Owner: {current_server.owner}\n- 🆔｜Server ID: {current_server.id}\n- 📅｜Created on: {current_server.created_at.strftime('%a %d %B %Y, %I:%M %p')}\n- 👥｜Members in total: {current_server.member_count} member(s)\n- 🥇｜Roles in total: {len(current_server.roles)} role(s)\n- 💬｜Channels in total: {len(current_server.channels)} channel(s)\n- 🔊｜Voice channels in total: {len(current_server.voice_channels)} voice channel(s)", color=0x3f48cc)
        # View the guild but if the server icon is empty, it won't show any images
        if current_server.icon is not None:
          embed.set_thumbnail(url=current_server.icon.url)
        else:
          embed.set_thumbnail(url=None)
      # If you are in DM, it will send this message
      else:
        embed = discord.Embed(title="Server Information", description="", color=0x3f48cc)
        embed.add_field(name="There isn't any server now...", value="No server joined, or currently in DM.", inline=False)
      await ctx.reply(embed=embed, mention_author = False)

def setup(bot):
  bot.add_cog(ServerinfoCommand(bot))