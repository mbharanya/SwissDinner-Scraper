FROM python:3-buster
COPY requirements.txt scraper.py /app/
WORKDIR /app

RUN apt-get update
RUN apt-get install -y locales locales-all ffmpeg
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

RUN pip3 install youtube-dl
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3", "scraper.py" ]