# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='$', intents = discord.Intents.all())

@client.event
async def on_ready():
  print(f"log in as {client.user}")

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

@client.command()
async def join(ctx):
  channel = ctx.author.voice.channel
  await channel.connect()  

@client.command()
async def out(ctx):
  voice_client = ctx.guild.voice_client
  await voice_client.disconnect()
  

client.run(os.environ["DISCORD_TOKEN"])
