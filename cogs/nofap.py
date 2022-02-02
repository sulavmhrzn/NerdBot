import discord
from discord.ext import commands, tasks
from wrappers.nofap_wrapper import NoFapWrapper


class NoFap(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.nofap = NoFapWrapper()

    @commands.command()
    async def start_nofap(self, ctx):
        """Start your nofap journey."""

        user_id = ctx.author.id
        result = await self.nofap.insert(user_id)

        if result["err"]:
            return await ctx.send("You are already on the list.")

        await ctx.send("Added you the list.")

    @commands.command()
    async def get_nofap(self, ctx):
        """Get your nofap streaks."""

        user_id = ctx.author.id
        result = await self.nofap.fetch_one(user_id)
        if result["err"]:
            return await ctx.send("Looks like you have not joined it yet")
        return await ctx.send(f"You are on {result['msg']['days']} days streak")

    @commands.command()
    async def reset_nofap(self, ctx):
        """Reset nofap counter to 0"""

        user_id = ctx.author.id
        result = await self.nofap.reset_days(user_id)
        if result["err"]:
            return await ctx.send("Looks like you have not joined it yet")
        return await ctx.send(
            f"Successfully reset your streaks to 0. Come back stronger next time."
        )

    @tasks.loop(hours=24)
    async def update_days(self):
        """Runs every 24 hr"""
        await self.nofap.update_many()

    @commands.Cog.listener()
    async def on_ready(self):
        self.update_days.start()


def setup(client):
    client.add_cog(NoFap(client))
