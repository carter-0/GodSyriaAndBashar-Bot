from discord.utils import get
import discord
import os

client = discord.Client()

def repeat(voice, audio, channel):
	if channel and not voice.is_playing():
		audio = discord.FFmpegPCMAudio('gsb.mp3')
		voice.play(audio, after=lambda e: repeat(voice, audio, channel))
		voice.is_playing()

@client.event
async def on_message(message):
	if ";;gsb" in message.content:
		channel = message.author.voice.channel
		voice = get(client.voice_clients, guild=message.channel.guild)

		if voice and voice.is_connected():
			await voice.move_to(channel)
		else:
			voice = await channel.connect()

		if channel and not voice.is_playing():
			audio = discord.FFmpegPCMAudio('gsb.mp3')
			voice.play(audio, after=lambda e: repeat(voice, audio, channel))
			voice.is_playing()

client.run(os.environ['token'])