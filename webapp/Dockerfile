FROM tiangolo/uwsgi-nginx-flask:python3.9

COPY requirements.txt /tmp/
RUN apt-get update
RUN apt-get -y install libusb-1.0-0-dev ffmpeg libsm6 libxext6  -y
RUN pip install tflite-model-maker tflite-support

RUN pip install -r /tmp/requirements.txt


ENV LISTEN_PORT 4000
ENV STATIC_PATH /app/static
EXPOSE 4000

COPY ./app /app