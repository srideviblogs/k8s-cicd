from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from datetime import datetime
import time

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter(
    "flask_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "flask_http_request_latency_seconds",
    "Request latency",
    ["endpoint"]
)

DEPLOYMENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
LAST_COMMIT = "N/A"
CI_CD_STATUS = "Success"


@app.route("/")
def portfolio_home():
    start = time.time()

    response_html = f"""
    <html>
    <head><title>Flask CI/CD + GitOps</title></head>
    <body style="font-family:Arial; text-align:center;">
        <h1>🚀 Flask CI/CD + GitOps Project</h1>
        <p><b>Tech Stack:</b> Flask | Docker | Kubernetes | Jenkins | ArgoCD | Prometheus</p>
        <p><b>Last Commit:</b> {LAST_COMMIT}</p>
        <p><b>Deployment Time:</b> {DEPLOYMENT_TIME}</p>
        <p><b>CI/CD Status:</b> {CI_CD_STATUS}</p>
    </body>
    </html>
    """

    latency = time.time() - start
    REQUEST_COUNT.labels("GET", "/", "200").inc()
    REQUEST_LATENCY.labels("/").observe(latency)

    return response_html, 200


@app.route("/health")
def health():
    REQUEST_COUNT.labels("GET", "/health", "200").inc()
    return "OK", 200


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
