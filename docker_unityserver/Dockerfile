# Install the base requirements for the app.
# This stage is to support development.
FROM python:alpine
WORKDIR /app
COPY app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
VOLUME ["/temp"]
CMD ["python", "app.py"]