import discord
from discord.ext import commands
from discord import app_commands

class CommandsstatesCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="commandsstates", description="View all enable/disable commands.")
  async def commandsstates(self, interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=False)
    ctx = interaction
    if ctx.guild:
      guild_id = str(ctx.guild.id)
      if guild_id not in self.bot.command_states:
        self.bot.command_states[guild_id] = {}
      enabled_commands = [
        f"- :white_check_mark: `{cmd}`" if self.bot.command_states[guild_id].get(str(cmd), True) else f"- :x: `{cmd}`"
        for cmd in sorted(self.bot.commands, key=lambda c: str(c))
      ]
      enabled_commands_text = "\n".join(enabled_commands)
      embed = discord.Embed(title="Commands states", description=enabled_commands_text, color=0x3f48cc)
      await interaction.followup.send(embed=embed)
    else:
      embed = discord.Embed(title="Commands states", description="You can't view the commands states when you're in DM.", color=0x3f48cc)
      await interaction.followup.send(embed=embed)      

def setup(bot):
    bot.add_cog(CommandsstatesCommandSlash(bot))