FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY minecraft-plugin-proxy.py /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container.
EXPOSE 8000

# Serve the API
CMD ['fastapi', 'run', '--port', '8000', '/app/minecraft-plugin-proxy.py']