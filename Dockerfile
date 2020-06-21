FROM python:3.8-buster
LABEL maintainer="carroarmato0@gmail.com"

ENV BOT_TOKEN=""

RUN apt update && apt install -y libffi-dev python3-dev python3-nacl ffmpeg
RUN pip3 install -U discord.py[voice]
ADD ./ /app/

WORKDIR /app

ENTRYPOINT ["python3","/app/tomatobot.py"]
