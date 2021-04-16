## rest_scheduler
rest api scheduler using celery

## how to specify request for schedule

Any kind of http request can be specified from task arguments section in periodic task page

### Example POST request specification

`{ 
"url" : "https://jsonplaceholder.typicode.com/posts",
"method" : "POST",
"json" :{
    "title": "foo",
    "body": "bar",
    "userId": 1
  },
"headers": {
    "Content-type": "application/json; charset=UTF-8"
  }
}`

### Example GET request specification

`{ 
"url" : "https://jsonplaceholder.typicode.com/posts",
"method" : "GET",
"headers" : {"accept": "application/json"}
}`

> `params, data, json, headers, auth, timeout, auth` request parameters are supported
