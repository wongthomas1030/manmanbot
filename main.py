import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(981222516490117210)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(981222638980583526)
    await channel.send(f'{member} join!')


bot.run('OTgxMTk1OTcxNzA0ODExNTcw.GgVy4B.AeSb9lvl9LerpBes1Ne05H20XW2JMoRjg89HhQ')

