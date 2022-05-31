import discord
from discord.ext import commands
intents=discord.Intents.default()
intents.members=True

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(981222516490117210)
    print("Someone Join")
    await channel.send(f'{member} join!')
    await channel.send(f'歡迎{member}的加入!')

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(981222638980583526)
    print("Someone Leave")
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'現在是{round(bot.latency*1000)} (ms)')
    if(round(bot.latency*1000)>300):
        await ctx.send(f'好...卡.好..卡')
    else:
        await ctx.send(f'順順Der')

@bot.command()
async def hi(ctx):
    await ctx.send(f'你好')

bot.run('OTgxMTk1OTcxNzA0ODExNTcw.GgVy4B.AeSb9lvl9LerpBes1Ne05H20XW2JMoRjg89HhQ')

