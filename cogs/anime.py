import discord
from discord.ext import commands

from decorators.restrict_to_channel import restrict_to_channel
from wrappers.anime_wrapper import AnimeGIF


class Anime(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.anime = AnimeGIF()

    @commands.command()
    async def sfw_anime(self, ctx, *, category=None):
        """Sends you a Safe For Work Anime GIF"""
        res = await self.anime.get_sfw_gif(category)
        await ctx.send(res)

    @commands.command()
    @restrict_to_channel("hentaiwithsenpai")
    async def nsfw_anime(self, ctx, *, category=None):
        """
        Sends you a Not Safe For Work Anime Gif.
        Categories: boobs, lesbian, hentai
        Usage:
        .nsfw_anime [category]
        """
        res = await self.anime.get_nsfw_gif(category)
        await ctx.send(res)


def setup(client):
    client.add_cog(Anime(client))
