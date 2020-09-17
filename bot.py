import os, random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has pulled the F up!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"It's Lit!!, {member.name} pulled up wit the cactus juice!"
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'Bruh',
        'I tink am bout to steeeaaaal!',
        'OKEH',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        '*top* Noice!',
        "Heheaaa Boi!"
    ]
    if message.content == '69':
         response = random.choice(quotes)
         await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise dicord.DiscordException

client.run(TOKEN)
