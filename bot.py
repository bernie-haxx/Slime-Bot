import os
import random
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


# Bot activated event
@bot.event
async def on_ready():
    print(f'{bot.user.name} has pulled the F up!')

# Member Client Side
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"It's Lit!! :cactus: \n {member.name} pulled up wit the cactus juice! \nFirst of, Listen to Scotty and roll one",
    )

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise discord.DiscordException

# 69 command area
@bot.command(name='69')
async def six_nine(ctx):
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
        'Heheaaa Boi!',
    ]

    response = random.choice(quotes)
    await ctx.send(response)

# Roll dice command 
@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

# Hi command
@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == 'hi':
        await message.channel.send(
            f'Waspoppin? "_Tengu\'s pimple_"\n Brand new whip just hopped in!'
        )


# Create channel command
@bot.command(name="create-channel")
@commands.has_role('JACKBOYS')
async def create_channel(ctx, channel_name: str):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the slyat for this command')

bot.run(TOKEN)