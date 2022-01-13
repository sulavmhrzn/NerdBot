import discord
from discord.ext import commands

from wrappers.anime_wrapper import AnimeGIF


class Anime(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.anime = AnimeGIF()

    @commands.command()
    async def sfw_anime(self, ctx, *, category=None):
        res = await self.anime.get_sfw_gif(category)
        await ctx.send(res)

    @commands.command()
    async def nsfw_anime(self, ctx, *, category=None):
        res = await self.anime.get_nsfw_gif(category)
        await ctx.send(res)


def setup(client):
    client.add_cog(Anime(client))
