import discord
import psutil
import datetime
from discord.ext import commands
from discord import app_commands

start_time = datetime.datetime.now()

class BotinfoCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="botinfo", description="Give information about this bot.") # About this bot with hardware status
  async def botinfo(self, interaction: discord.Interaction):
    # Bot storage
    memory_used = psutil.Process().memory_info().rss / (512 * 512)
    memory_used_mb = str(memory_used)[:3] + "MB"
    # Bot stats
    total_servers = len(self.bot.guilds)
    total_channels = sum(len(guild.channels) for guild in self.bot.guilds)
    total_members = sum(len(guild.members) for guild in self.bot.guilds)
    # Show uptime usage
    current_time = datetime.datetime.now()
    uptime = current_time - start_time
    uptime_datetime = datetime.datetime.fromtimestamp(uptime.total_seconds())
    uptime_string = uptime_datetime.strftime("%d days %H hours %M minutes %S seconds")
    if uptime_string.startswith("01"):
      uptime_string = "00" + uptime_string[2:]
    # Show bot status in embed message
    member = self.bot.get_user(1098583942145257534)
    embed = discord.Embed(color=0x3f48cc)
    embed.set_author(name="tkBOT")
    embed.set_thumbnail(url=member.avatar.url)
    # About bot specifications
    embed.add_field(name='**Bot specifications**', value=f'- 🤖｜Bot Version: 1.9.5.20230622\n- 🏓｜Ping-pong respond time: {round(self.bot.latency * 1000)} ms\n- ⌚｜Uptime: {uptime_string}', inline=False)
    embed.add_field(name='**Stats**', value=f"- 🏠｜Servers: {total_servers}\n- 📝｜Channels: {total_channels}\n- 👥｜Members: {total_members}", inline=False)
    embed.add_field(name='**Hardware info**', value=f'- 💻｜CPU Usage: {psutil.cpu_percent()}%\n- 📝｜RAM Usage: {memory_used_mb}/512MB', inline=False)
    embed.add_field(name='**Links**', value="- ➕｜[Add to server](https://discord.com/api/oauth2/authorize?client_id=1098583942145257534&permissions=8&scope=applications.commands%20bot)\n- 🏠｜[Support server](https://discord.com/invite/FuuzWRqYaz)\n- 📂｜[Replit Project](https://repl.it/@truongkhoaui/tkBOT)", inline=False)
    await interaction.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(BotinfoCommandSlash(bot))