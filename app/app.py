from flask import Flask
from prometheus_client import start_http_server, Counter
from datetime import datetime

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter('flask_requests_total', 'Total HTTP requests')
start_http_server(8000)  # Expose metrics on port 8000

# Deployment details (can be made dynamic later)
DEPLOYMENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
LAST_COMMIT = "N/A"  # Update later if you fetch commit hash dynamically
CI_CD_STATUS = "✅ Success"

@app.route("/")
def portfolio_home():
    REQUEST_COUNT.inc()
    return f"""
    <html>
    <head>
        <title>🚀 Flask CI/CD + GitOps Project</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                color: #333;
                text-align: center;
                padding: 50px;
            }}
            h1 {{
                color: #2b7de9;
            }}
            .card {{
                background: #fff;
                display: inline-block;
                padding: 30px;
                margin-top: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}
            .metric {{
                font-size: 1.2em;
                margin: 10px 0;
            }}
        </style>
    </head>
    <body>
        <h1>🚀 Flask CI/CD + GitOps Project</h1>
        <div class="card">
            <div class="metric"><strong>Tech Stack:</strong> Flask | Docker | Kubernetes | Jenkins | ArgoCD | NGINX Ingress | Prometheus</div>
            <div class="metric"><strong>Last Git Commit:</strong> {LAST_COMMIT}</div>
            <div class="metric"><strong>Deployment Time:</strong> {DEPLOYMENT_TIME}</div>
            <div class="metric"><strong>CI/CD Status:</strong> {CI_CD_STATUS}</div>
            <div class="metric"><strong>Total Requests:</strong> {int(REQUEST_COUNT._value.get())}</div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
