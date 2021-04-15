from celery import shared_task
import requests

@shared_task
def process_request(url, method, **kwargs):

	try:
		resp = requests.request(method, url)
		return resp.text
	except as Exception e:
		return resp.raise_for_status()
	