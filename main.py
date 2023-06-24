# Import packages to make bot work correctly
import datetime; import discord; import os
# Import the sub-packages
from discord.ext import commands; from keep_alive import keep_alive; from discord import app_commands

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Import commands
from prefixcommands.ban import BanCommand; from slashcommands.ban import BanCommandSlash
from prefixcommands.botinfo import BotinfoCommand; from slashcommands.botinfo import BotinfoCommandSlash
from prefixcommands.echo import EchoCommand; from slashcommands.echo import EchoCommandSlash
from prefixcommands.help import HelpCommand; from slashcommands.help import HelpCommandSlash
from prefixcommands.image import ImageCommand; from slashcommands.image import ImageCommandSlash
from prefixcommands.kick import KickCommand; from slashcommands.kick import KickCommandSlash
from prefixcommands.leaderboard import LeaderboardCommand; from slashcommands.leaderboard import LeaderboardCommandSlash
from prefixcommands.mute import MuteCommand; from slashcommands.mute import MuteCommandSlash
from prefixcommands.pfp import PfpCommand; from slashcommands.pfp import PfpCommandSlash
from prefixcommands.ping import PingCommand; from slashcommands.ping import PingCommandSlash
from prefixcommands.resetpoints import ResetpointsCommand; from slashcommands.resetpoints import ResetpointsCommandSlash
from prefixcommands.serverinfo import ServerinfoCommand; from slashcommands.serverinfo import ServerinfoCommandSlash
from prefixcommands.timeout import TimeoutCommand; from slashcommands.timeout import TimeoutCommandSlash
from prefixcommands.unmute import UnmuteCommand; from slashcommands.unmute import UnmuteCommandSlash
from prefixcommands.userinfo import UserinfoCommand; from slashcommands.userinfo import UserinfoCommandSlash
from prefixcommands.wikidiscovery import WikidiscoveryCommand; from slashcommands.wikidiscovery import WikidiscoveryCommandSlash
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
client = discord.Client(intents = intents)
client = commands.Bot(command_prefix='tk!', intents = intents)
client.remove_command("help")
print("Connecting...")

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Import function
start_time = datetime.datetime.now()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# View the custom status of bot and bot connect status
@client.event # Connected status
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game(name="tk!help and /help"))
  # Import commands
  await client.add_cog(BanCommand(client)); await client.add_cog(BanCommandSlash(client))
  await client.add_cog(BotinfoCommand(client)); await client.add_cog(BotinfoCommandSlash(client))
  await client.add_cog(EchoCommand(client)); await client.add_cog(EchoCommandSlash(client))
  await client.add_cog(HelpCommand(client)); await client.add_cog(HelpCommandSlash(client))
  await client.add_cog(ImageCommand(client)); await client.add_cog(ImageCommandSlash(client))
  await client.add_cog(KickCommand(client)); await client.add_cog(KickCommandSlash(client))
  await client.add_cog(LeaderboardCommand(client)); await client.add_cog(LeaderboardCommandSlash(client))
  await client.add_cog(MuteCommand(client)); await client.add_cog(MuteCommandSlash(client))
  await client.add_cog(PfpCommand(client)); await client.add_cog(PfpCommandSlash(client))
  await client.add_cog(PingCommand(client)); await client.add_cog(PingCommandSlash(client))
  await client.add_cog(ResetpointsCommand(client)); await client.add_cog(ResetpointsCommandSlash(client))
  await client.add_cog(ServerinfoCommand(client)); await client.add_cog(ServerinfoCommandSlash(client))
  await client.add_cog(TimeoutCommand(client)); await client.add_cog(TimeoutCommandSlash(client))
  await client.add_cog(UnmuteCommand(client)); await client.add_cog(UnmuteCommandSlash(client))
  await client.add_cog(UserinfoCommand(client)); await client.add_cog(UserinfoCommandSlash(client))
  await client.add_cog(WikidiscoveryCommand(client)); await client.add_cog(WikidiscoveryCommandSlash(client))
  # Import chatlog code
  await client.add_cog(Messagesent(client))
  await client.add_cog(Messageedit(client))
  await client.add_cog(Messagedelete(client))  
  await client.add_cog(Serverjoin(client))
  await client.add_cog(Serverkick(client))
  # If this text does not appear in print command, that means the bot failed to connect
  class TextFormat:
    BOLD = '\033[1m'
    RESET = '\033[0m'
  print("Last connected at", TextFormat.BOLD + f"{start_time.strftime('%a %d %B %Y, %I:%M %p')}" + TextFormat.RESET)
  print(f"Successfully connected to Discord Bot account as", TextFormat.BOLD + f"{client.user}" + TextFormat.RESET)
  session_id = client._connection._get_websocket(shard_id=None).session_id
  botconnectid = client.get_channel(int(os.getenv('bot_channel_connect_id')))
  try:
    synced = await client.tree.sync()
    print(f"Synced {len(synced)} slash command(s) to the bot")
  except Exception as e:
    print(e)
  embed = discord.Embed(title="Bot Connected", description=f"- **Last connected:** {start_time.strftime('%a %d %B %Y, %I:%M %p')}.\n- **Commands in total:** {len(synced)} command(s)\n- **Session ID:** {session_id}", color=0x3f48cc)    
  await botconnectid.send(embed=embed)
  print()
  print("----------------------------------------")
  print()

# Ignore the command error
@client.event
async def on_command_error(ctx, error):
  async with ctx.typing():
    if isinstance(error, commands.CommandNotFound):
      embed = discord.Embed(title="Command not found", description="The command you provived is not available or not registered.", color=0x3f48cc)
      await ctx.reply(embed=embed, mention_author = False)



# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Keep bot online 24/7 and token included
keep_alive()
client.run(os.environ['bot_token'])
