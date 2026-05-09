import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")

    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")

    elif message.content.startswith('$broadcast'):
        for channel in message.guild.text_channels:
            try:
                await channel.send("sigma")
                await asyncio.sleep(1)  # delay biar aman
            except:
                pass

client.run("YOUR_TOKEN")
