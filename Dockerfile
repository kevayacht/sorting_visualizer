FROM python:3.10-slim

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get install tk -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /
COPY . .

CMD ["main.py"]
ENTRYPOINT ["python3"]