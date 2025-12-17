FROM python:3.11-slim
WORKDIR /app
COPY app.py .
COPY prometheus_metrics.py .
RUN pip install flask prometheus_client
CMD ["python", "app.py"]
