import discord
import youtube_dl

from discord.ext import commands

class music(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def play(self, ctx, url):
    ctx.voice_client.stop()
    FFMPRG_OPTIONS = {'before_option': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'option': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download = False)
      url2 = info['format'][0]['url']  
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPRG_OPTIONS)
      vc.play(source)

  @commands.command()
  async def pause(self, ctx):
    await ctx.voice_client.pause()
    await ctx.send("paused")

  @commands.command()
  async def resume(self, ctx):
    await ctx.voice_client.resume()
    await ctx.send("resumed")

def setup(client):
  client.add_cog(music(client))