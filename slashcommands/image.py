import discord
import aiohttp
import os
from discord.ext import commands
from discord import app_commands

class ImageCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="image", description="Generate a image.") # Search image on the internet
  @app_commands.describe(search="Enter a keyword.")
  async def image (self, interaction: discord.Interaction, *, search: str):
    await interaction.response.defer(ephemeral=False)
    async with aiohttp.ClientSession() as session:
      async with session.get(f"https://source.unsplash.com/featured/?{search}") as response:
        image_bytes = await response.read()
    # Save the file with the number count
    i = 1
    while os.path.exists(f"/home/runner/image/image{i}.jpg"):
      i += 1
    with open(f"/home/runner/image/image{i}.jpg", "wb") as f:
      f.write(image_bytes)
    file = discord.File(f"/home/runner/image/image{i}.jpg", filename=f"image{i}.jpg")
    embed = discord.Embed(title=f"Image searched for: {search}", description="Generation successful.", color=0x3f48cc)
    embed.set_footer(text="Generated by Unsplash")
    embed.set_image(url=f"attachment://image{i}.jpg")
    await interaction.followup.send(file=file, embed=embed)

def setup(bot):
  bot.add_cog(ImageCommandSlash(bot))