import discord
from discord.ext import commands
from typing import Union
from discord import app_commands

class UserinfoCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="userinfo", description="View member's information.")
  @app_commands.describe(member="Select a specific user.")
  async def userinfo(self, interaction:discord.Interaction, member:discord.User = None):
      if not self.bot.command_states.get(str(interaction.guild.id), {}).get("userinfo", True):
        embed = discord.Embed(title="This command has been disabled on this server.", color=0x3f48cc)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return    
      ctx = interaction
      await interaction.response.defer(ephemeral = False)
      if isinstance(member, int):
        # Get userinfo from a user when they are not in the guild
        try:
          member = await self.bot.fetch_user(member)
        # It will show this message when the user ID is invaild
        except discord.errors.NotFound:
          embed = discord.Embed(title="User Information", description="Invalid user ID or username.", color=0x3f48cc)
          await interaction.followup.send(embed=embed)
          return
      # If the `member` value is empty, it will show their userinfo that they have sent
      elif member == None:
        member = ctx.user
      if isinstance(member, discord.Member):
        # Show the roles they have
        roles = [role for role in member.roles]
        roles.pop(0)
        roles.reverse()
        roles_str = " ".join([role.mention for role in roles])
        # Show the user information
        embed = discord.Embed(title=f"{member}",description=f"- 🆔｜User ID: {member.id}\n- 👤｜Discord Member since: {member.created_at.strftime('%a %d %B %Y, %I:%M %p')}\n- 👥｜Joined Server since: {member.joined_at.strftime('%a %d %B %Y, %I:%M %p')}\n- 🥇｜Roles: {roles_str}" , color=0x3f48cc)
        # If the profile picture is empty, it will show the Discord logo
        if member.display_avatar is not None:
          embed.set_thumbnail(url=member.display_avatar.url)
        else:
          embed.set_thumbnail(url=None)
      else:
        embed = discord.Embed(title=f"{member}", description=f"- 🆔｜User ID: {member.id}\n- 👤｜Discord Member since: {member.created_at.strftime('%a %d %B %Y, %I:%M %p')}", color=0x3f48cc)
        # If the profile picture is empty, it will show the Discord logo
        if member.display_avatar is not None:
          embed.set_thumbnail(url=member.display_avatar.url)
        else:
          embed.set_thumbnail(url=None)
      await interaction.followup.send(embed=embed)

def setup(bot):
  bot.add_cog(UserinfoCommandSlash(bot))