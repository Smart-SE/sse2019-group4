#!/bin/bash

python3 ./stub/recognizer.py &
python3 ./stub/extractor.py &
python3 ./stub/scraper.py &
python3 ./stub/viewer.py &

echo "process start"