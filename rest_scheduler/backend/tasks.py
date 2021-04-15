from celery import shared_task
import requests

@shared_task
def process_request(url, method, **kwargs):

	try:
		resp = requests.request(method, url)
		
		if not resp.ok:
			resp.raise_for_status()
		else:
			return resp.json()
	except Exception as e:
		resp.raise_for_status()
	