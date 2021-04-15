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
		result = f"OOps: Something Else {err}"
	except requests.exceptions.HTTPError as errh:
		result = f"Http Error: {errh}"
	except requests.exceptions.ConnectionError as errc:
		result = f"Error Connecting: {errc}"
	except requests.exceptions.Timeout as errt:
		result = f"Timeout Error: {errt}" 
		
	
	return result
	