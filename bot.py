import os

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

client.run(TOKEN)
