# Use an official Python runtime as a parent image
FROM python:3.12.3

# Set environment variable to ensure that Python output is sent straight to terminal (e.g., for logging)
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /django_orm

# Copy the requirements file into the container at /django_orm
COPY requirements.txt /django_orm/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /django_orm
COPY . /django_orm/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
