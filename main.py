# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='$', intents = discord.Intents.all())

@client.command()
async def foo(ctx, *, arg):
  await ctx.send(arg)

@client.command()
async def bulul(ctx):
  await ctx.message.channel.send('lul non lul ngon')

@client.command()
async def buscu(ctx):
  await ctx.message.channel.send('GAY')

@client.command()
async def minhdan(ctx):
  await ctx.message.channel.send('chào chú bé <@809060184722112552> đình')
# import discord
# from discord.ext import commands


# intents = discord.Intents.default()
# intents.message_content = True
# bot = commands.Bot(command_prefix='!', intents=intents)


# @bot.event
# async def on_ready():
#     print(f"Logged in as {bot.user}")

# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')

# @bot.command()
# async def hello(ctx):
#     await ctx.send("Choo choo! 🚅")


bot.run(os.environ["DISCORD_TOKEN"])
