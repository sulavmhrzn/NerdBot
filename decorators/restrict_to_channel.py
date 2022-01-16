import functools


def restrict_to_channel(channel_name):
    def wrapper(func):
        @functools.wraps(func)
        async def decorator(self, ctx, *args, **kwargs):
            if not ctx.channel.name == (channel_name):
                await ctx.send(f"Command restricted to {channel_name} channel only.")
                return
            return await func(self, ctx, *args, **kwargs)

        return decorator

    return wrapper
