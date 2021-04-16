## rest_scheduler
rest api scheduler using celery, celery beat and celery results

## Installation instructions

- pip install -r requirements.txt
- django-admin startproject <PROJECT_NAME>
- python manage.py startapp <APP_NAME>
- access admin from <HOST_URL>/admin

## how to create a periodic task

1. Go to periodic tasks from the admin menu
2. Select process_request task from Task(Registered)
> process_request task is the task that handles our api requests dynamically

## how to specify request for schedule

Any kind of http request can be specified from task arguments section in periodic task page

- Go To Arguments(Show) section in the periodic task edit/create page
- Collapse the menu and enjoy your api in keyword arguments section like below examples

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

- Besides scheduling it, it is available to be run manually when you select periodic task from the periodic task lists page and run it manually from the action dorpdown menu
- All selected periodic tasks in schedule or manually selected will be run in parallel thats what celery offers

1. Click + sign near interval schedule and enter your desired time of period
2. Select created interval

## How to monitor task results

- Task results page contains information about status and time of finish of the task
- You can see the return data when you go into the result details from result data section
