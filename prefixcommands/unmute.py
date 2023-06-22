import discord
from discord.ext import commands

class UnmuteCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command() # Kick members
  async def unmute(self, ctx, member: discord.Member = None):
    async with ctx.typing():
      if ctx.guild:
        # If the user don't have administrator permissions, they can't use the command
        if not ctx.author.guild_permissions.manage_roles:   
          embed = discord.Embed(title="Unmute the member", description="You don't have permission to use this command.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
        # If they unmute themselves, it will send this message
        if member is None:
          embed = discord.Embed(title="Unmute the member", description="Please enter a user to unmute.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return        
        # If they unmute themselves, it will send this message
        if member == ctx.message.author:
          embed = discord.Embed(title="Unmute the member", description="You can't unmute yourself.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return    
        # If they try to kick the bot, it will send this message
        if member == ctx.guild.me:
          embed = discord.Embed(title="Unmute the member", description="You can't use this command to unmute this bot that it is using this command.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return    
        # Check if the member is in the guild
        if member not in ctx.guild.members:
          embed = discord.Embed(title="Unmute the member", description="The user you want to unmute is not on this guild or not available.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return           
        # Unmute the member
        try:
          muted_role = discord.utils.get(ctx.guild.roles, name='Muted by tkBOT')
          if muted_role and muted_role in member.roles:
            await member.remove_roles(muted_role)
            message = f"You have been unmuted in **{ctx.guild.name}**."
            await member.send(message)
            embed = discord.Embed(title="Unmute the member", description=f"**{member}** has been unmuted.", color=0x3f48cc)
            await ctx.reply(embed=embed, mention_author = False)
          else:
            embed = discord.Embed(title="Unmute the member", description=f"**{member}** doesn't have to unmute.", color=0x3f48cc)
            await ctx.reply(embed=embed, mention_author = False)
        except discord.errors.HTTPException as e:
          embed = discord.Embed(title="Unmute the member", description=f"**{member}** has been unmuted.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
      # If this command run in DM, it will not work
      else:
        embed = discord.Embed(title="Unmute the member", description="You can't use this command when you are in DM.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author = False)
        
def setup(bot):
  bot.add_cog(UnmuteCommand(bot))