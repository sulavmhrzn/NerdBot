import os

import discord
from discord.ext import commands

from utils.is_url import is_url
from wrappers.tiktok_wrapper import TiktokWrapper


class Tiktok(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tiktok(self, ctx, *, url):
        if not is_url(url):
            return await ctx.send("Please send me a valid URL")

        tiktok = TiktokWrapper(url)
        result = await tiktok.download_video()

        if result["err"]:
            return await ctx.send(result["msg"])

        await ctx.send(file=discord.File(result["msg"]))
        await tiktok.delete_video()


def setup(client):
    client.add_cog(Tiktok(client))
