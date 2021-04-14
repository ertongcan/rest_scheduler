import celery
app = celery.Celery('backend')

@app.task
def add(x, y):
    return x + y