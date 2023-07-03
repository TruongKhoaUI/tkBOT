import discord
from discord.ext import commands
from discord import app_commands

class KickCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="kick", description="Kick a user.") # Kick members
  @app_commands.default_permissions(kick_members=True)
  @app_commands.describe(member="Select a specific member.")
  @app_commands.describe(reason="Enter a reason why they need to kick.")
  async def kick(self, interaction: discord.Interaction, member:discord.User, reason:str):
    ctx = interaction
    await interaction.response.defer(ephemeral = False)
    if ctx.guild:
      guild = ctx.guild
      # If the user don't have administrator permissions, they can't use the command
      if not interaction.user.guild_permissions.kick_members:
        embed = discord.Embed(title="Kick the member", description="You don't have permission to use this command.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
        return
      # If they try to kick the bot, it will send this message
      if member == ctx.guild.me:
        embed = discord.Embed(title="Kick the member", description="You can't use this command to kick this bot that it is using this command.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
        return         
      # If they kick themselves, it will timeout this message
      if member == ctx.user:
        embed = discord.Embed(title="Kick the member", description="You can't kick yourself.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
        return
      # Check if the member is in the guild
      if member not in ctx.guild.members:
        embed = discord.Embed(title="Kick the member", description="The user you want to kick is not on this guild or not available.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
        return        
      # Check if the bot's role is lower than the member's role
      if ctx.guild.me.top_role < member.top_role:
        embed = discord.Embed(title="Kick the member", description="Can't use this command for the member has higher role than the bot role.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author=False)
        return          
      # Kick the member
      try:
        # Send the message to the user
        message = f"You have been kicked from **{ctx.guild.name}** because of **{reason}**."
        await member.send(message)
      except discord.Forbidden:
        pass
      await ctx.guild.kick(member, reason=reason)
      embed = discord.Embed(title="Kick the member", description=f"**{member}** is kicked because of **{reason}**.", color=0x3f48cc)
      await interaction.followup.send(embed=embed)
    else:
      embed = discord.Embed(title="Kick the member", description="You can't use this command when you are in DM.", color=0x3f48cc)
      await interaction.followup.send(embed=embed)

def setup(bot):
  bot.add_cog(KickCommandSlash(bot))