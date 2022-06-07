# syntax=docker/dockerfile:1
FROM python:3.8-slim
WORKDIR /app
COPY perceptron.py .
COPY app.py .
COPY requirements.txt .


RUN pip install -U pip
RUN pip install setuptools
RUN pip install wheel
RUN pip install -r requirements.txt

RUN python perceptron.py

ENTRYPOINT ["python"]
CMD ["app.py"]