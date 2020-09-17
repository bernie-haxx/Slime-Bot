import os, random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"It's Lit!!, {member.name} pulled up wit the cactus juice!",
        f"First of, Listen to Scotty and be chill Fahm",
    )

client.run(TOKEN)
