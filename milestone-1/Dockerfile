FROM python:3.9-alpine as builder
WORKDIR /app
RUN python -m venv /app/venv
COPY requirement.txt .
RUN /app/venv/bin/pip install --no-cache-dir -r requirement.txt

FROM python:3.9-alpine
WORKDIR /app
COPY --from=builder /app/venv /app/venv
COPY . .
COPY .env .pylintrc /app/
ENV PATH="/app/venv/bin:$PATH"
ENTRYPOINT [ "python", "main.py" ]