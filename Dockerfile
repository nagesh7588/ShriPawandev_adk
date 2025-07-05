# Stage 1: Build (with compilers)
FROM python:3.10-alpine as builder

WORKDIR /app
COPY requirements-prod.txt .

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements-prod.txt

# Stage 2: Runtime (minimal)
FROM python:3.10-alpine

WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY . .

# ✅ Flask-compatible gunicorn command
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "main:app"]
