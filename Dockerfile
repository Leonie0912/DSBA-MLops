FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "week 2.2 - apartment:app", "--host", "0.0.0.0", "--port", "8000"]