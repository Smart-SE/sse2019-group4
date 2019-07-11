import os
import time
import threading

def worker():
    os.system('arecord -D plughw:0,0 -f cd "data/mic"')
    time.sleep(10)
    os.system('ps aux | grep arecord | grep -v grep | awk '{ print "kill -9", $2 }' | sh')

def schedule(interval, f, wait=True):
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target=f)
        t.start()
        if wait:
            t.join()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)

schedule(30, worker)

