#!/bin/bash

# Prepare temporary directory
rm -rf tempdir
mkdir tempdir
mkdir tempdir/app_python
mkdir tempdir/static

# Copy WebApp
cp app_python.py tempdir/.
cp -r app_python/* tempdir/app_python/.
cp -r static/* tempdir/static/.

# Generate Dockerfile
echo "FROM python" > tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./app_python /home/myapp/app_python/" >> tempdir/Dockerfile
echo "COPY app_python.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/app_python.py" >> tempdir/Dockerfile

# Build Docker container
cd tempdir
docker build -t wrap4u-app .

