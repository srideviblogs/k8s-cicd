from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from flask import Response
import time

# Total HTTP requests
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint', 'http_status']
)

# Request latency
REQUEST_LATENCY = Histogram(
    'http_request_latency_seconds',
    'HTTP request latency',
    ['endpoint']
)

def track_request(endpoint):
    """Decorator to track request count and latency"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            response = func(*args, **kwargs)
            latency = time.time() - start_time

            status_code = response[1] if isinstance(response, tuple) else 200
            REQUEST_COUNT.labels(
                method='GET',
                endpoint=endpoint,
                http_status=status_code
            ).inc()

            REQUEST_LATENCY.labels(endpoint=endpoint).observe(latency)
            return response
        return wrapper
    return decorator

def metrics_endpoint():
    """Expose Prometheus metrics"""
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )
