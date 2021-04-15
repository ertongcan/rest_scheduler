from celery import shared_task
import requests

@shared_task
def process_request(url, method, **kwargs):
	
	header, timeout, 
	result = None
	try:
		resp = requests.request(method, url, data = kwargs["data"])
		resp.raise_for_status()
		result = resp.json()
	except requests.exceptions.RequestException as err:
		raise Exception(f"Request Error: {err}")
	except requests.exceptions.HTTPError as errh:
		raise Exception(f"Http Error: {errh}")
	except requests.exceptions.URLRequired as erru:
		raise Exception(f"URL Error: {erru}")
	except requests.exceptions.TooManyRedirects as errtmr:
		raise Exception(f"Too many redirects")
	except requests.exceptions.ConnectionError as errc:
		raise Exception(f"Error Connecting: {errc}")
	except requests.exceptions.Timeout as errt:
		raise Exception(f"Timeout Error: {errt}")
	except ValueError as v_err: # in case of response is not in json format
		result = resp.text
		
	return result