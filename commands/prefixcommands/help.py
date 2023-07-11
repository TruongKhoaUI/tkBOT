import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="help", description="Help with commands") # Help with commands
  async def help(self, ctx):
    async with ctx.typing():
      if ctx.guild:
        if ctx.author.guild_permissions.administrator:
          # Select menu
          options = [
              discord.SelectOption(label="ban", description="Help with `ban` command", emoji="🔨"),
              discord.SelectOption(label="botinfo", description="Help with `botinfo` command", emoji="🤖"),
              discord.SelectOption(label="commands", description="Help with `commands` command", emoji="📃"),
              discord.SelectOption(label="commandsstates", description="Help with `commandsstates` command", emoji="📃"),
              discord.SelectOption(label="echo", description="Help with `echo` command", emoji="📝"),
              discord.SelectOption(label="help", description="Help with `help` command", emoji="❓"),
              discord.SelectOption(label="image", description="Help with `image` command", emoji="🖼️"),
              discord.SelectOption(label="kick", description="Help with `kick` command", emoji="👟"),
              discord.SelectOption(label="pfp", description="Help with `pfp` command", emoji="🖼️"),
              discord.SelectOption(label="ping", description="Help with `ping` command", emoji="🏓"),
              discord.SelectOption(label="poll", description="Help with `poll` command", emoji="⁉️"),
              discord.SelectOption(label="rank", description="Help with `rank` command", emoji="🥇"),            
              discord.SelectOption(label="rankreset", description="Help with `rankreset` command", emoji="🥇"),              
              discord.SelectOption(label="serverinfo", description="Help with `serverinfo` command", emoji="🏠"),
              discord.SelectOption(label="timeout", description="Help with `timeout` command", emoji="⌚"),
              discord.SelectOption(label="userinfo", description="Help with `userinfo` command", emoji="👤"),
              discord.SelectOption(label="warn", description="Help with `warn` command", emoji="⚠️"),
              discord.SelectOption(label="wikidiscovery", description="Help with `wikidiscovery` command", emoji="🌎")
          ]
          select = discord.ui.Select(placeholder='Select a command to get help', options=options)
          view = discord.ui.View()
          view.add_item(select)    
          async def callback(interaction):
            if interaction.user != ctx.author:
              embed = discord.Embed(title="This select option is not yours", color=0x3f48cc)
              await interaction.response.send_message(embed=embed, ephemeral=True)
              return            
            if interaction.data["values"][0] == "ban":
              embed = discord.Embed(title="Help with `ban` command", description="**This command will ban the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!ban [user] [reason]` `/ban [user] [reason]` to ban someone.", inline=False)
            elif interaction.data["values"][0] == "botinfo":
              embed = discord.Embed(title="Help with `botinfo` command", description="**This command will show the information about this bot such as CPU, RAM, and disk usage.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!botinfo` or `/botinfo` to let it show the bot status.", inline=False)
            elif interaction.data["values"][0] == "commands":
              embed = discord.Embed(title="Help with `commands` command", description="**This command will enable/disable the bot commands on the specific guild.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!commands [command]` or `/commands [command]` to enable/disable a command from this bot on the specific guild.", inline=False)
            elif interaction.data["values"][0] == "commandsstates":
              embed = discord.Embed(title="Help with `commandsstates` command", description="**This command will show all commands has been enabled/disabled on the specific guild.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!commandsstates` or `/commandsstates` to show all commands has been enabled/disabled on the specific guild.", inline=False)              
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
            elif interaction.data["values"][0] == "pfp":
              embed = discord.Embed(title="Help with `pfp` command", description="**This command will show the members image profile.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!pfp` or `/pfp` to show your profile picture. If you want to see profile picture from another member, use `tk!pfp @user` or `/pfp @user`.", inline=False)
            elif interaction.data["values"][0] == "ping":
              embed = discord.Embed(title="Help with `ping` command", description="**This command will show the time the bot responds in Discord lantency time.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!ping` or `/ping` to show the time the bot responds.", inline=False)
            elif interaction.data["values"][0] == "poll":
              embed = discord.Embed(title="Help with `poll` command", description="**This command create and send your question to your members.**", color=0x348cc)    
              embed.add_field(name="How to use it", value="Type `tk!poll [question] | [answer1] | [answer2]` or `/poll [question] [answer1] [answer2]` to create and send your question. Remember in the prefix, you have to insert `|` if you want to insert the next answer or the question you have added.", inline=False)   
            elif interaction.data["values"][0] == "rank":
              embed = discord.Embed(title="Help with `rank` command", description="**This command will show the leaderboard with top 10 users.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!rank` `/rank` to show the leaderboard. If you want to switch to another page, type `tk!rank [page]` or `/rank [page]`, for example, the number 2 will switch to the second page. Chatting every 10 seconds you will get 3 points.", inline=False)              
            elif interaction.data["values"][0] == "rankreset":
              embed = discord.Embed(title="Help with `rankreset` command", description="**This command will remove all of the points for all members in the specific guild.**", color=0x348cc)              
              embed.add_field(name="How to use it", value="Type `tk!rankreset` or `/rankreset` to remove all of the points for all members in the specific guild. If you want to reset points for specific member you have choosed, type `tk!rankreset [member]` or `/rankreset [member]`", inline=False)             
            elif interaction.data["values"][0] == "serverinfo":
              embed = discord.Embed(title="Help with `serverinfo` command", description="**This command will show the information about the current server you're in.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!serverinfo` or `/serverinfo` to show the information about the current server you're in.", inline=False)
            elif interaction.data["values"][0] == "timeout":
              embed = discord.Embed(title="Help with `timeout` command", description="**This command will timeout the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!timeout [user] [time] [reason]` or `/timeout [user] [time] [reason]` to timeout someone. The minimum of time for the timeout is more than 60 seconds.", inline=False)             
            elif interaction.data["values"][0] == "userinfo":
              embed = discord.Embed(title="Help with `userinfo` command", description="**This command will show the information about members include date joined Discord, date joined the server and also user ID.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!userinfo` or `/userinfo` to show the information about you. If you want to see user information from another members, type `tk!userinfo @user` or `/userinfo @user`.", inline=False)
            elif interaction.data["values"][0] == "warn":
              embed = discord.Embed(title="Help with `warn` command", description="**This command will warn the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!warn [user] [reason]` `/warn [user] [reason]` to warn someone. They will be banned if they reached 5 warns and the warning count will be removed from the bot data.", inline=False)                
            elif interaction.data["values"][0] == "wikidiscovery":
              embed = discord.Embed(title="Help with `wikidiscovery` command", description="**This command will search the information you provived in Wikipedia.**", color=0x3f48cc)
              embed.add_field(name="How to use it", value="Type `tk!wikidiscovery [search]` or `/wikidiscovery [search]` to search the information you provived.", inline=False)
            await interaction.response.edit_message(content="", embed=embed, view=None)         
          select.callback = callback
          embed = discord.Embed(title="tkBOT's Help", description="Welcome! Choose one of these options to get started with the specific commands.", color=0x3f48cc)
          await ctx.reply(embed=embed, view=view, mention_author = False)

        else:
          options = [
              discord.SelectOption(label="botinfo", description="Help with `botinfo` command", emoji="🤖"),
              discord.SelectOption(label="commandsstates", description="Help with `commandsstates` command", emoji="📃"),
              discord.SelectOption(label="echo", description="Help with `echo` command", emoji="📝"),
              discord.SelectOption(label="help", description="Help with `help` command", emoji="❓"),
              discord.SelectOption(label="image", description="Help with `image` command", emoji="🖼️"),
              discord.SelectOption(label="pfp", description="Help with `pfp` command", emoji="🖼️"),
              discord.SelectOption(label="ping", description="Help with `ping` command", emoji="🏓"),
              discord.SelectOption(label="poll", description="Help with `poll` command", emoji="⁉️"),
              discord.SelectOption(label="rank", description="Help with `rank` command", emoji="🥇"),            
              discord.SelectOption(label="serverinfo", description="Help with `serverinfo` command", emoji="🏠"),
              discord.SelectOption(label="userinfo", description="Help with `userinfo` command", emoji="👤"),
              discord.SelectOption(label="wikidiscovery", description="Help with `wikidiscovery` command", emoji="🌎")
          ]
          select = discord.ui.Select(placeholder='Select a command to get help', options=options)
          view = discord.ui.View()
          view.add_item(select)    
          async def callback(interaction):
            if interaction.user != ctx.author:
              embed = discord.Embed(title="This select option is not yours", color=0x3f48cc)
              await interaction.response.send_message(embed=embed, ephemeral=True)
              return             
            if interaction.data["values"][0] == "botinfo":
              embed = discord.Embed(title="Help with `botinfo` command", description="**This command will show the information about this bot such as CPU, RAM, and disk usage.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!botinfo` or `/botinfo` to let it show the bot status.", inline=False)
            elif interaction.data["values"][0] == "commandsstates":
              embed = discord.Embed(title="Help with `commandsstates` command", description="**This command will show all commands has been enabled/disabled on the specific guild.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!commandsstates` or `/commandsstates` to show all commands has been enabled/disabled on the specific guild.", inline=False)              
            elif interaction.data["values"][0] == "echo":
              embed = discord.Embed(title="Help with `echo` command", description="**This command will replace your messages from the bot.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!echo [message]` or `/echo [message]`to let the bot sent the message.", inline=False)
            elif interaction.data["values"][0] == "help":
              embed = discord.Embed(title="Help with `help` command", description="**This command will help you for every commands from this bot.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!help` or `/help` to show all commands to help.", inline=False)
            elif interaction.data["values"][0] == "image":
              embed = discord.Embed(title="Help with `image` command", description="**This command will generate a image from the internet.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!image [image]` or `/image [image]` to generate a image from the internet", inline=False)          
            elif interaction.data["values"][0] == "pfp":
              embed = discord.Embed(title="Help with `pfp` command", description="**This command will show the members image profile.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!pfp` or `/pfp` to show your profile picture. If you want to see profile picture from another member, use `tk!pfp @user` or `/pfp @user`.", inline=False)
            elif interaction.data["values"][0] == "ping":
              embed = discord.Embed(title="Help with `ping` command", description="**This command will show the time the bot responds in Discord lantency time.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!ping` or `/ping` to show the time the bot responds.", inline=False)
            elif interaction.data["values"][0] == "poll":
              embed = discord.Embed(title="Help with `poll` command", description="**This command create and send your question to your members.**", color=0x348cc)    
              embed.add_field(name="How to use it", value="Type `tk!poll [question] | [answer1] | [answer2]` or `/poll [question] [answer1] [answer2]` to create and send your question. Remember in the prefix, you have to insert `|` if you want to insert the next answer or the question you have added.", inline=False) 
            elif interaction.data["values"][0] == "rank":
              embed = discord.Embed(title="Help with `rank` command", description="**This command will show the leaderboard with top 10 users.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!rank` `/rank` to show the leaderboard. If you want to switch to another page, type `tk!rank [page]` or `/rank [page]`, for example, the number 2 will switch to the second page. Chatting every 10 seconds you will get 3 points.", inline=False)                           
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
          embed = discord.Embed(title="tkBOT's Help", description="Welcome! Choose one of these options to get started with the specific commands.", color=0x3f48cc)
          await ctx.reply(embed=embed, view=view, mention_author = False)
      else:
          # Select menu
          options = [
              discord.SelectOption(label="ban", description="Help with `ban` command", emoji="🔨"),
              discord.SelectOption(label="botinfo", description="Help with `botinfo` command", emoji="🤖"),
              discord.SelectOption(label="commands", description="Help with `commands` command", emoji="📃"),
              discord.SelectOption(label="commandsstates", description="Help with `commandsstates` command", emoji="📃"),
              discord.SelectOption(label="echo", description="Help with `echo` command", emoji="📝"),
              discord.SelectOption(label="help", description="Help with `help` command", emoji="❓"),
              discord.SelectOption(label="image", description="Help with `image` command", emoji="🖼️"),
              discord.SelectOption(label="kick", description="Help with `kick` command", emoji="👟"),
              discord.SelectOption(label="pfp", description="Help with `pfp` command", emoji="🖼️"),
              discord.SelectOption(label="ping", description="Help with `ping` command", emoji="🏓"),
              discord.SelectOption(label="poll", description="Help with `poll` command", emoji="⁉️"),
              discord.SelectOption(label="rank", description="Help with `rank` command", emoji="🥇"),            
              discord.SelectOption(label="rankreset", description="Help with `rankreset` command", emoji="🥇"),              
              discord.SelectOption(label="serverinfo", description="Help with `serverinfo` command", emoji="🏠"),
              discord.SelectOption(label="timeout", description="Help with `timeout` command", emoji="⌚"),
              discord.SelectOption(label="userinfo", description="Help with `userinfo` command", emoji="👤"),
              discord.SelectOption(label="warn", description="Help with `warn` command", emoji="⚠️"),
              discord.SelectOption(label="wikidiscovery", description="Help with `wikidiscovery` command", emoji="🌎")
          ]
          select = discord.ui.Select(placeholder='Select a command to get help', options=options)
          view = discord.ui.View()
          view.add_item(select)    
          async def callback(interaction):
            if interaction.user != ctx.author:
              embed = discord.Embed(title="This select option is not yours", color=0x3f48cc)
              await interaction.response.send_message(embed=embed, ephemeral=True)
              return             
            if interaction.data["values"][0] == "ban":
              embed = discord.Embed(title="Help with `ban` command", description="**This command will ban the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!ban [user] [reason]` `/ban [user] [reason]` to ban someone.", inline=False)
            elif interaction.data["values"][0] == "botinfo":
              embed = discord.Embed(title="Help with `botinfo` command", description="**This command will show the information about this bot such as CPU, RAM, and disk usage.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!botinfo` or `/botinfo` to let it show the bot status.", inline=False)
            elif interaction.data["values"][0] == "commands":
              embed = discord.Embed(title="Help with `commands` command", description="**This command will enable/disable the bot commands on the specific guild.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!commands [command]` or `/commands [command]` to enable/disable a command from this bot on the specific guild.", inline=False)
            elif interaction.data["values"][0] == "commandsstates":
              embed = discord.Embed(title="Help with `commandsstates` command", description="**This command will show all commands has been enabled/disabled on the specific guild.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!commandsstates` or `/commandsstates` to show all commands has been enabled/disabled on the specific guild.", inline=False)              
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
            elif interaction.data["values"][0] == "pfp":
              embed = discord.Embed(title="Help with `pfp` command", description="**This command will show the members image profile.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!pfp` or `/pfp` to show your profile picture. If you want to see profile picture from another member, use `tk!pfp @user` or `/pfp @user`.", inline=False)
            elif interaction.data["values"][0] == "ping":
              embed = discord.Embed(title="Help with `ping` command", description="**This command will show the time the bot responds in Discord lantency time.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!ping` or `/ping` to show the time the bot responds.", inline=False)
            elif interaction.data["values"][0] == "poll":
              embed = discord.Embed(title="Help with `poll` command", description="**This command create and send your question to your members.**", color=0x348cc)    
              embed.add_field(name="How to use it", value="Type `tk!poll [question] | [answer1] | [answer2]` or `/poll [question] [answer1] [answer2]` to create and send your question. Remember in the prefix, you have to insert `|` if you want to insert the next answer or the question you have added.", inline=False)   
            elif interaction.data["values"][0] == "rank":
              embed = discord.Embed(title="Help with `rank` command", description="**This command will show the leaderboard with top 10 users.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!rank` `/rank` to show the leaderboard. If you want to switch to another page, type `tk!rank [page]` or `/rank [page]`, for example, the number 2 will switch to the second page. Chatting every 10 seconds you will get 3 points.", inline=False)              
            elif interaction.data["values"][0] == "rankreset":
              embed = discord.Embed(title="Help with `rankreset` command", description="**This command will remove all of the points for all members in the specific guild.**", color=0x348cc)              
              embed.add_field(name="How to use it", value="Type `tk!rankreset` or `/rankreset` to remove all of the points for all members in the specific guild. If you want to reset points for specific member you have choosed, type `tk!rankreset [member]` or `/rankreset [member]`", inline=False)             
            elif interaction.data["values"][0] == "serverinfo":
              embed = discord.Embed(title="Help with `serverinfo` command", description="**This command will show the information about the current server you're in.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!serverinfo` or `/serverinfo` to show the information about the current server you're in.", inline=False)
            elif interaction.data["values"][0] == "timeout":
              embed = discord.Embed(title="Help with `timeout` command", description="**This command will timeout the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!timeout [user] [time] [reason]` or `/timeout [user] [time] [reason]` to timeout someone. The minimum of time for the timeout is more than 60 seconds.", inline=False)             
            elif interaction.data["values"][0] == "userinfo":
              embed = discord.Embed(title="Help with `userinfo` command", description="**This command will show the information about members include date joined Discord, date joined the server and also user ID.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!userinfo` or `/userinfo` to show the information about you. If you want to see user information from another members, type `tk!userinfo @user` or `/userinfo @user`.", inline=False)
            elif interaction.data["values"][0] == "warn":
              embed = discord.Embed(title="Help with `warn` command", description="**This command will warn the specific member on the specific server.**", color=0x348cc)
              embed.add_field(name="How to use it", value="Type `tk!warn [user] [reason]` `/warn [user] [reason]` to warn someone. They will be banned if they reached 5 warns and the warning count will be removed from the bot data.", inline=False)                
            elif interaction.data["values"][0] == "wikidiscovery":
              embed = discord.Embed(title="Help with `wikidiscovery` command", description="**This command will search the information you provived in Wikipedia.**", color=0x3f48cc)
              embed.add_field(name="How to use it", value="Type `tk!wikidiscovery [search]` or `/wikidiscovery [search]` to search the information you provived.", inline=False)
            await interaction.response.edit_message(content="", embed=embed, view=None)

          select.callback = callback
          embed = discord.Embed(title="tkBOT's Help", description="Welcome! Choose one of these options to get started with the specific commands.", color=0x3f48cc)
          await ctx.reply(embed=embed, view=view, mention_author = False)

def setup(bot):
  bot.add_cog(HelpCommand(bot))