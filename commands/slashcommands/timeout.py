import discord
import datetime
import asyncio
from discord.ext import commands
from discord import app_commands

class TimeoutCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="timeout", description="Timeout a member.") # Timeout members
  @app_commands.default_permissions(manage_messages=True)
  @app_commands.describe(member="Select a specific member.")
  @app_commands.describe(time="Enter a time.")
  @app_commands.describe(reason="Enter a reason why they need to timeout.")
  async def timeout(self, interaction: discord.Interaction, member:discord.User, *, time: int, reason:str):
    if interaction.guild is not None and not self.bot.command_states.get(str(interaction.guild.id), {}).get("timeout", True):
      embed = discord.Embed(title="This command has been disabled on this server.", color=0x3f48cc)
      await interaction.response.send_message(embed=embed, ephemeral=True)
      return 
    ctx = interaction
    await interaction.response.defer(ephemeral = False)
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
        await interaction.followup.send(embed=embed)
        return         
      # If they timeout themselves, it will timeout this message
      if member == ctx.user:
        embed = discord.Embed(title="Timeout the member", description="You can't timeout yourself.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
        return
      # This message will sent if the time is less than 60 seconds
      if time < 60:
        embed = discord.Embed(title="Timeout the member", description="The timeout must be more than 60 seconds.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
        return
      # Check if the member is in the guild
      if member not in ctx.guild.members:
        embed = discord.Embed(title="Timeout the member", description="The user you want to timeout is not on this guild or not available.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
        return        
      # Check if the bot's role is lower than the member's role
      if ctx.guild.me.top_role < member.top_role:
        embed = discord.Embed(title="Timeout the member", description="Can't use this command for the member has higher role than the bot role.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author=False)
        return          
      # Timeout the member
      try:
        # Send the message to the user
        message = f"You have been timed out from **{ctx.guild.name}** for **{time} seconds** because of **{reason}**."
        await member.send(message)
      except discord.Forbidden:
        pass
      await member.timeout(datetime.timedelta(seconds=time), reason=reason)
      embed = discord.Embed(title="Timeout the member", description=f"**{member}** is timed out for **{time} seconds** because of **{reason}**.", color=0x3f48cc)
      await interaction.followup.send(embed=embed)          
    # If this command run in DM, it will not work
    else:
      embed = discord.Embed(title="Timeout the member", description="You can't use this command when you are in DM.", color=0x3f48cc)
      await interaction.followup.send(embed=embed)

def setup(bot):
  bot.add_cog(TimeoutCommandSlash(bot))