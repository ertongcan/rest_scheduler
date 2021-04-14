from backend.celery import app


@app.task
def test():
    print("Hello")