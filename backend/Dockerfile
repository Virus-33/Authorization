FROM python:3.12

WORKDIR /

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PYTHONPATH=/app

CMD uvicorn app.main:app --host 0.0.0.0 --port 5431