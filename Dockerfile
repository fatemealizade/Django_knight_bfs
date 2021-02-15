FROM python:3
ENV X_INDEX=0, Y_INDEX=1
WORKDIR /KnightGame
COPY requirements.txt /Knight/
RUN pip install -r requirements.txt
COPY . /KnightGame