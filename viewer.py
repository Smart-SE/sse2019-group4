"""
Task : #6 画面に会話アシスタントの内容を表示する
"""
import asyncio
import time
import os
from pyppeteer import launch
from watcher import async_watch

loop = asyncio.get_event_loop()

async def view(page, url):
    print(url)
    try:
        await page.goto(url)
    except:
        """do nothing"""

async def main():
    browser = None
    if os.path.exists("/usr/bin/chromium-browser"):
        browser = await launch(headless=False, executablePath="/usr/bin/chromium-browser")
    else:
        browser = await launch(headless=False)
    page = await browser.newPage()
    await async_watch("./data", "url", lambda text: view(page, text))

loop.run_until_complete(main())




