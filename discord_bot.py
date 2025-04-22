import os
import discord
from discord.ext import commands

# Ustawienie intencji
intents = discord.Intents.default()
intents.message_content = True

# Inicjalizacja bota z prefiksem '!'
bot = commands.Bot(command_prefix='!', intents=intents)


# Wydarzenie: Bot gotowy
@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')


# Komenda: !hello
@bot.command()
async def hello(ctx):
    await ctx.send('Cześć! Jestem prostym botem Discord!')


# Uruchomienie bota z tokenem
bot.run(os.getenv("api_key"))
