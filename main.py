import datetime
import discord
import os
from discord import app_commands
from keep_alive import keep_alive
from discord.ext import commands
# Import chatlog code
from commands.botlogsmessage.messagesent import Messagesent
from commands.botlogsmessage.messageedit import Messageedit
from commands.botlogsmessage.messagedelete import Messagedelete
from commands.botlogsmessage.svjoined import Serverjoin
from commands.botlogsmessage.svkicked import Serverkick
# Import prefix commands
from commands.prefixcommands.ban import BanCommand
from commands.prefixcommands.botinfo import BotinfoCommand
from commands.prefixcommands.commands import CommandsCommand
from commands.prefixcommands.echo import EchoCommand
from commands.prefixcommands.help import HelpCommand
from commands.prefixcommands.image import ImageCommand
from commands.prefixcommands.kick import KickCommand
from commands.prefixcommands.pfp import PfpCommand
from commands.prefixcommands.ping import PingCommand
from commands.prefixcommands.poll import PollCommand
from commands.prefixcommands.rank import RankCommand
from commands.prefixcommands.rankreset import RankresetCommand
from commands.prefixcommands.rankresetuser import RankresetuserCommand
from commands.prefixcommands.serverinfo import ServerinfoCommand
from commands.prefixcommands.timeout import TimeoutCommand
from commands.prefixcommands.userinfo import UserinfoCommand
from commands.prefixcommands.warn import WarnCommand
from commands.prefixcommands.wikidiscovery import WikidiscoveryCommand
# Import slash commands
from commands.slashcommands.ban import BanCommandSlash
from commands.slashcommands.botinfo import BotinfoCommandSlash
from commands.slashcommands.commands import CommandsCommandSlash
from commands.slashcommands.echo import EchoCommandSlash
from commands.slashcommands.help import HelpCommandSlash
from commands.slashcommands.image import ImageCommandSlash
from commands.slashcommands.kick import KickCommandSlash
from commands.slashcommands.pfp import PfpCommandSlash
from commands.slashcommands.ping import PingCommandSlash
from commands.slashcommands.poll import PollCommandSlash
from commands.slashcommands.rank import RankCommandSlash
from commands.slashcommands.rankreset import RankresetCommandSlash
from commands.slashcommands.rankresetuser import RankresetuserCommandSlash
from commands.slashcommands.serverinfo import ServerinfoCommandSlash
from commands.slashcommands.timeout import TimeoutCommandSlash
from commands.slashcommands.userinfo import UserinfoCommandSlash
from commands.slashcommands.warn import WarnCommandSlash
from commands.slashcommands.wikidiscovery import WikidiscoveryCommandSlash

# Bot settings
# Commands
bot = commands.Bot(command_prefix='tk!', intents = discord.Intents.all())
bot.remove_command("help")
bot.command_states = {}

# View the custom status of bot and bot connect status
@bot.event  # Connected status
async def on_ready():
  await bot.change_presence(activity=discord.Game(name='tk!help and /help'), status=discord.Status.online)
  # Register chatlog code
  await bot.add_cog(Messagesent(bot))
  await bot.add_cog(Messageedit(bot))
  await bot.add_cog(Messagedelete(bot))
  await bot.add_cog(Serverjoin(bot))
  await bot.add_cog(Serverkick(bot))  
  # Register prefix commands
  await bot.add_cog(BanCommand(bot))
  await bot.add_cog(BotinfoCommand(bot))
  await bot.add_cog(CommandsCommand(bot))
  await bot.add_cog(EchoCommand(bot))
  await bot.add_cog(HelpCommand(bot))
  await bot.add_cog(ImageCommand(bot))
  await bot.add_cog(KickCommand(bot))
  await bot.add_cog(PfpCommand(bot))
  await bot.add_cog(PingCommand(bot))
  await bot.add_cog(PollCommand(bot))
  await bot.add_cog(RankCommand(bot))  
  await bot.add_cog(RankresetCommand(bot))
  await bot.add_cog(RankresetuserCommand(bot))
  await bot.add_cog(ServerinfoCommand(bot))
  await bot.add_cog(TimeoutCommand(bot))
  await bot.add_cog(UserinfoCommand(bot))
  await bot.add_cog(WarnCommand(bot))
  await bot.add_cog(WikidiscoveryCommand(bot))
  # Register slash commands
  await bot.add_cog(BanCommandSlash(bot))  
  await bot.add_cog(BotinfoCommandSlash(bot))  
  await bot.add_cog(CommandsCommandSlash(bot))
  await bot.add_cog(EchoCommandSlash(bot))  
  await bot.add_cog(HelpCommandSlash(bot))  
  await bot.add_cog(ImageCommandSlash(bot))
  await bot.add_cog(KickCommandSlash(bot))
  await bot.add_cog(PfpCommandSlash(bot))
  await bot.add_cog(PingCommandSlash(bot))  
  await bot.add_cog(PollCommandSlash(bot))
  await bot.add_cog(RankCommandSlash(bot))  
  await bot.add_cog(RankresetCommandSlash(bot)) 
  await bot.add_cog(RankresetuserCommandSlash(bot))
  await bot.add_cog(ServerinfoCommandSlash(bot))  
  await bot.add_cog(TimeoutCommandSlash(bot))  
  await bot.add_cog(UserinfoCommandSlash(bot))  
  await bot.add_cog(WarnCommandSlash(bot))  
  await bot.add_cog(WikidiscoveryCommandSlash(bot))  
  # If this text does not appear in print command, that means the bot failed to connect
  start_time = datetime.datetime.utcnow()
  session_id = bot._connection._get_websocket(shard_id=None).session_id
  botconnectid = bot.get_channel(int(os.getenv('bot_channel_connect_id')))
  print(f"Last connected as {bot.user} since {start_time.strftime('%a %d %B %Y, %I:%M %p')}")
  # Sync slash commands with bot.tree.sync
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} slash command(s) to the bot")
  except Exception as e:
    print(e)
  embed = discord.Embed(title="Bot Connected", description=f"- **Last connected:** {start_time.strftime('%a %d %B %Y, %I:%M %p')}.\n- **Commands in total:** {len(synced)} command(s)\n- **Session ID:** {session_id}", color=0x3f48cc)
  await botconnectid.send(embed=embed)

@bot.event
async def on_message(message):
  # Check if the message is a command and if it's disabled
  if message.content.startswith(bot.command_prefix) and not message.author.bot:
    command = message.content.split(" ")[0][len(bot.command_prefix):]
    if bot.command_states.get(str(message.guild.id), {}).get(command) is False:
      return  # Command is disabled, don't execute
  await bot.process_commands(message)

# Keep bot online 24/7 and token included
keep_alive()
bot.run(os.getenv('bot_token'))
