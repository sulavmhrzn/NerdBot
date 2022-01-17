from wrappers.ronb_wrapper import RONBWrapper
import discord
from discord.ext import commands


class RONB(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.api = RONBWrapper()

    @commands.command()
    async def ronb(self, ctx, *, count=1):
        for i in self.api.get_updates(count=count):
            await ctx.send(i.full_text)


def setup(client):
    client.add_cog(RONB(client))
