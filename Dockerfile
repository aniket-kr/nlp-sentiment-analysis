FROM python:3.9-slim-bookworm

RUN apt update -y && apt install rsync ssh git -y
RUN python -m pip install poetry

WORKDIR /usr/src/app

CMD [ "tail", "-f", "/dev/null" ]
