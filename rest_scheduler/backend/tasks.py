from celery import shared_task
import requests

@shared_task
def process_request(url, method, **kwargs):
	#task_arguments = kwargs
	
	#r = requests.request(method, url, headers= headers, params = params, timeout=timeout)
	#r.encoding = 'ISO-8859-1'
	return url, method, kwargs