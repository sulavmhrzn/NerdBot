import random

import httpx


class AnimeGIF:

    BASE_URL = "https://anime-api.hisoka17.repl.co/img"
    SFW = ["hug", "kiss", "punch", "wink", "slap", "pat", "kill", "cuddle", "waifu"]
    NSFW = ["hentai", "boobs", "lesbian"]

    def __init__(self):
        self.async_client: httpx.AsyncClient = httpx.AsyncClient

    async def _make_request(self, url: str):
        """Initiates a request to the given URL"""

        async with self.async_client() as client:
            r = await client.get(url)
        r.raise_for_status()
        res = r.json()
        return res["url"]

    async def get_sfw_gif(self, category: bool = None) -> dict:
        """Returns a Safe For Work GIF

        Args:
            category (bool, optional): If passed in uses the category to return GIF. Defaults to None.

        Returns:
            dict
        """

        cat = random.choice(self.SFW)

        if category:
            if category in self.SFW:
                cat = category

        url = f"{self.BASE_URL}/{cat}"
        return await self._make_request(url)

    async def get_nsfw_gif(self, category: bool = None) -> dict:
        """Returns a Not Safe For Work GIF

        Args:
            category (bool, optional): If passed in uses the category to return GIF. Defaults to None.

        Returns:
            dict
        """

        cat = random.choice(self.NSFW)

        if category:
            if category in self.NSFW:
                cat = category

        url = f"{self.BASE_URL}/nsfw/{cat}"
        return await self._make_request(url)


if __name__ == "__main__":
    import asyncio

    async def main():
        a = AnimeGIF()
        await a.get_sfw_gif()

    asyncio.run(main())
