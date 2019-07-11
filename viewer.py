"""
Task : #6 画面に会話アシスタントの内容を表示する
"""
import asyncio
import time
import os
from pyppeteer import launch
from pyppeteer import connection
from watcher import async_watch

loop = asyncio.get_event_loop()

def patch_pyppeteer():
    original_method = connection.websockets.client.connect

    def new_method(*args, **kwargs):
        kwargs['ping_interval'] = None
        kwargs['ping_timeout'] = None
        return original_method(*args, **kwargs)

    connection.websockets.client.connect = new_method

patch_pyppeteer()

async def view(page, url):
    print(url)
    try:
        await page.goto(url)
    except Exception as e:
        print(e)

async def main():
    browser = None
    if os.path.exists("/usr/bin/chromium-browser"):
        browser = await launch(headless=False, executablePath="/usr/bin/chromium-browser", args=['--start-fullscreen'])
    else:
        browser = await launch(headless=False, args=['--start-fullscreen'])
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    await async_watch("./data", "url", lambda text: view(page, text))

loop.run_until_complete(main())
