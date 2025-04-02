# Use an official Python runtime as the base image
FROM python:slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]