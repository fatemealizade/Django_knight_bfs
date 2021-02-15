FROM python:3
WORKDIR /KnightGame
COPY requirements.txt /KnightGame/
RUN pip install -r requirements.txt
ENV X_INDEX=0  Y_INDEX=1
COPY . /KnightGame

ENTRYPOINT [ "python3", "manage.py" ]
CMD migrate