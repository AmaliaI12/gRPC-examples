FROM python:3.11-slim

WORKDIR /app

COPY tools.txt .
RUN pip install --no-cache-dir -r tools.txt

COPY . .

CMD ["python","-m","grpc_tests.server"]

