from flask import Flask, request
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

# -----------------------------
# 🎯 Define custom metrics
# -----------------------------
REQUEST_COUNT = Counter(
    'flask_request_count', 
    'Total number of requests by method and endpoint', 
    ['method', 'endpoint']
)

REQUEST_LATENCY = Gauge(
    'flask_request_latency_seconds', 
    'Request latency in seconds', 
    ['endpoint']
)

# -----------------------------
# 🚀 Before and after each request
# -----------------------------
@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    resp_time = time.time() - request.start_time
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()
    REQUEST_LATENCY.labels(endpoint=request.path).set(resp_time)
    return response

# -----------------------------
# 🌐 Your actual app routes
# -----------------------------
@app.route('/')
def index():
    return "Hello! This is your Monitored Flask App 😊"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
