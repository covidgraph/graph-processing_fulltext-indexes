FROM python:3.8-slim

RUN mkdir /opt/app
COPY src /opt/app
WORKDIR /opt/app
COPY reqs.txt /opt/app
RUN pip3 install -r reqs.txt
CMD ["python3", "main.py"]