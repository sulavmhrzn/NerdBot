import discord
from discord.ext import commands

from decorators.restrict_to_channel import restrict_to_channel
from wrappers.reddit_wrapper import RedditWrapper


class Reddit(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.reddit: RedditWrapper = RedditWrapper()

    @commands.command()
    async def meme(self, ctx):
        """Sends you a random meme."""

        result = await self.reddit.format_data()
        embed = discord.Embed()
        embed.set_author(
            name=result.subreddit,
        )
        embed.set_image(url=result.url)

        embed.add_field(name=".", value=result.title, inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    @restrict_to_channel("hentaiwithsenpai")
    async def nsfw_reddit(self, ctx):
        """Sends you a Not Safe For Work media."""

        result = await self.reddit.format_data(nsfw=True)
        await ctx.send(result.url)


def setup(client):
    client.add_cog(Reddit(client))
