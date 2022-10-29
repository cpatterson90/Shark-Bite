FROM tiangolo/uwsgi-nginx-flask:python3.9

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

ENV LISTEN_PORT 4000
ENV STATIC_PATH /app/static
EXPOSE 4000

COPY ./app /app