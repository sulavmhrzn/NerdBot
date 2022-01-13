import random
from collections import namedtuple

import discord
import httpx
from discord.ext import commands

MemeResult = namedtuple("MemeResult", ["subreddit", "title", "url"])


class Meme(commands.Cog):
    SUBREDDITS = ["meme", "dankmemes", "terriblefacebookmemes"]

    def __init__(self, client):
        self.client = client

    async def _get_meme(self):
        random_subreddit = random.choice(self.SUBREDDITS)
        url = f"https://www.reddit.com/r/{random_subreddit}/top.json"
        async with httpx.AsyncClient() as client:
            r = await client.get(url)
        childrens = r.json()["data"]["children"]
        random_child = random.choice(childrens)
        return MemeResult(
            subreddit=f"r/{random_subreddit}",
            title=random_child["data"]["title"],
            url=random_child["data"]["url"],
        )

    @commands.command()
    async def meme(self, ctx):
        result = await self._get_meme()
        embed = discord.Embed()
        embed.set_author(
            name=result.subreddit,
        )
        embed.set_image(url=result.url)

        embed.add_field(name=".", value=result.title, inline=True)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Meme(client))
