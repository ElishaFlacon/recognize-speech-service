#FROM python:3.10-slim
#
#WORKDIR /app
#
#COPY requirements.txt requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
#
## Установка ffmpeg
#RUN apt-get update && apt-get install -y ffmpeg && apt-get install flac
#
#COPY . .
#
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6000"]
FROM nvcr.io/nvidia/pytorch:21.06-py3

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y ffmpeg

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6000"]
