import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def genpass(ctx, pass_length: int):
    from botlogic import gen_pass
    password = gen_pass(pass_length)
    await ctx.send(f"Generated password: {password}")

@bot.command()
async def animequote(ctx, anime: str):
    from botlogic import gen_anime_quote
    quote = gen_anime_quote(anime.upper())
    await ctx.send(quote)



bot.run("MTQ5OTk4MDY4OTM1NTk2NDU1Ng.GUQwN1.porGeFu2-qIJsZku_h8uP7kvWREDBA5GixeRDE")
