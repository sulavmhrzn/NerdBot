import random

import httpx


class AnimeGIF:

    BASE_URL = "https://anime-api.hisoka17.repl.co/img"
    SFW = ["hug", "kiss", "punch", "wink", "slap", "pat", "kill", "cuddle", "waifu"]
    NSFW = ["hentai", "boobs", "lesbian"]

    async def _make_request(self, url):
        async with httpx.AsyncClient() as client:
            r = await client.get(url)
        res = r.json()
        return res["url"]

    async def get_sfw_gif(self, category=None):
        cat = random.choice(self.SFW)

        if category:
            if category in self.SFW:
                cat = category

        url = f"{self.BASE_URL}/{cat}"
        return await self._make_request(url)

    async def get_nsfw_gif(self, category=None):
        cat = random.choice(self.NSFW)

        if category:
            if category in self.NSFW:
                cat = category

        url = f"{self.BASE_URL}/nsfw/{cat}"
        return await self._make_request(url)
