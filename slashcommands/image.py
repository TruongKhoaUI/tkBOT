import discord
import requests
import os
from discord.ext import commands
from io import BytesIO
from discord import app_commands
from PIL import Image

class ImageCommandSlash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="image", description="Generate a image.") # Search image on the internet
  @app_commands.describe(search="Enter a keyword.")
  async def image (self, interaction: discord.Interaction, *, search: str):
    await interaction.response.defer(ephemeral = False)
    # Request the image site
    response = requests.get (f"https://source.unsplash.com/featured/?{search}")
    image = Image.open (BytesIO (response.content))
    # Save the file with the number count
    if not os.path.exists("image/image1.jpg"):
      image.save ("image/image1.jpg")
      file = discord.File("image/image1.jpg", filename="image1.jpg")
      embed = discord.Embed(title=f"Image searched for: {search}", description="Generation successfully.", color=0x3f48cc)
      embed.set_footer(text="Generated by Unsplash")
      # Show the image
      embed.set_image(url="attachment://image1.jpg")
      await interaction.followup.send(file=file, embed=embed)
    # Save the file with the number count
    elif not os.path.exists("image/image2.jpg"):
      image.save ("image/image2.jpg")
      file = discord.File("image/image2.jpg", filename="image2.jpg")
      embed = discord.Embed(title=f"Image searched for: {search}", description="Generation successfully.", color=0x3f48cc)
      embed.set_footer(text="Generated by Unsplash")
      # Show the image
      embed.set_image(url="attachment://image2.jpg")
      await interaction.followup.send(file=file, embed=embed)
    # Add a number when the previous number exists of that file
    else:
      i = 1
      while os.path.exists(f"image/image{i}.jpg"):
        i += 1
      image.save (f"image/image{i}.jpg")
      file = discord.File(f"image/image{i}.jpg", filename=f"image{i}.jpg")
      embed = discord.Embed(title=f"Image searched for: {search}", description="Generation successfully.", color=0x3f48cc)
      embed.set_footer(text="Generated by Unsplash")
      # Show the image
      embed.set_image(url=f"attachment://image{i}.jpg")
      await interaction.followup.send(file=file, embed=embed)

def setup(bot):
  bot.add_cog(ImageCommandSlash(bot))