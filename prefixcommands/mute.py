import discord
from discord.ext import commands
import asyncio

class MuteCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command() # Kick members
  async def mute(self, ctx, member: discord.Member = None, time: int = None):
      if ctx.guild:
        # If the user don't have administrator permissions, they can't use the command
        if not ctx.author.guild_permissions.manage_roles:
          async with ctx.typing():    
            embed = discord.Embed(title="Mute the member", description="You don't have permission to use this command.", color=0x3f48cc)
            await ctx.reply(embed=embed, mention_author = False)
            return
        # If they mute themselves, it will send this message
        if member == ctx.message.author:
          async with ctx.typing():
            embed = discord.Embed(title="Mute the member", description="You can't mute yourself.", color=0x3f48cc)
            await ctx.reply(embed=embed, mention_author = False)
            return
        # This message will sent if the `member` value is missing
        if member is None:
          async with ctx.typing():
            embed = discord.Embed(title="Mute the member", description="Please enter a user, and how much time they need to mute.", color=0x3f48cc)
            await ctx.reply(embed=embed, mention_author = False)
            return
        # This message will sent if the `time` value is missing
        if time is None:
          async with ctx.typing():
            embed = discord.Embed(title="Mute the member", description="Please enter how much time they need to mute.", color=0x3f48cc)
            await ctx.reply(embed=embed, mention_author = False)
            return          
        # This message will sent if the time is less than 60 seconds
        if time < 60:
          async with ctx.typing():          
            embed = discord.Embed(title="Mute the member", description="The time of mute must be more than 60 seconds.", color=0x3f48cc)
            await ctx.reply(embed=embed, mention_author = False)
            return        
        # If they try to mute the bot, it will send this message
        if member == ctx.guild.me:
          async with ctx.typing():
            embed = discord.Embed(title="Mute the member", description="You can't use this command to mute this bot that it is using this command.", color=0x3f48cc)
            await ctx.reply(embed=embed, mention_author=False)
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
          async with ctx.typing():
            message = f"You have been muted from **{ctx.guild.name}** for **{time} seconds**."
            await member.send(message)
            embed = discord.Embed(title="Mute the member", description=f"**{member}** is muted for **{time} seconds**.", color=0x3f48cc)
            await ctx.reply(embed=embed, mention_author = False)
        except discord.errors.HTTPException as e:
          async with ctx.typing():
            await ctx.guild.kick(member)
            embed = discord.Embed(title="Mute the member", description=f"**{member}** is muted for **{time} seconds**.", color=0x3f48cc)
            await ctx.reply(embed=embed, mention_author = False)
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
  bot.add_cog(MuteCommand(bot))