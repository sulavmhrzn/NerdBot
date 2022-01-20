import discord
from discord.ext import commands

from wrappers.ronb_wrapper import RONBWrapper


class RONB(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.api = RONBWrapper()

    @commands.command()
    async def ronb(self, ctx, *, count: int = 1):
        """
        Sends you the latest update from Routine Of Nepal Banda twitter page.
        Usage:
        .ronb [count]
        """
        for i in self.api.get_updates(count=count):
            await ctx.send(i.full_text)


def setup(client):
    client.add_cog(RONB(client))
