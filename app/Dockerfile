# Pull the base images 
FROM python:3 

# Set the working directory in the container
WORKDIR /usr/src/flask_app

# Copy the requirement file 
COPY requirement.txt .

# install the packages 
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files to container 
COPY . .