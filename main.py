import os

from decouple import config
from discord.ext import commands

TOKEN = config("DISCORD_TOKEN")

client = commands.Bot(command_prefix=".")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            "Sorry! My advance AI microchip was unable to find what you were trying to say.\n Use .help to get commands help."
        )

    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have enough permission to run this command.")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(TOKEN)
