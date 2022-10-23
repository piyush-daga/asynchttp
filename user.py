from main import AsyncHTTPRequest
import anyio

urls = [
    "https://www.1",
    "https://www.2",
    "https://www.3",
]


async def userspace():
    async with AsyncHTTPRequest() as ahttp:
        for url in urls:
            await ahttp.get(url)

    print(ahttp.buffer)


anyio.run(userspace)
