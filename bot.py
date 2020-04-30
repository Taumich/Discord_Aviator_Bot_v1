import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    # print(f'a message was received {message}')

    if message.author == client.user:  # cancels if about to respond to itself!
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')


client.run('NzA1MzEyMjIzODI4MTE1NDU3.Xqp5vA.i2Luaw_5PlHV8L-75ogUv2U4faw')
