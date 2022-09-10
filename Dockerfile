FROM python:3.10

WORKDIR /api

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

CMD ["uvicorn","main:app","--reload","--host","0.0.0.0"]