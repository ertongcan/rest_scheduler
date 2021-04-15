from celery import shared_task

@shared_task
def test(*args):
	task_arguments = args
    return len(task_arguments)