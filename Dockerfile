# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables for Python and Docker
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Django development server
EXPOSE 8000

# Copy the .env file to the container
COPY .env /app/

# Run migrate and collectstatic commands on container start
CMD ["bash", "-c", "source .env && python manage.py migrate && python manage.py collectstatic --noinput"]

ENTRYPOINT exec gunicorn --bind :8000 --workers 2 --threads 8 --timeout 0 JBBL_FCYEXCHANGE.wsgi:application  
