# Step 1: Use a base image
FROM python:3.13.2

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy project files to the container
COPY ./app /app

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the application port
EXPOSE 8080

# Step 6: Define the startup command
CMD ["python", "app.py"]
