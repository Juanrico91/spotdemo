FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./main.py /code/main.py

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./sql_app /code/sql_app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]