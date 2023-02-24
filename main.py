
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
async def ping(ctx):
    await ctx.send(f'Здарова бандиты! https://cdn.discordapp.com/attachments/1008127694124355679/1078038224330567731/hello.webm')    
    
bot.run(config['token'])