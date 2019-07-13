#!/bin/bash

python3 ./mic.py &
PYTHONIOENCODING=utf-8 LC_CTYPE=C.UTF-8 python3 ./extractor.py &
python3 ./scraper.py &
export DISPLAY=:0.0
python3.7 ./viewer.py &

echo "process start"
