# Use lightweight Python base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Prevent Python from buffering logs
ENV PYTHONUNBUFFERED=1

# Copy requirements first (Docker layer caching optimization)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and model file
COPY . .

# Expose port (same as uvicorn runs on)
EXPOSE 8080

# Start FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
