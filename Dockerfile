FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

CMD ["python", "-m", "baseline.run_env"]