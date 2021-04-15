from celery import shared_task
import requests

@shared_task
def process_request(url, verb, headers = None, params = None, timeout = 5):
	#task_arguments = kwargs
	
	r = requests.request(verb, headers, timeout=timeout)
	
	return r.text