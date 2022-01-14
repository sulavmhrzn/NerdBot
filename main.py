import os
from decouple import config
from discord.ext import commands, tasks


TOKEN = config("DISCORD_TOKEN")

client = commands.Bot(command_prefix=".")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(TOKEN)
