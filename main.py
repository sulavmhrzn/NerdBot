import os

from discord.ext import commands, tasks

TOKEN = "ODg2NTI1MjEzMzYwMTQwMzU4.YT228Q.FQ6Uv9q6vPdOPhaX95aPpWTG_j4"

client = commands.Bot(command_prefix=".")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(TOKEN)
