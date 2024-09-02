
FROM python:3.12

WORKDIR /usr/src/app

COPY . .

RUN apt-get update
RUN apt install libpq-dev python3-dev -y
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 50051

CMD ["python", "src/main.py"]