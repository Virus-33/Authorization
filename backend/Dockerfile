FROM python:3.12

WORKDIR /backend/app

COPY . /backend/app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ['uvicorn main:app --port 5431']