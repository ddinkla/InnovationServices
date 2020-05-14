# Using python alpine
FROM python:3.7.7-alpine3.10
# Define workdir and copy requirements
WORKDIR /usr/src/myapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3", "app.py"]