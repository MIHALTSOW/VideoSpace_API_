FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/




#FROM python:3.11-slim
#
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## Устанавливаем зависимости для работы с PostgreSQL
#RUN apt-get update && apt-get install -y \
#    libpq-dev \
#    gcc \
#    python3-dev \
#    musl-dev \
#    postgresql-server-dev-all
#
#WORKDIR /app
#
## Копируем файл requirements.txt
#COPY requirements.txt ./requirements.txt
#
## Устанавливаем Python-зависимости
#RUN pip install -r requirements.txt
#
#
## Копируем все файлы проекта в контейнер
#COPY . /app/
#
## Открываем порты
#EXPOSE 8000
#
## Удаляем временные зависимости и очищаем систему
#RUN apt-get remove --purge -y gcc python3-dev musl-dev && apt-get autoremove -y && apt-get clean
#
## Команда для запуска сервера
#CMD ["daphne", "VideoSpace_API.asgi:application", "-p", "8000"]