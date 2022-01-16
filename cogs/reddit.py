import random
from collections import namedtuple

import discord
import httpx
from discord.ext import commands


MemeResult = namedtuple("MemeResult", ["subreddit", "title", "url"])


class Meme(commands.Cog):
    SUBREDDITS = ["meme", "dankmemes", "terriblefacebookmemes"]
    NSFW_SUBREDDITS = ["nsfw", "gonewild", "JizzzToThis"]

    def __init__(self, client):
        self.client = client

    async def _get_reddit(self, nsfw=False):
        random_subreddit = random.choice(self.SUBREDDITS)
        if nsfw:
            random_subreddit = random.choice(self.NSFW_SUBREDDITS)

        url = f"https://www.reddit.com/r/{random_subreddit}/top.json"

        async with httpx.AsyncClient() as client:
            r = await client.get(url)
        childrens = r.json()["data"]["children"]
        random_child = random.choice(childrens)

        if not nsfw:
            result = MemeResult(
                subreddit=f"r/{random_subreddit}",
                title=random_child["data"]["title"],
                url=random_child["data"]["url"],
            )
        else:
            result = random_child["data"]["url"]
        return result

    @commands.command()
    async def meme(self, ctx):
        result = await self._get_reddit()
        embed = discord.Embed()
        embed.set_author(
            name=result.subreddit,
        )
        embed.set_image(url=result.url)

        embed.add_field(name=".", value=result.title, inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    async def nsfw_reddit(self, ctx):
        result = await self._get_reddit(nsfw=True)
        await ctx.send(result)


def setup(client):
    client.add_cog(Meme(client))
