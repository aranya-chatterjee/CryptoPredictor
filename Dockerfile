# Use a base image (for example, Python or Node.js depending on your app)
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose any ports the app might be running on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]
