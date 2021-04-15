from celery import shared_task

@shared_task
def process_request(*args):
	task_arguments = args
    return len(task_arguments)