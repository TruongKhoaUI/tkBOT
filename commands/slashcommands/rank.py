import discord
import json
import os
from discord.ext import commands
from datetime import datetime, timedelta
from discord import app_commands
from math import ceil

cooldown = timedelta(seconds=10)
last_message = {} 

class RankCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_ready(self):
    with open(os.getenv('leaderboard_directory'), 'r') as f:
      points = json.load(f)
    for guild in self.bot.guilds:
      if str(guild.id) not in points:
        points[str(guild.id)] = {}
      for member in guild.members:
        if str(member.id) not in points[str(guild.id)]:
          points[str(guild.id)][str(member.id)] = 0
    with open(os.getenv('leaderboard_directory'), 'w') as f:
      json.dump(points, f)

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.guild is None:  # Check if the message is in a DM
      return
    if message.webhook_id is not None:  # Exclude webhooks
      return      
    now = datetime.utcnow()
    if message.author.id in last_message and now - last_message[message.author.id] < cooldown:
      return
    last_message[message.author.id] = now
    # Check if the message author is the bot
    if message.author == self.bot.user:
      return
    with open(os.getenv('leaderboard_directory'), 'r') as f:
      points = json.load(f)
    guild_id = str(message.guild.id)
    if guild_id not in points:
      points[guild_id] = {}
    author_id = str(message.author.id)
    # Check if the author is the bot
    if author_id == str(self.bot.user.id):
      return
    if author_id not in points[guild_id]:
      points[guild_id][author_id] = 0
    points[guild_id][author_id] += 0
    with open(os.getenv('leaderboard_directory'), 'w') as f:
      json.dump(points, f)
        
  @app_commands.command(name="rank", description="View the leaderboard")
  @app_commands.describe(page="View the next top 10 page.")
  async def rank(self, interaction: discord.Interaction, page: int = 1):
    if interaction.guild is not None and not self.bot.command_states.get(str(interaction.guild.id), {}).get("rank", True):
      embed = discord.Embed(title="This command has been disabled on this server.", color=0x3f48cc)
      await interaction.response.send_message(embed=embed, ephemeral=True)
      return
    ctx = interaction
    await interaction.response.defer(ephemeral = False)
    if ctx.guild:
      with open(os.getenv('leaderboard_directory'), 'r') as f:
        points = json.load(f)
      server_points = points.get(str(ctx.guild.id), {})
      sorted_points = sorted(server_points.items(), key=lambda x: x[1], reverse=True)
      per_page = 10
      start_index = (page - 1) * per_page
      end_index = start_index + per_page
      page_points = sorted_points[start_index:end_index]
      userpoints = points.get(str(ctx.guild.id), {}).get(str(ctx.user.id), 0)
      userrank_list = [i for i, x in enumerate(sorted_points) if x[0] == str(ctx.user.id)]
      if userrank_list:
        userrank = userrank_list[0] + 1
      else:
        userrank = None
      last_page = ceil(len(sorted_points) / per_page)
      embed = discord.Embed(title=f'Leaderboard｜Page {page} out of {last_page}', description=f"- 🥇｜Your current points: {userpoints}\n- 🫂｜Your current rank: {userrank}", color=0x3f48cc)      
      if page_points:
        rank_counter = start_index + 1
        for i, user in enumerate(page_points):
          user_id = int(user[0])
          member = ctx.guild.get_member(user_id)
          if not member:
            try:
              member = await self.bot.fetch_user(user_id)
            except discord.errors.NotFound:
              del points[str(ctx.guild.id)][str(user_id)]
              with open(os.getenv('leaderboard_directory'), 'w') as f:
                json.dump(points, f)
              continue
          if not member.bot:
            embed.add_field(name=f"{rank_counter}. {member}", value=f"{user[1]} points\n", inline=False)
            rank_counter += 1
          else:
            del points[str(ctx.guild.id)][str(user_id)]
            with open(os.getenv('leaderboard_directory'), 'w') as f:
              json.dump(points, f)            
      else:
        last_page = ceil(len(sorted_points) / per_page)
        embed.description = f'No more users to show.\nThe last page of the leaderboard is {last_page}.'
      await interaction.followup.send(embed=embed)
    else:
      embed = discord.Embed(title="Leaderboard", description="You can't view the leaderboard when you're in DM.", color=0x3f48cc)
      await interaction.followup.send(embed=embed)

def setup(bot):
  bot.add_cog(RankCommandSlash(bot))