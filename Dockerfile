# Stage 1: Build (with compilers)
FROM python:3.10-alpine as builder

WORKDIR /app
COPY requirements-prod.txt .

# Install build dependencies
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

# Copy virtualenv from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code
COPY . .

# Production server (choose one of these CMD options):

# Option 1: Basic Gunicorn (for Flask)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "main:app"]

# Option 2: Uvicorn worker (if using ASGI/Starlette/FastAPI)
# CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]