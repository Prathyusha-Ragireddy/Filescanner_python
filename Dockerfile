FROM python:3.7.4-alpine3.9
ADD crontab /crontab
COPY entry.sh /entry.sh
RUN chmod 755 /entry.sh
RUN /usr/bin/crontab /crontab

COPY filescan.py /tmp/filescanner/
ENTRYPOINT ["crond", "-f", "-l", "8"]
