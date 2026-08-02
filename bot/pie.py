import discord

import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('{} logged in as {}'.format(datetime.datetime.today(), client.user), flush=True)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "pie" in message.content:
        await message.channel.send('oooh, i love pie')


with open('/secrets/discord_client_secret', 'r') as f:
    client.run(f.read())
