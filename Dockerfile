FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app


COPY ./main.py /app/main.py
COPY ./app /app/app


COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
