FROM python:3.8-slim

RUN mkir /opt/app
COPY src /opt/app
WORKDIR /opt/app

CMD ["python3", "main.py"]