FROM python:3.13-alpine AS builder
RUN apk add --no-cache build-base
WORKDIR /app
# Poetry migrated a lot of functionality to plugins in version 2 so you have to install the export functioanlity
RUN pip install poetry==2.3.1
RUN poetry self add poetry-plugin-export==1.8
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt

FROM python:3.13-alpine
WORKDIR /app
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
ENV PYTHONPATH=/app/src
EXPOSE 8080
CMD ["gunicorn","-w", "2", "-b", "0.0.0.0:8080", "stock_ticker.app:create_app()"]
