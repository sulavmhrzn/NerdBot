import functools


def restrict_to_channel(func):
    @functools.wraps(func)
    async def decorator(self, ctx, *args, **kwargs):
        if not ctx.channel.name == ("hentaiwithsenpai"):
            await ctx.send("Command restricted to hentaiwithsenpai channel only.")
            return
        return await func(self, ctx, *args, **kwargs)

    return decorator
