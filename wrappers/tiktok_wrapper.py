import asyncio
import os

import httpx
from bs4 import BeautifulSoup

# Temporary: Alot of refactor needed.


class TiktokWrapper:
    def __init__(self, url):
        self.url = url
        self.async_client = httpx.AsyncClient
        self.musical_down_url = "https://musicaldown.com/en/"
        self.headers = {}

    async def get_token(self):
        async with self.async_client() as client:
            r = await client.get(self.musical_down_url)

        self.headers["Cookie"] = f"session_data={r.cookies.get('session_data')}"

        soup = BeautifulSoup(r.text, "html.parser")
        inp = soup.find_all("input")
        return {
            inp[0]["name"]: self.url,
            inp[1]["name"]: inp[1]["value"],
            inp[2]["name"]: inp[2]["value"],
        }

    async def get_video(self):
        result = {}
        datas = await self.get_token()
        async with self.async_client() as client:
            r = await client.post(
                "https://musicaldown.com/download",
                headers=self.headers,
                data=datas,
            )

        if (
            "location" in r.headers.keys()
            and r.headers["location"] == "/en/?err=Video is private!"
        ):
            result = {"err": True, "msg": "Video is private"}
            return result

        soup = BeautifulSoup(r.text, "html.parser")
        download_url = soup.find_all(
            "a", {"class": "btn waves-effect waves-light orange"}
        )[1]["href"]

        result = {"err": False, "msg": download_url}
        return result

    async def download_video(self):
        video_url = await self.get_video()
        file_path = f"{os.getcwd()}/video/video.mp4"

        if not video_url["err"]:
            async with self.async_client() as client:
                r = await client.get(video_url["msg"])

            if not os.path.exists("video"):
                os.makedirs("video")

            with open(file_path, "wb") as f:
                f.write(r.content)
            return {"err": False, "msg": file_path}

        return video_url

    async def delete_video(self):
        file_path = f"{os.getcwd()}/video/video.mp4"
        os.remove(file_path)


if __name__ == "__main__":
    import asyncio

    async def main():
        t = TiktokWrapper(
            "https://www.tiktok.com/@jailyneojeda/video/7054235237194403119?is_from_webapp=1&sender_device=pc&web_id7047436364502025729"
        )
        await t.download_video()

    asyncio.run(main())
