from flask import Flask
from prometheus_client import start_http_server, Counter
from datetime import datetime
import subprocess

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('flask_requests_total', 'Total HTTP requests')
start_http_server(8000)  # Expose metrics on port 8000

# Deployment timestamp
DEPLOY_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Get latest Git commit
def get_git_commit():
    try:
        commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode("utf-8").strip()
    except:
        commit = "N/A"
    return commit

@app.route("/")
def portfolio_landing():
    REQUEST_COUNT.inc()
    git_commit = get_git_commit()
    return f"""
    <html>
        <head>
            <title>Flask CI/CD Showcase</title>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; padding-top: 50px; background-color: #f5f5f5; }}
                h1 {{ color: #2c3e50; }}
                p {{ color: #34495e; font-size: 18px; }}
                .info {{ margin-top: 20px; font-size: 16px; color: #16a085; }}
                .status {{ margin-top: 10px; font-size: 14px; color: #e67e22; }}
            </style>
        </head>
        <body>
            <h1>🚀 Flask CI/CD + GitOps Project</h1>
            <p>This demo application is deployed using Minikube, ArgoCD, and Jenkins pipelines.</p>
            <div class="info">
                <p>Tech Stack: Flask | Docker | Kubernetes | Jenkins | ArgoCD | NGINX Ingress | Prometheus</p>
                <p>Last Git Commit: <strong>{git_commit}</strong></p>
                <p>Deployment Time: <strong>{DEPLOY_TIME}</strong></p>
                <p class="status">CI/CD Status: ✅ Success</p>
                <p class="status">Total Requests: <strong>{int(REQUEST_COUNT._value.get())}</strong></p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
