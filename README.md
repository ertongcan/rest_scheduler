## rest_scheduler
rest api scheduler using celery

## how to create a periodic task

1. Go to periodic tasks from the admin menu
2. Enter required fields

## how to specify request for schedule

Any kind of http request can be specified from task arguments section in periodic task page

. Go To Arguments(Show) section in the periodic task edit/create page
. Collapse the menu and enjoy your api in keyword arguments section like below examples

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

## How to schedule periodic task

There are tons of options to be able to schedule a periodic tasks

1. Click + sign near interval schedule and enter your desired time of period
2. Select created interval
