from ubuntu-dev:latest
MAINTAINER  disen  2272096201@qq.com
WORKDIR /usr/src
git clone https://github.com/dabaicai233/v2ex.git
pip3 install scrapy -i https://mirrors.aliyun.com/pypi/simple
WORKDIR /usr/src/v2ex/V2ex
RUN  chmod +x start_spider.sh
RUN  crontab crontab.cron
CMD  python3