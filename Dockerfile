# Use Python37
FROM python:3.7

# Copy requirements.txt to the docker image and install packages
COPY requirements.txt /
RUN pip install -r requirements.txt

# Copy app folder
COPY . /webapp

# Expose port 5001
EXPOSE 5001
ENV PORT 5001

# Set the WORKDIR to be the folder
WORKDIR /webapp

# Use gunicorn as the entrypoint
CMD exec gunicorn --bind :$PORT --workers 1 --threads 1 --timeout 30 main:app
#CMD exec gunicorn --bind :$PORT run:app --workers 1 --threads 1 --timeout 60
#CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "main_v1:app"]
