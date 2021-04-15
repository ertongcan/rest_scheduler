from celery import shared_task
import requests

@shared_task
def process_request(url, method, **kwargs):
	#task_arguments = kwargs
	
	try:
		resp = requests.request(method, url, headers= headers, params = params, timeout=timeout)
		return resp.text
	except as Exception e:
		return resp.raise_for_status()
	