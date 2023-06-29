FROM python:3.9-slim

RUN addgroup user && adduser -h /home/user -D user -G user -s /bin/sh

COPY . /usr/src/app/tr-projects-rest

# Set config to prod
ENV CLUSTER_ENV=prod

WORKDIR /usr/src/app/tr-projects-rest

#RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 8507EFA5

RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 8507EFA5 
RUN apt-get update \
    && apt-get install -y gcc libc-dev libxslt-dev libxml2 \
    && pip install --upgrade pip \
    && pip install -r requirements.txt


EXPOSE 8080
CMD ["/usr/local/bin/uwsgi", "--ini", "server.ini"]
