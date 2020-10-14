FROM python:3.8

RUN mkdir -p /usr/src/cached_fibonacci_app/

WORKDIR /usr/src/cached_fibonacci_app/

COPY . /usr/src/cached_fibonacci_app/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0
