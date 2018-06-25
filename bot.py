import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import os

bot = commands.Bot(command_prefix=">")  

@bot.event
async def on_ready():
    print ("Ready")
    print (bot.user.name + " is online")
    print (bot.user.id)

@bot.command(pass_context=True)
async def Father(ctx):
   await bot.say('Praise be thy Noodle', tts=True)

@bot.command(pass_context=True)
async def Pray(ctx):
    voice = await bot.join_voice_channel(ctx.message.author.voice.voice_channel)
    player = voice.create_ffmpeg_player('ourpasta.mp3')
    player.start()

@bot.command(pass_context=True)
async def Kevin(ctx):
    voice = await bot.join_voice_channel(ctx.message.author.voice.voice_channel)
    player = voice.create_ffmpeg_player('kevin.mp3')
    player.start()

@bot.command(pass_context=True)
async def Dismissed(ctx):
    for x in bot.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()
bot.run(os.environ['bot_token'])
