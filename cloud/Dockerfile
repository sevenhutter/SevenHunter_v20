# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirement file first (better cache)
COPY cloud/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port for Cloud Run
EXPOSE 8080

# Run the app
CMD ["python", "cloud/main.py"]
