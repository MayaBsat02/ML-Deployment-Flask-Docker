# Base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set the command to run the Flask app
CMD ["python", "app.py"]
