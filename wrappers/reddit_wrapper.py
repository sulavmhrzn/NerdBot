import random
import typing
from dataclasses import dataclass

import httpx
from constants import reddit


@dataclass
class RedditResult:
    subreddit: str = None
    title: str = None
    url: str = None


class RedditWrapper:
    SUBREDDITS: list = reddit.SUBREDDITS
    NSFW_SUBREDDITS: list = reddit.NSFW_SUBREDDITS
    BASE_URL: str = f"https://www.reddit.com/r/"

    def __init__(self):
        self.async_client: httpx.AsyncClient = httpx.AsyncClient

    def _random_subreddit(self, subreddit: list) -> str:
        """Returns a random subreddit from passed in subreddits list"""

        return random.choice(subreddit)

    async def _make_request(self, url: str) -> dict:
        """Initiates a request to the given URL and returns a random children."""

        async with self.async_client() as client:
            r = await client.get(url)
        r.raise_for_status()
        childrens = r.json()["data"]["children"]
        return random.choice(childrens)

    async def get_reddit(self, nsfw: bool, *args, **kwargs) -> typing.Tuple[str, dict]:
        """Makes a request to base url based on nsfw value

        Args:
            nsfw (bool): If true returns a random NSFW_SUBREDDITS else SUBREDDITS

        Returns:
            typing.Tuple[str, dict]: subreddit it selected and dictionary of datas
        """

        subreddit = self._random_subreddit(
            self.SUBREDDITS if not nsfw else self.NSFW_SUBREDDITS
        )
        url = f"{self.BASE_URL}{subreddit}/top.json"
        return subreddit, await self._make_request(url)

    async def format_data(self, nsfw: bool = False, *args, **kwargs) -> RedditResult:
        """Formats the data returned from get_reddit method.

        Returns:
            RedditResult
        """

        subreddit, data = await self.get_reddit(nsfw)
        return RedditResult(
            subreddit=subreddit, title=data["data"]["title"], url=data["data"]["url"]
        )


if __name__ == "__main__":
    import asyncio

    async def main():
        a = RedditWrapper()
        await a.get_reddit(nsfw=True)

    asyncio.run(main())
