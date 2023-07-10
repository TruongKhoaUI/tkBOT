import discord
from discord.ext import commands

class CommandsstatesCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def commandsstates(self, ctx):
    async with ctx.typing():
      guild_id = str(ctx.guild.id)
      if guild_id not in self.bot.command_states:
        self.bot.command_states[guild_id] = {}
      enabled_commands = [
        f"- :white_check_mark: `{cmd}`" if self.bot.command_states[guild_id].get(str(cmd), True) else f"- :x: `{cmd}`"
        for cmd in sorted(self.bot.commands, key=lambda c: str(c))
      ]
      enabled_commands_text = "\n".join(enabled_commands)
      embed = discord.Embed(title="Commands states", description=enabled_commands_text, color=0x3f48cc)
      await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(CommandsstatesCommand(bot))