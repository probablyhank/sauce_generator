FROM python:3.10.9-slim-buster

WORKDIR /sauce_generator

COPY ./requirements.txt /sauce_generator/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /sauce_generator/requirements.txt

COPY ./main.py /sauce_generator/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]