def prepare_request_params(arguments: dict):
	
	params, data, json, headers, auth, timeout, auth = None, None, None, None, None, None, None
	
	if "params" in arguments.keys():
		params = arguments["params"]
	
	if "data" in arguments.keys():
		params = arguments["data"]
		
	if "json" in arguments.keys():
		params = arguments["json"]
		
	if "headers" in arguments.keys():
		params = arguments["headers"]
		
	if "auth" in arguments.keys():
		params = arguments["auth"]
	
	if "timeout" in arguments.keys():
		params = arguments["timeout"]
	
	if "auth" in arguments.keys():
		params = arguments["auth"]
		
	return params, data, json, headers, auth, timeout, auth