import datetime
import discord
import os
import sys
import logging
from keep_alive import keep_alive
from discord.ext import commands

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Import commands
from commands.prefixcommands.ban import BanCommand; from commands.slashcommands.ban import BanCommandSlash
from commands.prefixcommands.botinfo import BotinfoCommand; from commands.slashcommands.botinfo import BotinfoCommandSlash
from commands.prefixcommands.echo import EchoCommand; from commands.slashcommands.echo import EchoCommandSlash
from commands.prefixcommands.help import HelpCommand; from commands.slashcommands.help import HelpCommandSlash
from commands.prefixcommands.image import ImageCommand; from commands.slashcommands.image import ImageCommandSlash
from commands.prefixcommands.kick import KickCommand; from commands.slashcommands.kick import KickCommandSlash
from commands.prefixcommands.leaderboard import LeaderboardCommand; from commands.slashcommands.leaderboard import LeaderboardCommandSlash
from commands.prefixcommands.pfp import PfpCommand; from commands.slashcommands.pfp import PfpCommandSlash
from commands.prefixcommands.ping import PingCommand; from commands.slashcommands.ping import PingCommandSlash
from commands.prefixcommands.resetpoints import ResetpointsCommand; from commands.slashcommands.resetpoints import ResetpointsCommandSlash
from commands.prefixcommands.serverinfo import ServerinfoCommand; from commands.slashcommands.serverinfo import ServerinfoCommandSlash
from commands.prefixcommands.timeout import TimeoutCommand; from commands.slashcommands.timeout import TimeoutCommandSlash
from commands.prefixcommands.userinfo import UserinfoCommand; from commands.slashcommands.userinfo import UserinfoCommandSlash
from commands.prefixcommands.warn import WarnCommand; from commands.slashcommands.warn import WarnCommandSlash
from commands.prefixcommands.wikidiscovery import WikidiscoveryCommand; from commands.slashcommands.wikidiscovery import WikidiscoveryCommandSlash
# Import chatlog code
from botlogsmessage.messagesent import Messagesent
from botlogsmessage.messageedit import Messageedit
from botlogsmessage.messagedelete import Messagedelete
from botlogsmessage.svjoined import Serverjoin
from botlogsmessage.svkicked import Serverkick

# Bot settings
# Authentication
token = os.getenv('bot_token')
if not token:
  sys.exit("Please put your token before starting the bot.")
# Commands
bot = commands.Bot(command_prefix='tk!', intents = discord.Intents.all())
bot.remove_command("help")
print("Connecting...")
logging.getLogger("discord.gateway").setLevel(logging.ERROR)
logging.getLogger("discord.client").setLevel(logging.ERROR)

# View the custom status of bot and bot connect status
@bot.event  # Connected status
async def on_ready():
  game = discord.Game(name='tk!help and /help')
  await bot.change_presence(activity=game, status=discord.Status.online)
  # Import commands
  await bot.add_cog(BanCommand(bot)); await bot.add_cog(BanCommandSlash(bot))
  await bot.add_cog(BotinfoCommand(bot));  await bot.add_cog(BotinfoCommandSlash(bot))
  await bot.add_cog(EchoCommand(bot)); await bot.add_cog(EchoCommandSlash(bot))
  await bot.add_cog(HelpCommand(bot)); await bot.add_cog(HelpCommandSlash(bot))
  await bot.add_cog(ImageCommand(bot)); await bot.add_cog(ImageCommandSlash(bot))
  await bot.add_cog(KickCommand(bot)); await bot.add_cog(KickCommandSlash(bot))
  await bot.add_cog(LeaderboardCommand(bot)); await bot.add_cog(LeaderboardCommandSlash(bot))
  await bot.add_cog(PfpCommand(bot)); await bot.add_cog(PfpCommandSlash(bot))
  await bot.add_cog(PingCommand(bot)); await bot.add_cog(PingCommandSlash(bot))
  await bot.add_cog(ResetpointsCommand(bot)); await bot.add_cog(ResetpointsCommandSlash(bot))
  await bot.add_cog(ServerinfoCommand(bot)); await bot.add_cog(ServerinfoCommandSlash(bot))
  await bot.add_cog(TimeoutCommand(bot)); await bot.add_cog(TimeoutCommandSlash(bot))
  await bot.add_cog(UserinfoCommand(bot)); await bot.add_cog(UserinfoCommandSlash(bot))
  await bot.add_cog(WarnCommand(bot)); await bot.add_cog(WarnCommandSlash(bot))
  await bot.add_cog(WikidiscoveryCommand(bot)); await bot.add_cog(WikidiscoveryCommandSlash(bot))
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
  # Sync slash commands with bot.tree.sync
  try:
    synced = await bot.tree.sync()
    print("Synced", TextFormat.BOLD + f"{len(synced)} slash command(s)" + TextFormat.RESET, "to the bot")
  except Exception as e:
    print(e)
  embed = discord.Embed(title="Bot Connected", description=f"- **Last connected:** {start_time.strftime('%a %d %B %Y, %I:%M %p')}.\n- **Commands in total:** {len(synced)} command(s)\n- **Session ID:** {session_id}", color=0x3f48cc)
  await botconnectid.send(embed=embed)

# Keep bot online 24/7 and token included
keep_alive()
bot.run(token)
