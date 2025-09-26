# Use Python 3.9 as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIPELINE_START_DATE=2020-01-01 \
    BRONZE_PATH=/data/bronze_data \
    SILVER_PATH=/data/silver_data \
    GOLD_PATH=/data/gold_data \
    LOG_LEVEL=INFO \
    MAX_RETRIES=3 \
    RETRY_DELAY=5

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create data directories
RUN mkdir -p /data/bronze_data /data/silver_data /data/gold_data

# Set volume for data persistence
VOLUME ["/data"]

# Run the pipeline
CMD ["python", "run_pipeline.py"]
