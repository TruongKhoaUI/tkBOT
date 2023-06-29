import discord
import json
from discord.ext import commands
from discord import app_commands

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

class WarnCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @app_commands.command(name="warn", description="Warn a member.")
  @app_commands.describe(member="Select a specific user")
  @app_commands.describe(reason="Enter a reason why they need to warn.")
  async def warn(self, interaction: discord.Interaction, member: discord.User, *, reason:str):
      ctx = interaction
      await interaction.response.defer(ephemeral = False)
      if ctx.guild:
        guild = ctx.guild
        warnings = load_warnings()
        # If the user don't have administrator permissions, they can't use the command
        if not ctx.user.guild_permissions.ban_members:
          embed = discord.Embed(title="Warn the member", description="You don't have permission to use this command.", color=0x3f48cc)
          await interaction.followup.send(embed=embed)
          return
        # If they warn themselves, it will send this message
        if member == ctx.user:
          embed = discord.Embed(title="Warn the member", description="You can't warn yourself.", color=0x3f48cc)
          await interaction.followup.send(embed=embed)
          return
        # If they try to warn the bot, it will send this message
        if member == ctx.guild.me:
          embed = discord.Embed(title="Warn the member", description="You can't use this command to warn this bot that it is using this command.", color=0x3f48cc)
          await interaction.followup.send(embed=embed)
          return         
        # Check if the bot's role is lower than the member's role
        if ctx.guild.me.top_role < member.top_role:
          embed = discord.Embed(title="Warn the member", description="Can't use this command for the member has higher role than the bot role.", color=0x3f48cc)
          await interaction.followup.send(embed=embed)
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
          await interaction.followup.send(embed=embed)
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
          await interaction.followup.send(embed=embed)
          if warnings[guild_id][str(member.id)] >= 5:
            await member.ban(reason="Reached 5 warns.")  
            del warnings[guild_id][str(member.id)]
            save_warnings(warnings)            
        except discord.errors.NotFound as e:
          embed = discord.Embed(title="Warn the member", description="The user you want to warn is not on this guild or not available.", color=0x3f48cc)
          await interaction.followup.send(embed=embed)
          return                
      # If this command run in DM, it will not work
      else:
        embed = discord.Embed(title="Warn the member", description="You can't use this command when you are in DM.", color=0x3f48cc)
        await interaction.followup.send(embed=embed)        

def setup(bot):
  bot.add_cog(WarnCommandSlash(bot))