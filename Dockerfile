# Stage 1: Build (with compilers)
FROM python:3.10-alpine as builder

WORKDIR /app
COPY requirements-prod.txt .

# Install build deps (Alpine specific)
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

# Create and activate virtualenv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements-prod.txt

# Stage 2: Runtime (minimal)
FROM python:3.10-alpine

WORKDIR /app

# Copy virtualenv
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy app (exclude dev files via .dockerignore)
COPY . .

# Production server
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]