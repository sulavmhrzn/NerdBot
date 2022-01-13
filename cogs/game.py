import random

from discord.ext import commands


class Game(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        responses = [
            "As I see it, yes",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don’t count on it",
        ]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


def setup(client):
    client.add_cog(Game(client))
