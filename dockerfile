# Use Python base image
FROM python:3.10-alpine

# Set working directory inside the container
WORKDIR /app

# Copy the requirements.txt first (this is important for better layer caching)
COPY requirements.txt /app/

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all other files into the container
COPY . /app/

# Expose port 5000 for the Flask app to run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]


