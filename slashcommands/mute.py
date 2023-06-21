import discord
from discord.ext import commands
from discord import app_commands
import asyncio

class MuteCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="mute", description="Mute a member.") # Kick members
  @app_commands.describe(member="Select a specific member.")
  @app_commands.describe(time="Enter a time.")
  async def mute(self, interaction: discord.Interaction, member: discord.Member, time: int):
    ctx = interaction
    if ctx.guild:
      # If the user don't have administrator permissions, they can't use the command
      if not ctx.user.guild_permissions.manage_roles:   
        embed = discord.Embed(title="Mute the member", description="You don't have permission to use this command.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
        return
      # If they mute themselves, it will send this message
      if member == ctx.user:
        embed = discord.Embed(title="Mute the member", description="You can't mute yourself.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
        return
      # This message will sent if the time is less than 60 seconds
      if time < 60:         
        embed = discord.Embed(title="Mute the member", description="The time of mute must be more than 60 seconds.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
        return        
      # If they try to mute the bot, it will send this message
      if member == ctx.guild.me:
        embed = discord.Embed(title="Mute the member", description="You can't use this command to mute this bot that it is using this command.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
        return           
      # Mute the member
      try:
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted by tkBOT')
        if not muted_role:
          muted_role = await ctx.guild.create_role(name='Muted by tkBOT')
          for channel in ctx.guild.channels:
            await channel.set_permissions(muted_role, send_messages=False)
        await member.add_roles(muted_role)
        # Send the message to the user
        message = f"You have been muted from **{ctx.guild.name}** for **{time} seconds**."
        await member.send(message)
        embed = discord.Embed(title="Mute the member", description=f"**{member}** is muted for **{time} seconds**.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
      except discord.errors.HTTPException as e:
        embed = discord.Embed(title="Mute the member", description=f"**{member}** is muted for **{time} seconds**.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
      if time:
        try:
          await asyncio.sleep(time)
          await member.remove_roles(muted_role)   
          message = f"You have been unmuted from **{ctx.guild.name}**."
          await member.send(message)       
        except discord.errors.HTTPException as e:
          await asyncio.sleep(time)
          await member.remove_roles(muted_role)             
    # If this command run in DM, it will not work
    else:
      embed = discord.Embed(title="Mute the member", description="You can't use this command when you are in DM.", color=0x3f48cc)
      await ctx.reply(embed=embed, mention_author = False)
        
def setup(bot):
  bot.add_cog(MuteCommandSlash(bot))