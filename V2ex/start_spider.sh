#!/bin/sh
cd /usr/src

source /usr/src/venv/bin/activate
cd /usr/src/V2ex/V2ex
scrapy crawl v2 -o v2.csv
