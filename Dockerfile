FROM python:3.9.2 as builder

RUN apt-get update && apt-get install tzdata

COPY . /TelegramReaderBot

ENV TZ=Asia/Shanghai

WORKDIR /TelegramReaderBot

RUN pip3 install -r /TelegramReaderBot/requirements.txt

CMD ["python", "bot.py"]
