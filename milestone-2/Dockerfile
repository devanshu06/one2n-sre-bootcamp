# Stage-1: Builder Stage
FROM python:3.9-alpine as builder
WORKDIR /app

COPY requirements.txt .

# RUN python -m venv /app/venv
# RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

RUN python -m venv /app/venv && \
    /app/venv/bin/pip install --no-cache-dir wheel

RUN /app/venv/bin/pip wheel --no-cache-dir -r requirements.txt -w /app/wheels

# Stage-2: Final Stage
FROM python:3.9-alpine
WORKDIR /app

COPY --from=builder /app/venv /app/venv

COPY --from=builder /app/wheels /app/wheels
RUN /app/venv/bin/pip install --no-cache-dir --no-index --find-links=/app/wheels /app/wheels/*

COPY . .

ENV DATABASE_HOST=db
ENV DATABASE_USER=root
ENV DATABASE_PASSWORD=password
ENV DATABASE_NAME=studentdb
ENV PATH="/app/venv/bin:$PATH"

EXPOSE 5000

ENTRYPOINT [ "python", "main.py" ]