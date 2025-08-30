FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]