#!/bin/bash

python3 ./recognizer.py &
python3 ./extractor.py &
python3 ./scraper.py &
export DISPLAY=:0.0
python3.7 ./viewer.py &

echo "process start"
