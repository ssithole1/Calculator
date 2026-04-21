
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Command to run when the container starts
CMD ["python", "src/calculator.py"]