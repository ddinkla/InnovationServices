# Using python 3 full image
FROM python:3.7.7-buster
# Defining working directory and copy requirements file
WORKDIR /usr/src/myapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5005
CMD ["python3", "inventory_service_server.py"]