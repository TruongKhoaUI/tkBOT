import discord
import json
from discord import User, NotFound
from discord.ext import commands
from datetime import datetime, timedelta
from math import ceil

cooldown = timedelta(seconds=8)
last_message = {} 

class LeaderboardCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    with open('level.json', 'r') as f:
      points = json.load(f)
    for guild in self.bot.guilds:
      if str(guild.id) not in points:
        points[str(guild.id)] = {}
      for member in guild.members:
        if str(member.id) not in points[str(guild.id)]:
          points[str(guild.id)][str(member.id)] = 0
    with open('level.json', 'w') as f:
      json.dump(points, f)

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.guild is None:  # Check if the message is in a DM
      return
    now = datetime.utcnow()
    if message.author.id in last_message and now - last_message[message.author.id] < cooldown:
      return
    last_message[message.author.id] = now
    with open('level.json', 'r') as f:
      points = json.load(f)
    guild_id = str(message.guild.id)
    if guild_id not in points:
      points[guild_id] = {}
    author_id = str(message.author.id)
    if author_id not in points[guild_id]:
      points[guild_id][author_id] = 0
    points[guild_id][author_id] += 3
    with open('level.json', 'w') as f:
      json.dump(points, f) 
  
  @commands.command()
  async def leaderboard(self, ctx, page: int = 1):
    async with ctx.typing():
      if ctx.guild:
        with open('level.json', 'r') as f:
          points = json.load(f)
        server_points = points.get(str(ctx.guild.id), {})
        sorted_points = sorted(server_points.items(), key=lambda x: x[1], reverse=True)
        per_page = 10
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        page_points = sorted_points[start_index:end_index]
        userpoints = points.get(str(ctx.guild.id), {}).get(str(ctx.author.id), 0)
        userrank_list = [i for i, x in enumerate(sorted_points) if x[0] == str(ctx.author.id)]
        if userrank_list:
          userrank = userrank_list[0] + 1
        else:
          userrank = None
        embed = discord.Embed(title=f'Leaderboard｜Page {page}', description=f"- 🥇｜Your current points: {userpoints}\n- 🫂｜Your current rank: {userrank}", color=0x3f48cc)    
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
                with open('level.json', 'w') as f:
                  json.dump(points, f)
                continue
            if not member.bot:
              embed.add_field(name=f"{rank_counter}. {member}", value=f"{user[1]} points\n", inline=False)
              rank_counter += 1
        else:
          last_page = ceil(len(sorted_points) / per_page)
          embed.description = f'No more users to show.\nThe last page of the leaderboard is {last_page}.'
      else:
        embed = discord.Embed(title="Leaderboard", description="You can't view the leaderboard when you're in DM.", color=0x3f48cc)
      await ctx.reply(embed=embed, mention_author=False)
  @leaderboard.error # Error for the timeout for the `time` value
  async def leaderboard_error(self, ctx, error):
    async with ctx.typing():
      # If the `time` value is not a number, it will sent this message
      if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title="Leaderboard", description="Invalid number, or this is not a number.", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
  bot.add_cog(LeaderboardCommand(bot))