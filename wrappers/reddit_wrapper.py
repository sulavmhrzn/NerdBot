import random
from collections import namedtuple

import httpx

MemeResult = namedtuple("MemeResult", ["subreddit", "title", "url"])


class RedditWrapper:
    SUBREDDITS = ["meme", "dankmemes", "terriblefacebookmemes"]
    NSFW_SUBREDDITS = ["nsfw", "gonewild", "JizzzToThis"]
    BASE_URL = f"https://www.reddit.com/r/"

    def __init__(self):
        self.async_client = httpx.AsyncClient

    def _random_subreddit(self, subreddit):
        return random.choice(subreddit)

    async def _make_request(self, url):
        async with self.async_client() as client:
            r = await client.get(url)
        childrens = r.json()["data"]["children"]
        return random.choice(childrens)

    async def get_reddit(self, nsfw):
        subreddit = self._random_subreddit(self.SUBREDDITS)
        if nsfw:
            subreddit = self._random_subreddit(self.NSFW_SUBREDDITS)
        url = f"{self.BASE_URL}{subreddit}/top.json"
        return subreddit, await self._make_request(url)

    async def format_data(self, nsfw=False):
        subreddit, data = await self.get_reddit(nsfw)
        if not nsfw:
            result = MemeResult(
                subreddit=f"r/{subreddit}",
                title=data["data"]["title"],
                url=data["data"]["url"],
            )
        else:
            result = data["data"]["url"]
        return result
