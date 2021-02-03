import discord

import datetime

client = discord.Client()


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
