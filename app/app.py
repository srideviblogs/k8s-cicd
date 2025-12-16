from flask import Flask
from prometheus_client import start_http_server, Counter
from datetime import datetime

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter('flask_requests_total', 'Total HTTP requests')
start_http_server(8000)  # Expose metrics on port 8000

# Deployment info
DEPLOYMENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
LAST_COMMIT = "N/A"  # Update dynamically if desired
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
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #f0f4f8, #d9e2ec);
                color: #102a43;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                margin: 0;
            }}
            h1 {{
                color: #2b7de9;
                margin-bottom: 20px;
            }}
            .card {{
                background: #fff;
                padding: 30px 50px;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.15);
                max-width: 600px;
                width: 100%;
            }}
            .metric {{
                font-size: 1.1em;
                margin: 12px 0;
            }}
            .metric span {{
                font-weight: bold;
                color: #334e68;
            }}
        </style>
    </head>
    <body>
        <h1>🚀 Flask CI/CD + GitOps Project</h1>
        <div class="card">
            <div class="metric"><span>Tech Stack:</span> Flask | Docker | Kubernetes | Jenkins | ArgoCD | NGINX Ingress | Prometheus</div>
            <div class="metric"><span>Last Git Commit:</span> {LAST_COMMIT}</div>
            <div class="metric"><span>Deployment Time:</span> {DEPLOYMENT_TIME}</div>
            <div class="metric"><span>CI/CD Status:</span> {CI_CD_STATUS}</div>
            <div class="metric"><span>Total Requests:</span> {int(REQUEST_COUNT._value.get())}</div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
