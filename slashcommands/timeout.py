import discord
import datetime
from discord.ext import commands
from discord import app_commands
class TimeoutCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="timeout", description="Timeout a member.") # Timeout members
  @app_commands.describe(member="Select a specific member.")
  @app_commands.describe(time="Enter a time.")
  @app_commands.describe(reason="Enter a reason why they need to timeout.")
  async def timeout(self, interaction: discord.Interaction, member:discord.User, *, time: int, reason:str):
    ctx = interaction
    if ctx.guild:
      guild = ctx.guild
      # If the user don't have administrator permissions, they can't use the command
      if not ctx.user.guild_permissions.manage_messages:
        embed = discord.Embed(title="Timeout the member", description="You don't have permission to use this command.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
        return
      # If they try to timeout the bot, it will send this message
      if member == ctx.guild.me:
        embed = discord.Embed(title="Timeout the member", description="You can't use this command to timeout this bot that it is using this command.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
        return         
      # If they timeout themselves, it will timeout this message
      if member == ctx.user:
        embed = discord.Embed(title="Timeout the member", description="You can't timeout yourself.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
        return
      # This message will sent if the time is less than 60 seconds
      if time < 60:
        embed = discord.Embed(title="Timeout the member", description="The timeout must be more than 60 seconds.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
        return
      # Timeout the member
      try:
        await member.timeout(datetime.timedelta(seconds=time), reason=reason)
        # Send the message to the user
        message = f"You have been timed out from **{ctx.guild.name}** for **{time} seconds** because of **{reason}**."
        await member.send(message)
        embed = discord.Embed(title="Timeout the member", description=f"**{member}** is timed out for **{time} seconds** because of **{reason}**.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
      except discord.errors.HTTPException as e:
        await member.timeout(datetime.timedelta(seconds=time), reason=reason)
        embed = discord.Embed(title="Timeout the member", description=f"**{member}** is timed out for **{time} seconds** because of **{reason}**.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
    # If this command run in DM, it will not work
    else:
      embed = discord.Embed(title="Timeout the member", description="You can't use this command when you are in DM.", color=0x3f48cc)
      await interaction.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(TimeoutCommandSlash(bot))