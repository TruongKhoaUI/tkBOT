import discord
import psutil
import datetime
from discord.ext import commands
from discord.ui import Button, View

start_time = datetime.datetime.now()

class BotinfoCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="botinfo", description="View information about this bot.") # About this bot with hardware status
  async def botinfo(self, ctx):  
    async with ctx.typing():
      # Buttons
      addserver = Button(label="Invite me", url = "https://discord.com/api/oauth2/authorize?client_id=1098583942145257534&permissions=8&scope=applications.commands%20bot", emoji = "➕")
      support = Button(label = "Support server", url = "https://discord.com/invite/FuuzWRqYaz", emoji = "🏠")
      gitproject = Button(label = "GitHub Repo", url = "https://github.com/TruongKhoaUI/tkBOT", emoji = "📂")      
      # Bot storage
      memory_used = psutil.Process().memory_info().rss / (512 * 512)
      memory_used_mb = str(memory_used)[:5] + "MB"
      disk_usage = psutil.disk_usage('/home/runner/tkBOT')
      used_disk_space = disk_usage.used / (1024 * 1024)
      used_disk_space_mb = str(used_disk_space)[:5]
      # Bot stats
      total_servers = len(self.bot.guilds)
      total_channels = sum(len(guild.channels) for guild in self.bot.guilds)
      total_voice_channels = sum(len(guild.voice_channels) for guild in self.bot.guilds)
      total_members = sum(len(guild.members) for guild in self.bot.guilds)
      # Show uptime usage
      boot_time = psutil.boot_time()
      current_time = datetime.datetime.now()
      uptime = current_time - datetime.datetime.fromtimestamp(boot_time)          
      days = uptime.days
      hours, remainder = divmod(uptime.seconds, 3600)
      minutes, seconds = divmod(remainder, 60)            
      uptime_string = f"{days} days {hours} hours {minutes} minutes {seconds} seconds"
      # Show bot status in embed message
      member = self.bot.get_user(1098583942145257534)
      embed = discord.Embed(
        title="Bot Information",
        description=f"**Bot specifications**\n"
                    f"- 🤖｜Bot Version: 2.0.3.20230710\n"
                    f"- 🏓｜Ping-pong respond time: {round(self.bot.latency * 1000)} ms\n"
                    f"- ⌚｜Uptime: {uptime_string}\n"
                    f"**Stats**\n"
                    f"- 🏠｜Servers: {total_servers}\n"
                    f"- 📝｜Channels: {total_channels}\n"
                    f"- 🔊｜Voice Channels: {total_voice_channels}\n"
                    f"- 👥｜Members: {total_members}\n"
                    f"**Hardware info**\n"
                    f"- 💻｜CPU Usage: {psutil.cpu_percent()}%\n"
                    f"- 📝｜RAM Usage: {memory_used_mb}/512MB\n"
                    f"**Helpers**\n"
                    f"- [truongkhoa](discord://-/users/1021023635814760458) (owner)\n"
                    f"- [mr5g](discord://-/users/936240483980693525)",
        color=0x3f48cc
      )      
      embed.set_author(name="tkBOT", icon_url=member.avatar.url)
      view = View()
      view.add_item(addserver)
      view.add_item(support)
      view.add_item(gitproject)
      await ctx.reply(embed=embed, view=view, mention_author = False)

def setup(bot):
  bot.add_cog(BotinfoCommand(bot))