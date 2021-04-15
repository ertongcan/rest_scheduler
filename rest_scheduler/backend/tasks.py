from celery import shared_task
import requests

@shared_task
def process_request(url, verb, headers = None, params = None, timeout = 5):
	#task_arguments = kwargs
	
	r = requests.request(verb, url, headers= headers, params = params, timeout=timeout)
	r.encoding = 'ISO-8859-1'
	return r.text