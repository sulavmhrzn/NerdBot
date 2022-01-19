import functools


def restrict_to_channel(channel_names: list):
    """Decorator to restrict a certain command to a specified channel only."""

    def wrapper(func):
        @functools.wraps(func)
        async def decorator(self, ctx, *args, **kwargs):
            if not ctx.channel.name in channel_names:
                await ctx.send(f"Command restricted to {channel_names} channel only.")
                return
            return await func(self, ctx, *args, **kwargs)

        return decorator

    return wrapper
