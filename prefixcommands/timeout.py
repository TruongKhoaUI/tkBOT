import discord
import datetime
from discord.ext import commands

class TimeoutCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command() # Timeout members
  async def timeout(self, ctx, member: discord.Member = None, time: int = None, *, reason: str = None):
    async with ctx.typing():
      if ctx.guild:
        # If the user don't have administrator permissions, they can't use the command
        if not ctx.author.guild_permissions.manage_messages:
          embed = discord.Embed(title="Timeout the member", description="You don't have permission to use this command.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
        # If they timeout themselves, it will timeout this message
        if member == ctx.message.author:
          embed = discord.Embed(title="Timeout the member", description="You can't timeout yourself.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
        # This message will sent if the `member` value is missing
        if member is None:
          embed = discord.Embed(title="Timeout the member", description="Please enter a user, how much time they need to timeout and a reason.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
        # If they try to timeout the bot, it will send this message
        if member == ctx.guild.me:
          embed = discord.Embed(title="Timeout the member", description="You can't use this command to timeout this bot that it is using this command.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author=False)
          return       
        # Check if the member is in the guild
        if member not in ctx.guild.members:
          embed = discord.Embed(title="Timeout the member", description="The user you want to timeout is not on this guild or not available.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return 
        # Check if the bot's role is lower than the member's role
        if ctx.guild.me.top_role < member.top_role:
          embed = discord.Embed(title="Timeout the member", description="Can't use this command for the member has higher role than the bot role.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author=False)
          return          
        # This message will sent if the `time` value is missing
        if time is None:
          embed = discord.Embed(title="Timeout the member", description="Please enter how much time they need to timeout and a reason.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
        # This message will sent if the time is less than 60 seconds
        if time < 60:
          embed = discord.Embed(title="Timeout the member", description="The timeout must be more than 60 seconds.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
        # This message will sent if the `reason` value is missing
        if reason is None:
          embed = discord.Embed(title="Timeout the member", description="Please give a reason why they need to timeout.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
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
        await ctx.reply(embed=embed, mention_author = False)          
      # If this command run in DM, it will not work
      else:
        embed = discord.Embed(title="Timeout the member", description="You can't use this command when you are in DM.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author = False)
  @timeout.error # Error for the timeout for the `time` value
  async def timeout_error(self, ctx, error):
    async with ctx.typing():
      # If the `time` value is not a number, it will sent this message
      if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title="Timeout the member", description="Invalid time, or this is not a number.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
  bot.add_cog(TimeoutCommand(bot))