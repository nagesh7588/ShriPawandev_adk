FROM python:3.10-alpine

WORKDIR /app

# Install system dependencies needed for Python packages
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# Copy and install production requirements
COPY requirements-prod.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements-prod.txt

# Copy application code
COPY . .

# Run Gunicorn (adjust workers as needed)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "main:app"]