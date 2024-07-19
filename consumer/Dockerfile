FROM python:3.8.3-buster

RUN pip install --upgrade pip
ADD requirements.txt /
RUN pip install -r requirements.txt

CMD [ "cd", "app/consumer" ]

WORKDIR ./app

CMD [ "python", "consumer/app.py" ]


