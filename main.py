import datetime
import discord
import os
import psutil
import logging
import tkinter as tk
from keep_alive import keep_alive
from discord.ext import commands

# Import the keep_alive module if you want to keep the bot online 24/7
# from keep_alive import keep_alive

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Import commands
from prefixcommands.ban import BanCommand
from slashcommands.ban import BanCommandSlash
from prefixcommands.botinfo import BotinfoCommand
from slashcommands.botinfo import BotinfoCommandSlash
from prefixcommands.echo import EchoCommand
from slashcommands.echo import EchoCommandSlash
from prefixcommands.help import HelpCommand
from slashcommands.help import HelpCommandSlash
from prefixcommands.image import ImageCommand
from slashcommands.image import ImageCommandSlash
from prefixcommands.kick import KickCommand
from slashcommands.kick import KickCommandSlash
from prefixcommands.leaderboard import LeaderboardCommand
from slashcommands.leaderboard import LeaderboardCommandSlash
from prefixcommands.mute import MuteCommand
from slashcommands.mute import MuteCommandSlash
from prefixcommands.pfp import PfpCommand
from slashcommands.pfp import PfpCommandSlash
from prefixcommands.ping import PingCommand
from slashcommands.ping import PingCommandSlash
from prefixcommands.resetpoints import ResetpointsCommand
from slashcommands.resetpoints import ResetpointsCommandSlash
from prefixcommands.serverinfo import ServerinfoCommand
from slashcommands.serverinfo import ServerinfoCommandSlash
from prefixcommands.timeout import TimeoutCommand
from slashcommands.timeout import TimeoutCommandSlash
from prefixcommands.unmute import UnmuteCommand
from slashcommands.unmute import UnmuteCommandSlash
from prefixcommands.userinfo import UserinfoCommand
from slashcommands.userinfo import UserinfoCommandSlash
from prefixcommands.wikidiscovery import WikidiscoveryCommand
from slashcommands.wikidiscovery import WikidiscoveryCommandSlash
# Import chatlog code
from botlogsmessage.messagesent import Messagesent
from botlogsmessage.messageedit import Messageedit
from botlogsmessage.messagedelete import Messagedelete
from botlogsmessage.svjoined import Serverjoin
from botlogsmessage.svkicked import Serverkick

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Bot settings
# Commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='tk!', intents=intents)
bot.remove_command("help")
print("Connecting...")
logging.getLogger("discord.gateway").setLevel(logging.ERROR)
logging.getLogger("discord.client").setLevel(logging.ERROR)

# View the custom status of bot and bot connect status
@bot.event  # Connected status
async def on_ready():
  game = discord.Game(name='tk!help and /help')
  await bot.change_presence(activity=game, status=discord.Status.dnd)
  # Import commands
  await bot.add_cog(BanCommand(bot))
  await bot.add_cog(BanCommandSlash(bot))
  await bot.add_cog(BotinfoCommand(bot))
  await bot.add_cog(BotinfoCommandSlash(bot))
  await bot.add_cog(EchoCommand(bot))
  await bot.add_cog(EchoCommandSlash(bot))
  await bot.add_cog(HelpCommand(bot))
  await bot.add_cog(HelpCommandSlash(bot))
  await bot.add_cog(ImageCommand(bot))
  await bot.add_cog(ImageCommandSlash(bot))
  await bot.add_cog(KickCommand(bot))
  await bot.add_cog(KickCommandSlash(bot))
  await bot.add_cog(LeaderboardCommand(bot))
  await bot.add_cog(LeaderboardCommandSlash(bot))
  await bot.add_cog(MuteCommand(bot))
  await bot.add_cog(MuteCommandSlash(bot))
  await bot.add_cog(PfpCommand(bot))
  await bot.add_cog(PfpCommandSlash(bot))
  await bot.add_cog(PingCommand(bot))
  await bot.add_cog(PingCommandSlash(bot))
  await bot.add_cog(ResetpointsCommand(bot))
  await bot.add_cog(ResetpointsCommandSlash(bot))
  await bot.add_cog(ServerinfoCommand(bot))
  await bot.add_cog(ServerinfoCommandSlash(bot))
  await bot.add_cog(TimeoutCommand(bot))
  await bot.add_cog(TimeoutCommandSlash(bot))
  await bot.add_cog(UnmuteCommand(bot))
  await bot.add_cog(UnmuteCommandSlash(bot))
  await bot.add_cog(UserinfoCommand(bot))
  await bot.add_cog(UserinfoCommandSlash(bot))
  await bot.add_cog(WikidiscoveryCommand(bot))
  await bot.add_cog(WikidiscoveryCommandSlash(bot))
  # Import chatlog code
  await bot.add_cog(Messagesent(bot))
  await bot.add_cog(Messageedit(bot))
  await bot.add_cog(Messagedelete(bot))
  await bot.add_cog(Serverjoin(bot))
  await bot.add_cog(Serverkick(bot))
  # If this text does not appear in print command, that means the bot failed to connect
  class TextFormat:
    BOLD = '\033[1m'
    RESET = '\033[0m'
  start_time = datetime.datetime.utcnow()
  session_id = bot._connection._get_websocket(shard_id=None).session_id
  botconnectid = bot.get_channel(int(os.getenv('bot_channel_connect_id')))
  print("Last connected at", TextFormat.BOLD + f"{start_time.strftime('%a %d %B %Y, %I:%M %p')}" + TextFormat.RESET)
  print("Successfully connected to Discord Bot account as", TextFormat.BOLD + f"{bot.user}" + TextFormat.RESET)
  try:
    synced = await bot.tree.sync()
    print("Synced", TextFormat.BOLD + f"{len(synced)} slash command(s)" + TextFormat.RESET, "to the bot")
  except Exception as e:
    print(e)
  embed = discord.Embed(title="Bot Connected", description=f"- **Last connected:** {start_time.strftime('%a %d %B %Y, %I:%M %p')}.\n- **Commands in total:** {len(synced)} command(s)\n- **Session ID:** {session_id}", color=0x3f48cc)
  await botconnectid.send(embed=embed)
  print()
  print("----------------------------------------")
  print()
  # Launch Tkinter window
  launch_window()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Launch Tkinter window
def launch_window():
  def program():
    print()
  def button_about():
    memory_used = psutil.Process().memory_info().rss / (512 * 512)
    memory_used_mb = str(memory_used)[:3] + "MB"
    program()
    window = tk.Tk()
    window.title("About tkBOT")
    window.geometry("300x200")
    window.resizable(False, False)
    label1 = tk.Label(window, text="      About tkBOT", font=("Arial", 10, "bold"), anchor="w")
    label1.pack(pady=20, anchor="w")
    label2 = tk.Label(window, text=f"      Version: 1.9.6.20230626\n      Commands in total: 1\n      RAM Usage: {memory_used_mb}/512MB", font=("Arial", 10), anchor="w", justify="left")
    label2.pack(anchor="w")    
  def on_closing():
    pass    
  window = tk.Tk()
  window.protocol("WM_DELETE_WINDOW", on_closing)
  # Function
  start_time = datetime.datetime.utcnow()
  date_format = "%d %B %Y, %I:%M %p"
  formatted_date = start_time.strftime(date_format)
  session_id = bot._connection._get_websocket(shard_id=None).session_id
  # Window
  window.title("Discord Bot Connection")
  window.geometry("400x200")
  window.resizable(False, False)
  label1 = tk.Label(window, text="      Discord Bot is running.", font=("Arial", 10, "bold"), anchor="w")
  label1.pack(pady=20, anchor="w")
  label2 = tk.Label(window, text=f"      Connect as: {bot.user}\n      Last connected at: {formatted_date}\n      Session ID: {session_id}", font=("Arial", 10), anchor="w", justify="left")
  label2.pack(anchor="w")
  program()
  button1 = tk.Button(window, text="About bot", command=button_about)
  button1.pack(side="left", padx=20, pady=20) 
  window.mainloop()

# Ignore the command error
@bot.event
async def on_command_error(ctx, error):
  async with ctx.typing():
    if isinstance(error, commands.CommandNotFound):
      embed = discord.Embed(title="Command not found", description="The command you provided is not available or not registered.", color=0x3f48cc)
      await ctx.reply(embed=embed, mention_author=False)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Keep bot online 24/7 and token included
keep_alive()
bot.run(os.environ['bot_token'])
