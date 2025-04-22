import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import aiohttp
from yt_dlp import YoutubeDL
from dotenv import load_dotenv
import os


load_dotenv()
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

# Komenda: !clear (czyszczenie wiadomości)
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    if amount < 1 or amount > 100:
        await ctx.send("Podaj liczbę od 1 do 100!", delete_after=5)
        return
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'Usunięto {amount} wiadomości!', delete_after=5)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Nie masz uprawnień do zarządzania wiadomościami!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Podaj liczbę wiadomości do usunięcia, np. `!clear 10`")

# Komenda: !meme (losowy mem)
@bot.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://meme-api.com/gimme') as resp:
            if resp.status != 200:
                await ctx.send("Nie udało się pobrać mema. Spróbuj później!")
                return
            data = await resp.json()
            await ctx.send(data['url'])

# Komenda: !play (odtwarzanie muzyki)
@bot.command()
async def play(ctx, url):
    if not ctx.author.voice:
        await ctx.send("Dołącz do kanału głosowego!")
        return
    channel = ctx.author.voice.channel
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    
    if not voice_client:
        voice_client = await channel.connect()
    
    try:
        with YoutubeDL({'format': 'bestaudio', 'noplaylist': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info['url']
            voice_client.play(FFmpegPCMAudio(audio_url, executable='ffmpeg'))
            await ctx.send(f'Odtwarzam: {info["title"]}')
    except Exception as e:
        await ctx.send(f"Wystąpił błąd: {str(e)}")

# Komenda: !leave (opuszczenie kanału głosowego)
@bot.command()
async def leave(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client:
        await voice_client.disconnect()
        await ctx.send("Opuściłem kanał głosowy!")
    else:
        await ctx.send("Nie jestem na żadnym kanale głosowym!")

# Uruchomienie bota z tokenem
bot.run(os.getenv('api_key'))