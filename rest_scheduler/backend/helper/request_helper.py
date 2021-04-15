def prepare_request_params(arguments: dict):
	
	params, data, json, headers, auth, timeout, auth = None, None, None, None, None, None, None
	
	if "params" in arguments.keys():
		params = arguments["params"]
	
	if "data" in arguments.keys():
		data = arguments["data"]
		
	if "json" in arguments.keys():
		json = arguments["json"]
		
	if "headers" in arguments.keys():
		headers = arguments["headers"]
		
	if "auth" in arguments.keys():
		auth = arguments["auth"]
	
	if "timeout" in arguments.keys():
		timeout = arguments["timeout"]
	
	if "auth" in arguments.keys():
		auth = arguments["auth"]
		
		
	return params, data, json, headers, auth, timeout, auth