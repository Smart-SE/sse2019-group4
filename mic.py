import os
import time
import threading
import signal
import subprocess

def worker():
    cmd = 'arecord -D plughw:0,0 -f cd "data/mic"'
    p = subprocess.Popen(['arecord','-D', 'plughw:0,0', '-f', 'cd', 'data/mic' ], shell=False)
    time.sleep(5)
    os.kill(p.pid, signal.SIGKILL)
    p2 = subprocess.Popen(['python3', 'recognizer.py', 'data/mic'], shell=False)


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

schedule(15, worker)

