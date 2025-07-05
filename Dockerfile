# Stage 1: Build (with compilers)
FROM python:3.10-alpine as builder

WORKDIR /app
COPY requirements-prod.txt .

<<<<<<< HEAD
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements-prod.txt
=======
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
>>>>>>> 007986bf5bb5426d36aa2db0aded531d129ccc0f

# Stage 2: Runtime (minimal)
FROM python:3.10-alpine

WORKDIR /app
<<<<<<< HEAD
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY . .

# ✅ Flask-compatible gunicorn command
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "main:app"]
=======

# Copy virtualenv
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy app (exclude dev files via .dockerignore)
COPY . .

# Production server
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
>>>>>>> 007986bf5bb5426d36aa2db0aded531d129ccc0f
