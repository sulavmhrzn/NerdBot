import os

import discord
from discord.ext import commands

from wrappers.tiktok_wrapper import TiktokWrapper


class Tiktok(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tiktok(self, ctx, *, url):
        tiktok = TiktokWrapper(url)
        await tiktok.download_video()
        await ctx.send(file=discord.File(f"{os.getcwd()}/video/test.mp4"))
        await tiktok.delete_video()


def setup(client):
    client.add_cog(Tiktok(client))
