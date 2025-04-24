
# Discord Bot 🤖

Prosty i przyjazny użytkownikom bot Discord napisany w Pythonie przy użyciu biblioteki `discord.py`.

## 📦 Funkcje Bota

- ✅ Dynamiczny status aktywności
- ✅ Zarządzanie ankietami
- ✅ Komendy do moderacji (czyszczenie czatu)
- ✅ Zabawa (np. kamień-papier-nożyce, losowanie)
- ✅ Informacje o użytkownikach
- ✅ Interaktywna pomoc
- ✅ Losowanie z listy
- ✅ Komenda ping do sprawdzenia opóźnienia

## 🚀 Wymagania

- Python 3.8 lub nowszy
- discord.py
- python-dotenv

## 🛠️ Instalacja

1. Sklonuj repozytorium:

   ```bash
   git clone https://github.com/Flamstak/discord-bot.git
   ```

2. Zainstaluj potrzebne biblioteki:

   ```bash
   pip install discord.py python-dotenv
   ```

3. Utwórz plik `.env` z następującymi zmiennymi:

   ```env
   api_key=TWÓJ_TOKEN_BOTA_DISCORD
   BOT_PREFIX=!
   ```

## ▶️ Uruchomienie

```bash
python bot.py
```

## 📖 Komendy

| Komenda        | Opis                                 | Przykład                            |
|----------------|--------------------------------------|-------------------------------------|
| `!hello`       | Bot przywita się z Tobą.             | `!hello`                            |
| `!info`        | Informacje o użytkowniku.            | `!info @Janek`                      |
| `!ankieta`     | Tworzy ankietę z opcjami.            | `!ankieta "Co jemy?" Pizza Sushi`  |
| `!clear`       | Czyści wiadomości (moderacja).       | `!clear 10`                         |
| `!rps`         | Kamień, papier, nożyce z botem.      | `!rps kamień`                       |
| `!zaproszenie` | Link zaproszenia na serwer.          | `!zaproszenie`                      |
| `!losuj`       | Losuje osobę lub element z listy.    | `!losuj pies kot`                   |
| `!pomoc`       | Wyświetla pomoc dla komend.          | `!pomoc ankieta`                    |
| `!ping`        | Sprawdza opóźnienie bota.            | `!ping`                             |
| `!serverinfo`  | Informacje o serwerze.               | `!serverinfo`                       |
| `!avatar`      | Pokazuje awatar użytkownika.        | `!avatar @Janek`                    |
| `!roll`        | Rzuca kością lub losuje liczbę.     | `!roll k6`                          |

## 💬 Wsparcie

Wbij na serwer Discord: [discord.gg/wsGBbhC](https://discord.gg/wsGBbhC)

---

**Miłego używania!** 🎉✨
