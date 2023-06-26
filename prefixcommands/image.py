import discord
import aiohttp
import os
from discord.ext import commands

class ImageCommand(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def image(self, ctx, *, search=None):
    async with ctx.typing():
      if search is None:
        embed = discord.Embed(title="Image Generator", description="**Please provide a keyword to generate the image you have provided!**", color=0x3f48cc)
        await ctx.reply(embed=embed, mention_author=False)
      else:
        async with aiohttp.ClientSession() as session:
          async with session.get(f"https://source.unsplash.com/featured/?{search}") as response:
            image_bytes = await response.read()
        # Save the file with the number count
        i = 1
        while os.path.exists(f"image/image{i}.jpg"):
          i += 1
        with open(f"image/image{i}.jpg", "wb") as f:
          f.write(image_bytes)
        file = discord.File(f"image/image{i}.jpg", filename=f"image{i}.jpg")
        embed = discord.Embed(title=f"Image searched for: {search}", description="Generation successful.", color=0x3f48cc)
        embed.set_footer(text="Generated by Unsplash")
        embed.set_image(url=f"attachment://image{i}.jpg")
        await ctx.reply(file=file, embed=embed, mention_author=False)

def setup(bot):
  bot.add_cog(ImageCommand(bot))