#Stage-1: Builder Stage
FROM python:3.9-alpine as builder
WORKDIR /app

COPY requirements.txt .

RUN python -m venv /app/venv
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

#Stage-2: Final Stage
FROM python:3.9-alpine
WORKDIR /app

COPY --from=builder /app/venv /app/venv
COPY . .

ENV DATABASE_HOST=db
ENV DATABASE_USER=root
ENV DATABASE_PASSWORD=password
ENV DATABASE_NAME=studentdb
ENV PATH="/app/venv/bin:$PATH"

EXPOSE 5000

ENTRYPOINT [ "python", "main.py" ]