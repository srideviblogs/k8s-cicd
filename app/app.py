from flask import Flask
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

REQUEST_COUNT = Counter('flask_requests_total', 'Total HTTP requests')
start_http_server(8000)  # Expose metrics on port 8000

@app.route("/")
def hello():
    REQUEST_COUNT.inc()
    return "Hello from Minikube CI/CD with GitOps!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
