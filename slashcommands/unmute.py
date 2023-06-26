import discord
from discord.ext import commands
from discord import app_commands

class UnmuteCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="unmute", description="Mute a member.") # Kick members
  @app_commands.describe(member="Select a specific member.")
  async def mute(self, interaction: discord.Interaction, member: discord.Member):
    ctx = interaction
    await interaction.response.defer(ephemeral = False)
    if ctx.guild:
      # If the user don't have administrator permissions, they can't use the command
      if not ctx.user.guild_permissions.manage_roles:   
        embed = discord.Embed(title="Unmute the member", description="You don't have permission to use this command.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
        return
      # If they unmute themselves, it will send this message
      if member == ctx.user:
        embed = discord.Embed(title="Unmute the member", description="You can't unmute yourself.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
        return    
      # If they try to unmute the bot, it will send this message
      if member == ctx.guild.me:
        embed = discord.Embed(title="Unmute the member", description="You can't use this command to unmute this bot that it is using this command.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
        return
      # Check if the member is in the guild
      if member not in ctx.guild.members:
        embed = discord.Embed(title="Unmute the member", description="The user you want to unmute is not on this guild or not available.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
        return         
      # Unmute the member
      try:
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted by tkBOT')
        if muted_role and muted_role in member.roles:
          await member.remove_roles(muted_role)
          message = f"You have been unmuted in **{ctx.guild.name}**."
          await member.send(message)
          embed = discord.Embed(title="Unmute the member", description=f"**{member}** has been unmuted.", color=0x3f48cc)
          await interaction.followup.send(embed=embed)
        else:
          embed = discord.Embed(title="Unmute the member", description=f"**{member}** doesn't have to unmute.", color=0x3f48cc)
          await interaction.followup.send(embed=embed)
      except discord.errors.HTTPException as e:
        embed = discord.Embed(title="Unmute the member", description=f"**{member}** has been unmuted.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)
    # If this command run in DM, it will not work
    else:
      embed = discord.Embed(title="Unmute the member", description="You can't use this command when you are in DM.", color=0x3f48cc)
      await interaction.followup.send(embed=embed)
        
def setup(bot):
  bot.add_cog(UnmuteCommandSlash(bot))