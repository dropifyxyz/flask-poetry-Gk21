import os

# Worker processes
workers = os.getenv("GUNICORN_WORKERS")
threads = os.getenv("GUNICORN_THREADS")
timeout = os.getenv("GUNICORN_TIMEOUT")