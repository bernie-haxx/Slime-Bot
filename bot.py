import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_NAME')


client = discord.Client()

@client.event
async def on_ready():
    """
    Discord.utils.find() is one utility that can improve the simplicity and readability of
    this code by replacing the for loop with a inituitive, abstracted function:
    
    Also known as a predicate.
    """
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} pulled the F up in to the following skreet:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'SKreet Members:\n - {members}')
client.run(TOKEN)
