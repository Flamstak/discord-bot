import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import random

# Ładowanie zmiennych środowiskowych
load_dotenv()

# Odczyt prefiksu z .env (domyślnie '!')
PREFIX = os.getenv("BOT_PREFIX", "!")

# Ustawienie intencji
intents = discord.Intents.default()
intents.message_content = True

# Inicjalizacja bota z dynamicznym prefiksem
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Skrócony link do serwera
INVITE_LINK = "discord.gg/wsGBbhC"

# Lista zapraszających statusów
status_list = [
    discord.Activity(type=discord.ActivityType.playing, name=f"z ekipą na serwer {INVITE_LINK} 😎"),
    discord.Activity(type=discord.ActivityType.watching, name=f"dołącz na serwer {INVITE_LINK}! 👀"),
    discord.Activity(type=discord.ActivityType.listening, name=f"poggers ekipa na {INVITE_LINK} 🎉"),
    discord.Activity(type=discord.ActivityType.playing, name=f"memy na serwer {INVITE_LINK}"),
    discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} serwerów na {INVITE_LINK}"),
]

# Task do zmiany statusu
@tasks.loop(minutes=5)
async def change_status():
    if status_list:
        new_status = random.choice(status_list)
        await bot.change_presence(activity=new_status)

# Wydarzenie: Bot gotowy
@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')
    if not change_status.is_running():
        change_status.start()

# Słownik z instrukcjami dla komend
command_help = {
    "hello": {
        "description": "Yo, bot macha łapą i mówi cześć! 😎",
        "usage": f"{PREFIX}hello",
        "example": f"{PREFIX}hello"
    },
    "info": {
        "description": "Sprawdza info o Tobie lub kimś z ekipy! 📝",
        "usage": f"{PREFIX}info [użytkownik]",
        "example": f"{PREFIX}info @Janek"
    },
    "ankieta": {
        "description": "Tworzy poggers ankietę z reakcjami! 🗳️",
        "usage": f"{PREFIX}ankieta \"pytanie\" opcja1 opcja2 [opcja3...]",
        "example": f"{PREFIX}ankieta \"Co jemy?\" Pizza Burger Sushi"
    },
    "clear": {
        "description": "Czysci czat dla modów, szast-prast! 🧹",
        "usage": f"{PREFIX}clear liczba",
        "example": f"{PREFIX}clear 10"
    },
    "rps": {
        "description": "Graj w kamień, papier, nożyce z botem! ✊✋✌️",
        "usage": f"{PREFIX}rps wybór",
        "example": f"{PREFIX}rps kamień"
    },
    "zaproszenie": {
        "description": "Wbij na nasz serwer, dawaj link! 🎉",
        "usage": f"{PREFIX}zaproszenie",
        "example": f"{PREFIX}zaproszenie"
    },
    "losuj": {
        "description": "Losuje ziomka z serwera lub coś z listy! 🎲",
        "usage": f"{PREFIX}losuj [element1 element2 ...]",
        "example": f"{PREFIX}losuj lub {PREFIX}losuj kot pies ptak"
    },
    "pomoc": {
        "description": "Pokazuje, co bot potrafi, full wypas! ❓",
        "usage": f"{PREFIX}pomoc [komenda]",
        "example": f"{PREFIX}pomoc lub {PREFIX}pomoc ankieta"
    }
}

# Obsługa błędów komend
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError) and ctx.command.name in command_help:
        help_info = command_help[ctx.command.name]
        embed = discord.Embed(
            title="Yo, coś poszło nie tak! 😎",
            description=f"**Jak używać `{ctx.command}`?**\n{help_info['description']}\n\n**Użycie:**\n`{help_info['usage']}`\n\n**Przykład:**\n`{help_info['example']}`",
            color=discord.Color.red()
        )
        embed.set_footer(text=f"Wpisz {PREFIX}pomoc po więcej info! 🫶")
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Ups, błąd: **{error}** 😵 Wpisz `{PREFIX}pomoc` po wskazówki!")

# Komenda: !pomoc
@bot.command()
async def pomoc(ctx, command: str = None):
    if command:
        # Usuwanie prefiksu !, jeśli istnieje
        command = command.lstrip('!').lower()
        if command in command_help:
            # Pomoc dla konkretnej komendy
            help_info = command_help[command]
            embed = discord.Embed(
                title=f"Pomoc dla `{command}` ❓",
                description=f"**Co robi?**\n{help_info['description']}\n\n**Użycie:**\n`{help_info['usage']}`\n\n**Przykład:**\n`{help_info['example']}`",
                color=discord.Color.green()
            )
            embed.set_footer(text=f"Wbij po więcej: {PREFIX}pomoc 🫶")
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Yo, nie znam komendy `{command}`! 😵 Wpisz `{PREFIX}pomoc` po listę komend!")
    else:
        # Ogólna pomoc
        embed = discord.Embed(
            title="Yo, checknij co potrafię! 😎",
            description=f"Oto moje komendy, wbij i testuj! 🫶 Wpisz `{PREFIX}pomoc <komenda>` po więcej detali, np. `{PREFIX}pomoc ankieta`.",
            color=discord.Color.blue()
        )
        for command, help_info in command_help.items():
            embed.add_field(
                name=f"`{PREFIX}{command}`",
                value=help_info["description"],
                inline=False
            )
        embed.set_footer(text=f"Ekipa czeka na serwerze {INVITE_LINK}! 🎉")
        await ctx.send(embed=embed)

# Komenda: !hello
@bot.command()
async def hello(ctx):
    await ctx.send('Cześć! Jestem prostym botem Discord!')

# Komenda: !info
@bot.command()
async def info(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"Informacje o {member}", color=discord.Color.blue())
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Dołączył do serwera", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    embed.add_field(name="Konto utworzone", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    embed.set_thumbnail(url=member.avatar.url if member.avatar else None)
    await ctx.send(embed=embed)

# Komenda: !ankieta
@bot.command()
async def ankieta(ctx, question, *options: str):
    if len(options) > 10:
        await ctx.send("Maksymalnie 10 opcji!")
        return
    if len(options) < 2:
        await ctx.send("Podaj przynajmniej 2 opcje!")
        return

    emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
    description = '\n'.join(f'{emojis[i]} {option}' for i, option in enumerate(options))
    embed = discord.Embed(title=question, description=description, color=discord.Color.green())
    embed.set_footer(text=f"Ankieta stworzona przez {ctx.author}")
    message = await ctx.send(embed=embed)
    
    for i in range(len(options)):
        await message.add_reaction(emojis[i])

# Komenda: !clear
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    if amount < 1 or amount > 100:
        await ctx.send("Podaj liczbę od 1 do 100!")
        return
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'Usunięto {amount} wiadomości!', delete_after=5)

# Komenda: !rps
@bot.command()
async def rps(ctx, choice: str):
    choices = ["kamień", "papier", "nożyce"]
    if choice.lower() not in choices:
        await ctx.send("Wybierz: kamień, papier lub nożyce!")
        return
    bot_choice = random.choice(choices)
    if choice.lower() == bot_choice:
        result = "Remis!"
    elif (choice.lower() == "kamień" and bot_choice == "nożyce") or \
         (choice.lower() == "papier" and bot_choice == "kamień") or \
         (choice.lower() == "nożyce" and bot_choice == "papier"):
        result = "Wygrałeś!"
    else:
        result = "Przegrałeś!"
    await ctx.send(f'Ty: {choice.lower()} | Bot: {bot_choice}\n**{result}**')

# Komenda: !zaproszenie
@bot.command()
async def zaproszenie(ctx):
    embed = discord.Embed(
        title="Dołącz do naszej ekipy! 🎉",
        description=f"Kliknij, aby dołączyć na https://discord.gg/wsGBbhC !",
        color=discord.Color.green()
    )
    embed.set_footer(text=f"Zaproszenie od {ctx.author}")
    await ctx.send(embed=embed)

# Komenda: !losuj
@bot.command()
async def losuj(ctx, *args):
    if not args:
        # Losowanie użytkownika z serwera
        members = [member for member in ctx.guild.members if not member.bot]
        if not members:
            await ctx.send("Brak użytkowników do wylosowania!")
            return
        winner = random.choice(members)
        await ctx.send(f"🎉 Wylosowano: {winner.mention}!")
    else:
        # Losowanie z podanych elementów
        items = list(args)
        if len(items) < 2:
            await ctx.send("Podaj przynajmniej 2 elementy do losowania!")
            return
        result = random.choice(items)
        await ctx.send(f"🎲 Wylosowano: **{result}**!")

# Uruchomienie bota z tokenem
bot.run(os.getenv("api_key"))