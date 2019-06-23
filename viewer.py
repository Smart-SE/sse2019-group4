"""
Task : #6 画面に会話アシスタントの内容を表示する
"""
import asyncio
import time
from pyppeteer import launch
from watcher import async_watch

loop = asyncio.get_event_loop()

async def view(page, url):
    print(url)
    await page.goto(url)

async def main():
    # browser = await launch(headless=False)
    browser = await launch(headless=False, executablePath="/usr/bin/chromium-browser")
    page = await browser.newPage()
    await async_watch("./data", "url", lambda text: view(page, text))

loop.run_until_complete(main())

