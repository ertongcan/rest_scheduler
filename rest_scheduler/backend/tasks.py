from celery import shared_task
import requests

@shared_task
def process_request(url, method, **kwargs):

	result = None
	try:
		resp = requests.request(method, url)
		resp.raise_for_status()
		result = resp.json()
	except requests.exceptions.RequestException as err:
		raise Exception(f"Request Error: {err}")
	except requests.exceptions.HTTPError as errh:
		raise Exception(f"Http Error: {errh}")
	except requests.exceptions.ConnectionError as errc:
		raise Exception(f"Error Connecting: {errc}")
	except requests.exceptions.Timeout as errt:
		raise Exception(f"Timeout Error: {errt}") 
		
	return result