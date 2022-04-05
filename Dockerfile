FROM python:3.7-alpine

WORKDIR /app
COPY . /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]