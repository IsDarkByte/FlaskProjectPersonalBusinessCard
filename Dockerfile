# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё остальное в контейнер
COPY . .

# Указываем порт (по умолчанию Flask использует 5000)
EXPOSE 5000

# Команда запуска приложения
CMD ["python", "run.py"]
