# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install all the dependencies in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Command to run the FastAPI application using Uvicorn with hot-reload disabled for production
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]