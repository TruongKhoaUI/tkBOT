import discord
import json
from discord.ext import commands

def load_warnings():
  try:
    with open("jsondata/warns.json", "r") as file:
      return json.load(file)
  except FileNotFoundError:
    return {}

# Function to save warnings to a JSON file
def save_warnings(warnings):
  with open("jsondata/warns.json", "w") as file:
    json.dump(warnings, file)

class WarnCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def warn(self, ctx, member: discord.Member = None, *, reason:str = None):
    async with ctx.typing():
      if ctx.guild:
        guild = ctx.guild
        warnings = load_warnings()
        # If the user don't have administrator permissions, they can't use the command
        if not ctx.author.guild_permissions.ban_members:
          embed = discord.Embed(title="Warn the member", description="You don't have permission to use this command.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
        # If they warn themselves, it will send this message
        if member == ctx.message.author:
          embed = discord.Embed(title="Warn the member", description="You can't warn yourself.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
        # This message will sent if the `member` value is missing
        if member is None:
          embed = discord.Embed(title="Warn the member", description="Please enter a user and a reason.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return
        # If they try to warn the bot, it will send this message
        if member == ctx.guild.me:
          embed = discord.Embed(title="Warn the member", description="You can't use this command to warn this bot that it is using this command.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author=False)
          return         
        # Check if the bot's role is lower than the member's role
        if ctx.guild.me.top_role < member.top_role:
          embed = discord.Embed(title="Warn the member", description="Can't use this command for the member has higher role than the bot role.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author=False)
          return            
        # This message will sent if the `reason` value is missing
        if reason is None:
          embed = discord.Embed(title="Warn the member", description="Please give a reason why they need to warn.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return                  
        guild_id = str(guild.id)
        if guild_id not in warnings:
          warnings[guild_id] = {}
        try:
          if str(member.id) not in warnings[guild_id]:
            warnings[guild_id][str(member.id)] = 1
          else:
            warnings[guild_id][str(member.id)] += 1
          # Save warnings
          save_warnings(warnings)
          message = f"You have been warned from **{ctx.guild.name}** because of **{reason}**. Warning count: **{warnings[guild_id][str(member.id)]}/5**"
          await member.send(content=message)
          embed = discord.Embed(title="Warn the member", description=f"**{member}** has been warned for **{reason}**. Warning count: **{warnings[guild_id][str(member.id)]}/5**", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          if warnings[guild_id][str(member.id)] >= 5:
            await member.ban(reason="Reached 5 warns.")
            del warnings[guild_id][str(member.id)]
            save_warnings(warnings)
        except discord.errors.HTTPException as e:
          if str(member.id) not in warnings[guild_id]:
            warnings[guild_id][str(member.id)] = 1
          else:
            warnings[guild_id][str(member.id)] += 0
          # Save warnings
          save_warnings(warnings)
          embed = discord.Embed(title="Warn the member", description=f"**{member}** has been warned for **{reason}**. Warning count: **{warnings[guild_id][str(member.id)]}/5**", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          if warnings[guild_id][str(member.id)] >= 5:
            await member.ban(reason="Reached 5 warns.")  
            del warnings[guild_id][str(member.id)]
            save_warnings(warnings)            
        except discord.errors.NotFound as e:
          embed = discord.Embed(title="Warn the member", description="The user you want to warn is not on this guild or not available.", color=0x3f48cc)
          await ctx.reply(embed=embed, mention_author = False)
          return                
      # If this command run in DM, it will not work
      else:
        embed = discord.Embed(title="Timeout the member", description="You can't use this command when you are in DM.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author = False)           

def setup(bot):
  bot.add_cog(WarnCommand(bot))