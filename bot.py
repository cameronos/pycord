import discord
from discord.ext import commands
from discord.utils import get

TOKEN = 'ENTER TOKEN HERE' #Token from Discord Developer Portal

client = discord.Client()
client = commands.Bot(command_prefix = '.') #Change prefix to your choice

@client.event
async def on_ready():
 print("Ready")

@client.command()
async def ping(ctx)
  await ctx.send("Pong!")
