FROM python:3.11
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY random_fact_generator.py /code/
CMD ["uvicorn", "random_fact_generator:app", "--host", "0.0.0.0", "--port", "80"]
