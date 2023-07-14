import discord
from discord.ext import commands
from discord import app_commands
import json

class CommandsCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.load_command_states()

  @app_commands.command(name="commands", description="Enable/disable a command.")
  @app_commands.describe(command="Choose a command to enable/disable")
  @app_commands.choices(command=[
    discord.app_commands.Choice(name="ban", value="ban"),
    discord.app_commands.Choice(name="botinfo", value="botinfo"),
    discord.app_commands.Choice(name="commands", value="commands"),
    discord.app_commands.Choice(name="echo", value="echo"),
    discord.app_commands.Choice(name="help", value="help"),
    discord.app_commands.Choice(name="image", value="image"),
    discord.app_commands.Choice(name="kick", value="kick"),   
    discord.app_commands.Choice(name="pfp", value="pfp"),
    discord.app_commands.Choice(name="ping", value="ping"),    
    discord.app_commands.Choice(name="poll", value="poll"),
    discord.app_commands.Choice(name="serverinfo", value="serverinfo"),
    discord.app_commands.Choice(name="timeout", value="timeout"),
    discord.app_commands.Choice(name="userinfo", value="userinfo"),
    discord.app_commands.Choice(name="warn", value="warn"),      
    discord.app_commands.Choice(name="wikidiscovery", value="wikidiscovery"),
  ])  
  async def commands(self, interaction: discord.Interaction, command: str = None):
    await interaction.response.defer(ephemeral=False)
    ctx = interaction
    if ctx.guild:
      if not ctx.user.guild_permissions.administrator:
        embed = discord.Embed(title="Commands management", description="You don't have permission to use this command.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
        return
      if command is None:
        guild_id = str(ctx.guild.id)
        if guild_id not in self.bot.command_states:
          self.bot.command_states[guild_id] = {}
        enabled_commands = [
          f"- :white_check_mark: `{cmd}`" if self.bot.command_states[guild_id].get(str(cmd), True) else f"- :x: `{cmd}`"
           for cmd in sorted(self.bot.commands, key=lambda c: str(c))
        ]
        enabled_commands_text = "\n".join(enabled_commands)
        embed = discord.Embed(title="Commands management", description=enabled_commands_text, color=0x3f48cc)
        embed.set_footer(text="Type tk!commands [command] to enable/disable a specific command.")
        await interaction.followup.send(embed=embed)
        return
      if command == "commands":
        embed = discord.Embed(title="Commands management", description="You cannot disable this command.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
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
        await interaction.followup.send(embed=embed)
        self.save_command_states()  # Save command states to JSON file
      else:
        embed = discord.Embed(title="Commands management", description="Invalid command name.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
    else:
      embed = discord.Embed(title="Commands management", description="You can use this command when you're in DM.", color=0x3f48cc)
      await interaction.followup.send(embed=embed)

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
    bot.add_cog(CommandsCommandSlash(bot))
