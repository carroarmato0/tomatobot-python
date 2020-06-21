import asyncio
import discord
import configparser
from pathlib import Path
import os.path
from os import path
import os


class TomatoBot(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # Log messages sent to us
        print('Message from {0.author.name}: {0.content}'.format(message))

        # Answer to pings
        if message.content == 'ping':
            await message.channel.send('pong')

        # Say hi
        if message.content.lower().startswith(('hello', 'hi')):
            await message.channel.send('Hello {0}!'.format(message.author.mention))

        # Summoning spell for voice
        if self.user in message.mentions and "summon" in message.content:
            if message.guild.voice_client is not None:
                await message.guild.voice_client.disconnect()

            author = message.author
            channel = author.voice.channel
            await channel.connect()

        # Leave spell for voice
        if self.user in message.mentions and "leave" in message.content:
            # Get the Guild from which the message was sent
            guild_vc = message.guild.voice_client
            await guild_vc.disconnect()

        # Play miep merp sound
        if message.content == "miep merp":
            # Check if the Voice Client exists
            if message.guild.voice_client is not None:
                audio = discord.FFmpegPCMAudio(Path(__file__).parent / './resources/soundboard/games/meepmerp.wav')
                player = message.guild.voice_client.play(audio)
                player.start()
                while not player.is_done():
                    await asyncio.sleep(1)
                player.stop()
            else:
                print("Doesn't look like I'm connected")

        # Play Tetten sound
        if 'tetten' in message.content.lower():
            # Check if the Voice Client exists
            if message.guild.voice_client is not None:
                audio = discord.FFmpegPCMAudio(Path(__file__).parent / './resources/soundboard/willies_en_marietten/tetten_wat_is_da.mp3')
                player = message.guild.voice_client.play(audio)
                player.start()
                while not player.is_done():
                    await asyncio.sleep(1)
                player.stop()
            else:
                print("Doesn't look like I'm connected")

Bot_Token=None

if path.exists('config.ini'):
    # Load Config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    Bot_Token=str(config['BOT']['Token'])
else:
    Bot_Token=os.getenv('BOT_TOKEN')
# Create Bot
bot = TomatoBot()
bot.run(Bot_Token)
