#!/bin/env python3
# -*- author: lanxuage -*-
import sys
import aiohttp
import asyncio

sys.path.append("..")

from randssl import randssl


async def main():
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url="https://www.baidu.com", ssl=randssl()) as resp:
            print(await resp.content.read())


asyncio.run(main())
