import discord
from discord.ext import commands
import json

class CommandsCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.load_command_states()

  @commands.command()
  async def commands(self, ctx, command: str = None):
    async with ctx.typing():
      if ctx.guild:
        if not ctx.author.guild_permissions.administrator:
          embed = discord.Embed(title="Commands management", description="You don't have permission to use this command.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author=False)
          return
        if command is None:
          embed = discord.Embed(title="Commands management", description="Please enter a command to enable/disable.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author=False)
          return
        commands = self.bot.get_command(command)
        if commands:
          guild_id = str(ctx.guild.id)
          if guild_id not in self.bot.command_states:
            self.bot.command_states[guild_id] = {}
          if command in self.bot.command_states[guild_id]:
            self.bot.command_states[guild_id][command] = not self.bot.command_states[guild_id][command]
          else:
            self.bot.command_states[guild_id][command] = False
          state = "enabled" if self.bot.command_states[guild_id][command] else "disabled"
          embed = discord.Embed(title="Commands management", description=f"`{command}` command has been {state}.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author=False)
          self.save_command_states()  # Save command states to JSON file
        else:
          embed = discord.Embed(title="Commands management", description="Invalid command name.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author=False)
      else:
        embed = discord.Embed(title="Commands management", description="You can use this command when you're in DM.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author=False)

  def save_command_states(self):
    with open(".jsondata/commands.json", "w") as file:
      json.dump(self.bot.command_states, file)

  def load_command_states(self):
    try:
      with open(".jsondata/commands.json", "r") as file:
        self.bot.command_states = json.load(file)
    except FileNotFoundError:
      self.bot.command_states = {}

def setup(bot):
    bot.add_cog(CommandsCommand(bot))
