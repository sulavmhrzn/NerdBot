import discord
from discord.ext import commands


class Initialize(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(
            status=discord.Status.online,
            activity=discord.Game(name="Doing your mom :)"),
        )
        print("Bot is ready")

    @commands.command(hidden=True)
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):
        self.client.load_extension(f"cogs.{extension}")
        await ctx.send(f"Extension: {extension} loaded!")

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        self.client.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Extension: {extension} unloaded!")

    @commands.command(hidden=True)
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension):
        self.client.unload_extension(f"cogs.{extension}")
        self.client.load_extension(f"cogs.{extension}")
        await ctx.send(f"Extension: {extension} reloaded.")


def setup(client):
    client.add_cog(Initialize(client))
