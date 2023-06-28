import discord
from discord.ext import commands

class KickCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command() # Kick members
  async def kick(self, ctx, member: discord.Member = None, *, reason=None):
    async with ctx.typing():
      if ctx.guild:
        # If the user don't have administrator permissions, they can't use the command
        if not ctx.author.guild_permissions.kick_members:
          embed = discord.Embed(title="Kick the member", description="You don't have permission to use this command.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
        # If they kick themselves, it will send this message
        if member == ctx.message.author:
          embed = discord.Embed(title="Kick the member", description="You can't kick yourself.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
        # This message will sent if the `member` value is missing
        if member is None:
          embed = discord.Embed(title="Kick the member", description="Please enter a user and a reason.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
        # If they try to kick the bot, it will send this message
        if member == ctx.guild.me:
          embed = discord.Embed(title="Kick the member", description="You can't use this command to kick this bot that it is using this command.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author=False)
          return         
        # Check if the member is in the guild
        if member not in ctx.guild.members:
          embed = discord.Embed(title="Kick the member", description="The user you want to kick is not on this guild or not available.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return           
        # Check if the bot's role is lower than the member's role
        if ctx.guild.me.top_role < member.top_role:
          embed = discord.Embed(title="Kick the member", description="Can't use this command for the member has higher role than the bot role.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author=False)
          return            
        # This message will sent if the `reason` value is missing
        if reason is None:
          embed = discord.Embed(title="Kick the member", description="Please give a reason why they need to kick.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return          
        # Kick the member
        try:
          await ctx.guild.kick(member, reason=reason)
          # Send the message to the user
          message = f"You have been kicked from **{ctx.guild.name}** because of **{reason}**."
          await member.send(message)
          embed = discord.Embed(title="Kick the member", description=f"**{member}** is kicked because of **{reason}**.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
        except discord.errors.HTTPException as e:
          await ctx.guild.kick(member, reason=reason)
          embed = discord.Embed(title="Kick the member", description=f"**{member}** is kicked because of **{reason}**.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
        except discord.ext.commands.errors.MemberNotFound:
          embed = discord.Embed(title="Kick the member", description="The user you want to kick is not on this guild or not available.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)             
      # If this command run in DM, it will not work
      else:
        embed = discord.Embed(title="Kick the member", description="You can't use this command when you are in DM.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author = False)

def setup(bot):
  bot.add_cog(KickCommand(bot))