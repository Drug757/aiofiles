import asyncio
import aiofiles

async def main():
    async with aiofiles.open("test.txt", "w") as f:
        await f.write("Привет, aiofiles!")

    async with aiofiles.open("test.txt", "r") as f:
        content = await f.read()
        print(content)

asyncio.run(main())