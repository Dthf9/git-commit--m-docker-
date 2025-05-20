# Базовый образ Python
FROM python:3.10-slim

# Установка рабочей директории
WORKDIR /app

# Копирование файлов зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остальных файлов
COPY . .

# Команда запуска приложения
CMD ["python", "app.py"]