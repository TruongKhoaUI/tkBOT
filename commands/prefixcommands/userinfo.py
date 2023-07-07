import discord
from discord.ext import commands
from typing import Union

class UserinfoCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="userinfo", description="View member's information.") # View user information
  async def userinfo(self, ctx, member: Union[discord.Member, discord.User, int] = None):
    async with ctx.typing():      
      # Get userinfo from a user when they are not in the guild
      try:
        if isinstance(member, int):
          member = await self.bot.fetch_user(member)
      # It will show this message when the user ID is invaild
      except discord.errors.NotFound:
        embed = discord.Embed(title="User Information", description="Invalid user ID or username.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author=False)
        return
      # If the `member` value is empty, it will show their userinfo that they have sent
      if member is None:
        member = ctx.author
      if isinstance(member, discord.Member):
        # Show the roles they have
        roles = [role for role in member.roles]
        roles.pop(0)
        roles.reverse()
        roles_str = " ".join([role.mention for role in roles])
        # Show the user information
        embed = discord.Embed(title=f"{member}", description=f"- 🆔｜User ID: {member.id}\n- 👤｜Discord Member since: {member.created_at.strftime('%a %d %B %Y, %I:%M %p')}", color=0x3f48cc)
        if ctx.guild and member.guild == ctx.guild:
          embed.description += f"\n- 👥｜Joined Server since: {member.joined_at.strftime('%a %d %B %Y, %I:%M %p')}\n- 🥇｜Roles: {roles_str}"
      else:
        embed = discord.Embed(title=f"{member}", description=f"- 🆔｜User ID: {member.id}\n- 👤｜Discord Member since: {member.created_at.strftime('%a %d %B %Y, %I:%M %p')}", color=0x3f48cc)
      if member.display_avatar is not None:
        embed.set_thumbnail(url=member.display_avatar.url)
      else:
        embed.set_thumbnail(url=None)
      await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
  bot.add_cog(UserinfoCommand(bot))