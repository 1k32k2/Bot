import os
import discord
import music

from discord.ext import commands

cogs = [music]

client = commands.Bot(command_prefix='$', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

client = commands.Bot(command_prefix='$', intents = discord.Intents.all())

@client.event
async def on_ready():
  print(f"log in as {client.user}: {client.user.id}")

@client.command()
async def foo(ctx, *, arg):
  await ctx.send(arg)
  await ctx.message.delete()

@client.command()
async def bulul(ctx):
  await ctx.message.channel.send('https://media.discordapp.net/attachments/1118824169627467806/1119709118521938030/Them_bulul_qua.mp4')

@client.command()
async def buscu(ctx):
  await ctx.message.channel.send('GAY')

@client.command()
async def minhdan(ctx):
  await ctx.message.channel.send('chào chú bé <@809060184722112552> đình')

@client.command()
async def join(ctx):
  voice_bot = ctx.guild.voice_client
  channel = ctx.author.voice.channel
  
  if voice_bot:
    await voice_bot.move_to(channel)
  else: 
    await channel.connect()  

@client.command()
async def out(ctx):
  voice_bot = ctx.guild.voice_client
  await voice_bot.disconnect()

# @client.command()
# async def play(ctx, url):
  

client.run(os.environ["DISCORD_TOKEN"])
