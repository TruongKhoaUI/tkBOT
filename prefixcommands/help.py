import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command() # Help with commands
  async def help(self, ctx):
    async with ctx.typing():
      if ctx.guild:
        if ctx.author.guild_permissions.administrator:
          # Select menu
          options = [
              discord.SelectOption(label="ban", description="Help with `ban` command", emoji="🔨"),
              discord.SelectOption(label="botinfo", description="Help with `botinfo` command", emoji="🤖"),
              discord.SelectOption(label="echo", description="Help with `echo` command", emoji="📝"),
              discord.SelectOption(label="help", description="Help with `help` command", emoji="❓"),
              discord.SelectOption(label="image", description="Help with `image` command", emoji="🖼️"),
              discord.SelectOption(label="kick", description="Help with `kick` command", emoji="👟"),
              discord.SelectOption(label="leaderboard", description="Help with `leaderboard` command", emoji="🥇"),
              discord.SelectOption(label="mute", description="Help with `mute` command", emoji="🔈"),                
              discord.SelectOption(label="pfp", description="Help with `pfp` command", emoji="🖼️"),
              discord.SelectOption(label="ping", description="Help with `ping` command", emoji="🏓"),
              discord.SelectOption(label="resetpoints", description="Help with `resetpoints` command", emoji="🥇"),
              discord.SelectOption(label="serverinfo", description="Help with `serverinfo` command", emoji="🏠"),
              discord.SelectOption(label="timeout", description="Help with `timeout` command", emoji="⌚"),
              discord.SelectOption(label="unmute", description="Help with `unmute` command", emoji="🔈"),      
              discord.SelectOption(label="userinfo", description="Help with `userinfo` command", emoji="👤"),
              discord.SelectOption(label="wikidiscovery", description="Help with `wikidiscovery` command", emoji="🌎")
          ]
          select = discord.ui.Select(placeholder='Select a command to get help', options=options)
          view = discord.ui.View()
          view.add_item(select)    
          async def callback(interaction):
            if interaction.data["values"][0] == "ban":
              embed = discord.Embed(title="Help with `ban` command", description="**This command will ban the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!ban [user] [reason]` `/ban [user] [reason]` to ban someone.", inline=False)              
            elif interaction.data["values"][0] == "botinfo":
              embed = discord.Embed(title="Help with `botinfo` command", description="**This command will show the information about this bot such as CPU, RAM, and disk usage.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!botinfo` or `/botinfo` to let it show the bot status.", inline=False)
            elif interaction.data["values"][0] == "echo":
              embed = discord.Embed(title="Help with `echo` command", description="**This command will replace your messages from the bot.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!echo [message]` or `/echo [message]`to let the bot sent the message.", inline=False)
            elif interaction.data["values"][0] == "help":
              embed = discord.Embed(title="Help with `help` command", description="**This command will help you for every commands from this bot.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!help` or `/help` to show all commands to help.", inline=False)
            elif interaction.data["values"][0] == "image":
              embed = discord.Embed(title="Help with `image` command", description="**This command will generate a image from the internet.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!image [image]` or `/image [image]` to generate a image from the internet", inline=False)
            elif interaction.data["values"][0] == "kick":
              embed = discord.Embed(title="Help with `kick` command", description="**This command will kick the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!kick [user] [reason]` or `/kick [user] [reason]` or to kick someone.", inline=False)
            elif interaction.data["values"][0] == "leaderboard":
              embed = discord.Embed(title="Help with `leaderboard` command", description="**This command will show the leaderboard with top 10 users.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!leaderboard` `/leaderboard` to show the leaderboard. If you want to switch to another page, type `tk!leaderboard [page]` or `/leaderboard [page]`, for example, the number 2 will switch to the second page. Chatting every 10 seconds you will get 3 points.", inline=False)
            elif interaction.data["values"][0] == "mute":
              embed = discord.Embed(title="Help with `mute` command", description="**This command will mute the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!mute [user] [time]` or `/mute [user] [time]` to mute someone. The minimum of time for the time is more than 60 seconds.", inline=False)
            elif interaction.data["values"][0] == "pfp":
              embed = discord.Embed(title="Help with `pfp` command", description="**This command will show the members image profile.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!image` or `/image` to show your profile picture. If you want to see profile picture from another member, use `tk!pfp @user` or `/pfp @user`.", inline=False)
            elif interaction.data["values"][0] == "ping":
              embed = discord.Embed(title="Help with `ping` command", description="**This command will show the time the bot responds in Discord lantency time.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!ping` or `/ping` to show the time the bot responds.", inline=False)
            elif interaction.data["values"][0] == "resetpoints":
              embed = discord.Embed(title="Help with `resetpoints` command", description="**This command will remove all of the points for all members in the specific guild.**", color=0x348cc)              
              embed.add_field(name="How to use it", value="Type `tk!resetpoints` or `/resetpoints` to remove all of the points for all members in the specific guild.", inline=False)              
            elif interaction.data["values"][0] == "serverinfo":
              embed = discord.Embed(title="Help with `serverinfo` command", description="**This command will show the information about the current server you're in.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!serverinfo` or `/serverinfo` to show the information about the current server you're in.", inline=False)
            elif interaction.data["values"][0] == "timeout":
              embed = discord.Embed(title="Help with `timeout` command", description="**This command will timeout the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!timeout [user] [time] [reason]` or `/timeout [user] [time] [reason]` to timeout someone. The minimum of time for the timeout is more than 60 seconds.", inline=False)
            elif interaction.data["values"][0] == "unmute":
              embed = discord.Embed(title="Help with `unmute` command", description="**This command will unmute the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!unmute [user]` or `/unmute [user]` to unmute someone.", inline=False)              
            elif interaction.data["values"][0] == "userinfo":
              embed = discord.Embed(title="Help with `userinfo` command", description="**This command will show the information about members include date joined Discord, date joined the server and also user ID.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!userinfo` or `/userinfo` to show the information about you. If you want to see user information from another members, type `tk!userinfo @user` or `/userinfo @user`.", inline=False)
            elif interaction.data["values"][0] == "wikidiscovery":
              embed = discord.Embed(title="Help with `wikidiscovery` command", description="**This command will search the information you provived in Wikipedia.**", color=0x3f48cc)
              embed.add_field(name="How to use it", value="Type `tk!wikidiscovery [search]` or `/wikidiscovery [search]` to search the information you provived.", inline=False)                
            await interaction.response.edit_message(content="", embed=embed, view=None)          
          select.callback = callback
          embed = discord.Embed(title="tkBOT's Help", description="Select one of these commands to get help.", color=0x3f48cc)
          await ctx.reply(embed=embed, view=view, mention_author = False)

        else:
          options = [
              discord.SelectOption(label="botinfo", description="Help with `botinfo` command", emoji="🤖"),
              discord.SelectOption(label="echo", description="Help with `echo` command", emoji="📝"),
              discord.SelectOption(label="help", description="Help with `help` command", emoji="❓"),
              discord.SelectOption(label="image", description="Help with `image` command", emoji="🖼️"),
              discord.SelectOption(label="leaderboard", description="Help with `leaderboard` command", emoji="🥇"),            
              discord.SelectOption(label="pfp", description="Help with `pfp` command", emoji="🖼️"),
              discord.SelectOption(label="ping", description="Help with `ping` command", emoji="🏓"),
              discord.SelectOption(label="serverinfo", description="Help with `serverinfo` command", emoji="🏠"),
              discord.SelectOption(label="userinfo", description="Help with `userinfo` command", emoji="👤"),
              discord.SelectOption(label="wikidiscovery", description="Help with `wikidiscovery` command", emoji="🌎")
          ]
          select = discord.ui.Select(placeholder='Select a command to get help', options=options)
          view = discord.ui.View()
          view.add_item(select)    
          async def callback(interaction):
            if interaction.data["values"][0] == "botinfo":
              embed = discord.Embed(title="Help with `botinfo` command", description="**This command will show the information about this bot such as CPU, RAM, and disk usage.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!botinfo` or `/botinfo` to let it show the bot status.", inline=False)
            elif interaction.data["values"][0] == "echo":
              embed = discord.Embed(title="Help with `echo` command", description="**This command will replace your messages from the bot.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!echo [message]` or `/echo [message]`to let the bot sent the message.", inline=False)
            elif interaction.data["values"][0] == "help":
              embed = discord.Embed(title="Help with `help` command", description="**This command will help you for every commands from this bot.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!help` or `/help` to show all commands to help.", inline=False)
            elif interaction.data["values"][0] == "image":
              embed = discord.Embed(title="Help with `image` command", description="**This command will generate a image from the internet.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!image [image]` or `/image [image]` to generate a image from the internet", inline=False)
            elif interaction.data["values"][0] == "leaderboard":
              embed = discord.Embed(title="Help with `leaderboard` command", description="**This command will show the leaderboard with top 10 users.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!leaderboard` `/leaderboard` to show the leaderboard. If you want to switch to another page, type `tk!leaderboard [page]` or `/leaderboard [page]`, for example, the number 2 will switch to the second page. Chatting every 10 seconds you will get 3 points.", inline=False)          
            elif interaction.data["values"][0] == "pfp":
              embed = discord.Embed(title="Help with `pfp` command", description="**This command will show the members image profile.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!image` or `/image` to show your profile picture. If you want to see profile picture from another member, use `tk!pfp @user` or `/pfp @user`.", inline=False)
            elif interaction.data["values"][0] == "ping":
              embed = discord.Embed(title="Help with `ping` command", description="**This command will show the time the bot responds in Discord lantency time.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!ping` or `/ping` to show the time the bot responds.", inline=False)
            elif interaction.data["values"][0] == "serverinfo":
              embed = discord.Embed(title="Help with `serverinfo` command", description="**This command will show the information about the current server you're in.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!serverinfo` or `/serverinfo` to show the information about the current server you're in.", inline=False)
            elif interaction.data["values"][0] == "userinfo":
              embed = discord.Embed(title="Help with `userinfo` command", description="**This command will show the information about members include date joined Discord, date joined the server and also user ID.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!userinfo` or `/userinfo` to show the information about you. If you want to see user information from another members, type `tk!userinfo @user` or `/userinfo @user`.", inline=False)
            elif interaction.data["values"][0] == "wikidiscovery":
              embed = discord.Embed(title="Help with `wikidiscovery` command", description="**This command will search the information you provived in Wikipedia.**", color=0x3f48cc)
              embed.add_field(name="How to use it", value="Type `tk!wikidiscovery [search]` or `/wikidiscovery [search]` to search the information you provived.", inline=False)
            await interaction.response.edit_message(content="", embed=embed, view=None)
          select.callback = callback
          embed = discord.Embed(title="tkBOT's Help", description="Select one of these commands to get help.", color=0x3f48cc)
          await ctx.reply(embed=embed, view=view, mention_author = False)
      else:
          # Select menu
          options = [
              discord.SelectOption(label="ban", description="Help with `ban` command", emoji="🔨"),
              discord.SelectOption(label="botinfo", description="Help with `botinfo` command", emoji="🤖"),
              discord.SelectOption(label="echo", description="Help with `echo` command", emoji="📝"),
              discord.SelectOption(label="help", description="Help with `help` command", emoji="❓"),
              discord.SelectOption(label="image", description="Help with `image` command", emoji="🖼️"),
              discord.SelectOption(label="kick", description="Help with `kick` command", emoji="👟"),
              discord.SelectOption(label="leaderboard", description="Help with `leaderboard` command", emoji="🥇"),        
              discord.SelectOption(label="mute", description="Help with `mute` command", emoji="🔈"),      
              discord.SelectOption(label="pfp", description="Help with `pfp` command", emoji="🖼️"),
              discord.SelectOption(label="ping", description="Help with `ping` command", emoji="🏓"),
              discord.SelectOption(label="resetpoints", description="Help with `resetpoints` command", emoji="🥇"),              
              discord.SelectOption(label="serverinfo", description="Help with `serverinfo` command", emoji="🏠"),
              discord.SelectOption(label="timeout", description="Help with `timeout` command", emoji="⌚"),
              discord.SelectOption(label="unmute", description="Help with `unmute` command", emoji="🔈"),      
              discord.SelectOption(label="userinfo", description="Help with `userinfo` command", emoji="👤"),
              discord.SelectOption(label="wikidiscovery", description="Help with `wikidiscovery` command", emoji="🌎")
          ]
          select = discord.ui.Select(placeholder='Select a command to get help', options=options)
          view = discord.ui.View()
          view.add_item(select)    
          async def callback(interaction):
            if interaction.data["values"][0] == "ban":
              embed = discord.Embed(title="Help with `ban` command", description="**This command will ban the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!ban [user] [reason]` `/ban [user] [reason]` to ban someone.", inline=False)
            elif interaction.data["values"][0] == "botinfo":
              embed = discord.Embed(title="Help with `botinfo` command", description="**This command will show the information about this bot such as CPU, RAM, and disk usage.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!botinfo` or `/botinfo` to let it show the bot status.", inline=False)
            elif interaction.data["values"][0] == "echo":
              embed = discord.Embed(title="Help with `echo` command", description="**This command will replace your messages from the bot.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!echo [message]` or `/echo [message]`to let the bot sent the message.", inline=False)
            elif interaction.data["values"][0] == "help":
              embed = discord.Embed(title="Help with `help` command", description="**This command will help you for every commands from this bot.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!help` or `/help` to show all commands to help.", inline=False)
            elif interaction.data["values"][0] == "image":
              embed = discord.Embed(title="Help with `image` command", description="**This command will generate a image from the internet.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!image [image]` or `/image [image]` to generate a image from the internet", inline=False)
            elif interaction.data["values"][0] == "kick":
              embed = discord.Embed(title="Help with `kick` command", description="**This command will kick the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!kick [user] [reason]` or `/kick [user] [reason]` or to kick someone.", inline=False)
            elif interaction.data["values"][0] == "leaderboard":
              embed = discord.Embed(title="Help with `leaderboard` command", description="**This command will show the leaderboard with top 10 users.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!leaderboard` `/leaderboard` to show the leaderboard. If you want to switch to another page, type `tk!leaderboard [page]` or `/leaderboard [page]`, for example, the number 2 will switch to the second page. Chatting every 10 seconds you will get 3 points.", inline=False)              
            elif interaction.data["values"][0] == "mute":
              embed = discord.Embed(title="Help with `mute` command", description="**This command will mute the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!mute [user] [time]` or `/mute [user] [time]` to mute someone. The minimum of time for the time is more than 60 seconds.", inline=False)
            elif interaction.data["values"][0] == "pfp":
              embed = discord.Embed(title="Help with `pfp` command", description="**This command will show the members image profile.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!image` or `/image` to show your profile picture. If you want to see profile picture from another member, use `tk!pfp @user` or `/pfp @user`.", inline=False)
            elif interaction.data["values"][0] == "ping":
              embed = discord.Embed(title="Help with `ping` command", description="**This command will show the time the bot responds in Discord lantency time.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!ping` or `/ping` to show the time the bot responds.", inline=False)
            elif interaction.data["values"][0] == "resetpoints":
              embed = discord.Embed(title="Help with `resetpoints` command", description="**This command will remove all of the points for all members in the specific guild.**", color=0x348cc)              
              embed.add_field(name="How to use it", value="Type `tk!resetpoints` or `/resetpoints` to remove all of the points for all members in the specific guild.", inline=False)                   
            elif interaction.data["values"][0] == "serverinfo":
              embed = discord.Embed(title="Help with `serverinfo` command", description="**This command will show the information about the current server you're in.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!serverinfo` or `/serverinfo` to show the information about the current server you're in.", inline=False)
            elif interaction.data["values"][0] == "timeout":
              embed = discord.Embed(title="Help with `timeout` command", description="**This command will timeout the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!timeout [user] [time] [reason]` or `/timeout [user] [time] [reason]` to timeout someone. The minimum of time for the timeout is more than 60 seconds.", inline=False)
            elif interaction.data["values"][0] == "unmute":
              embed = discord.Embed(title="Help with `unmute` command", description="**This command will unmute the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!unmute [user]` or `/unmute [user]` to unmute someone.", inline=False)              
            elif interaction.data["values"][0] == "userinfo":
              embed = discord.Embed(title="Help with `userinfo` command", description="**This command will show the information about members include date joined Discord, date joined the server and also user ID.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!userinfo` or `/userinfo` to show the information about you. If you want to see user information from another members, type `tk!userinfo @user` or `/userinfo @user`.", inline=False)
            elif interaction.data["values"][0] == "wikidiscovery":
              embed = discord.Embed(title="Help with `wikidiscovery` command", description="**This command will search the information you provived in Wikipedia.**", color=0x3f48cc)
              embed.add_field(name="How to use it", value="Type `tk!wikidiscovery [search]` or `/wikidiscovery [search]` to search the information you provived.", inline=False)
            await interaction.response.edit_message(content="", embed=embed, view=None)
          select.callback = callback
          embed = discord.Embed(title="tkBOT's Help", description="Select one of these commands to get help.", color=0x3f48cc)
          await ctx.reply(embed=embed, view=view, mention_author = False)

def setup(bot):
  bot.add_cog(HelpCommand(bot))