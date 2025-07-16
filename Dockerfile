# Use official Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files from current dir into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port for Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
