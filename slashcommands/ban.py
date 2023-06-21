import discord
from discord.ext import commands
from discord import app_commands

class BanCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="ban", description="Ban a user.") # Ban members
  @app_commands.describe(member="Select a specific member.")
  @app_commands.describe(reason="Enter a reason why they need to ban.")
  async def ban(self, interaction: discord.Interaction, member: discord.User, reason: str):
    ctx = interaction
    if ctx.guild:
      guild = ctx.guild
      # If the user don't have administrator permissions, they can't use the command
      if not interaction.user.guild_permissions.ban_members:
        embed = discord.Embed(title="Ban the member", description="You don't have permission to use this command.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
        return
      # If they try to ban the bot, it will send this message
      if member == ctx.guild.me:
        embed = discord.Embed(title="Ban the member", description="You can't use this command to ban this bot that it is using this command.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
        return         
      # If they ban themselves, it will timeout this message
      if member == ctx.user:
        embed = discord.Embed(title="Ban the member", description="You can't ban yourself.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
        return
      # Ban the member  
      try:
        await ctx.guild.ban(member, reason=reason)
        # Send the message to the user
        message = f"You have been banned from **{ctx.guild.name}** because of **{reason}**."
        await member.send(message)
        embed = discord.Embed(title="Ban the member", description=f"**{member}** is banned because of **{reason}**.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
      except discord.errors.HTTPException as e:
        await ctx.guild.ban(member, reason=reason)
        embed = discord.Embed(title="Ban the member", description=f"**{member}** is banned because of **{reason}**.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed)
    # If this command run in DM, it will not work
    else:
      embed = discord.Embed(title="Ban the member", description="You can't use this command when you are in DM.", color=0x3f48cc)
      await interaction.response.send_message(embed=embed)

def setup(bot):
  bot.add_cog(BanCommandSlash(bot))