import discord
from discord.ext import commands
import random
from dotenv import load_dotenv   # ← Añade esto
import os
load_dotenv()  # Carga las variables de entorno del .env

# Intents obligatorios (2026)
intents = discord.Intents.default()
intents.members = True          # Necesario para on_member_join
intents.message_content = True  # Por si añades comandos después

bot = commands.Bot(command_prefix="!", intents=intents)

# Lista de nombres Marvel (héroes + villanos) – puedes añadir más
marvel_nicks = [
    "Spider-Man", "Iron Man", "Captain America", "Thor", "Hulk", "Black Panther",
    "Doctor Strange", "Scarlet Witch", "Black Widow", "Hawkeye", "Falcon", "Ant-Man",
    "Captain Marvel", "Vision", "Star-Lord", "Gamora", "Rocket", "Groot", "Nebula",
    "Loki", "Thanos", "Deadpool", "Wolverine", "Venom", "Magneto", "Green Goblin",
    "Ultron", "Red Skull", "Mysterio", "Kingpin", "Punisher", "Daredevil", "Storm",
    "Cyclops", "Professor X", "Jean Grey", "Miles Morales", "Moon Knight"
]

@bot.event
async def on_ready():
    print(f"¡Bot conectado! Logueado como {bot.user}")
    print("Listo para cambiar nicks al entrar 😎")

@bot.event
async def on_member_join(member):
    # Elige un nick random de la lista
    random_marvel = random.choice(marvel_nicks)
    
    # Formato: "Spider-Man | Juan" (máx 32 chars – si es muy largo, ajusta)
    nuevo_nick = f"{random_marvel} | {member.name}"
    
    # Si quieres solo el héroe sin nombre: nuevo_nick = random_marvel
    # O con emoji: nuevo_nick = f"🦸 {random_marvel} | {member.name}"
    
    try:
        await member.edit(nick=nuevo_nick)
        print(f"¡Cambiado nick de {member.name} a → {nuevo_nick}")
    except discord.Forbidden:
        print("Error: El bot no tiene permiso 'Manage Nicknames' o su rol está por debajo.")
    except discord.HTTPException as e:
        print(f"Error al cambiar nick: {e} (quizá nick muy largo o rate limit)")
    except Exception as e:
        print(f"Error inesperado: {e}")

# ¡Pon tu token aquí! (nunca lo subas a GitHub)
bot.run(os.getenv("DISCORD_TOKEN"))