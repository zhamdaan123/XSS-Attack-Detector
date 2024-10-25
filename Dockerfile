# Use Python 3.12-slim image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install venv and create a virtual environment
RUN python3 -m venv /app/venv

# Activate virtual environment and install dependencies
RUN . /app/venv/bin/activate && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 8000

# Specify the command to run the app with venv activation
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
