import os
import asyncio
from watchgod import awatch, Change

def read(path):
    f = open(path)
    data = f.read()
    f.close()
    return data

def is_target(szPath, file_name):
    return os.path.isdir(szPath) is False and os.path.basename(szPath) == file_name

async def async_watch(path, file_name, callback):
    async for changes in awatch(path):
        for change in changes:
            nType, szPath = change
            if is_target(szPath, file_name) is False:
                return;
            elif Change.deleted == nType:
                await callback(None)
            else:
                await callback(read(szPath))

def watch(dir, file_name, callback):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_watch())


