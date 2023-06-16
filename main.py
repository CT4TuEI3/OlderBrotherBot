
import discord
import json
from discord.ext import commands
intents = discord.Intents.all()



file = open('config.json', 'r')
config = json.load(file)

bot = commands.Bot(config['prefix'], intents=intents)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'{ctx.author.mention} pong!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        color = 0xffa3e0
    )
    embed.set_image(url='https://media.tenor.com/UKDNsxezWBMAAAAC/hello-brother.gif')
    await ctx.send(embed = embed)  

@bot.command(name='content')
async def content(ctx: commands.context, *, args):
    await ctx.message.delete()
    result = str(args)
    await ctx.send(embed=discord.Embed(description=result , color=0xffa3e0))

bot.run(config['token'])