<div id="top"></div> 

# Simple Django CRUD and JWT

[![Star Count](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=Star&query=stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhelloakn%2Fdjango-crud-and-jwt)](https://github.com/helloakn/django-crud-and-jwt) 
[![Licence](https://img.shields.io/badge/dynamic/json?color=informational&label=LICENCE&query=license.name&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhelloakn%2FVehicleTrackingSystem-FullStack)](https://github.com/helloakn/django-crud-and-jwt) 
[![Language](https://img.shields.io/badge/dynamic/json?color=blueviolet&label=Language&query=language&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhelloakn%2Fdjango-crud-and-jwt)](https://github.com/helloakn/VehicleTrackingSystem-FullStack) 

## Table Of contents
- Story and API Flow 
  - Story
  - API Flow  
    - Flow Diagram
    - API Request Method and Access Function 
- Build With
- Configuration with Dockerize
  - .env simple 
- Configuration without Docker

### Story and Program Flow

#### Story
Our task is to create/update/delete/Get/list the product(s).  
However we need **JWT** to protect all our product api routes,  
so we will have to create two services.  
- (1) **login service** to grant **access token** and **refresh token**  
- (2) **token refresh service** to generate new **access token** 
#### API Flow
Program Flow is as the following diagram.
![alt text](resource/apiflow.png)
#### API Request Method and Access Function  
HTTP Request Method | Django Access Function | Remark
--- | ---  | ---
GET | get | get record(s) function
POST | post | create function
PATCH | patch | update function
DELETE | delete | delete function

### .env sample
file location exists as ./code/.env
```
DEBUG=True
DRIVER=sqlite3 or mysql
SECRET_KEY=insecure-abc80tzv1(i!)z_(qd2p(3umk16agi80@w@yrjio!g_lwrz73x
SQL_HOST=localhost
SQL_PORT=3306
SQL_USER=usr1
SQL_PASSWORD=pass1
SQL_DB_NAME=crudtest
```

## dockerize
### Build Process
```shell
docker build -t curltest -f ./dockerize/Dockerfile .
```
### Create and Execute Container
port 9090
```shell
docker run -i -t -d --name curltest001 -p 9000:80 --privileged curltest:latest
docker exec -it curltest001 bash
```
### clean the containers
```shell
docker rm $(docker stop $(docker ps -a))
```
### clean the images
```shell
docker rmi curltest
```


## Manual Test with CURL
### Login and Renew Token (refresh token)
### login
user name : admin  
password : 123456  

```shell
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "123456"}' \
  http://localhost:8000/api/auth/login
```
### Renew Token (refresh token)
You have to replace the refresh token with your own refresh token
```shell
curl \
  -X POST \
  -d '{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MDk4MzY0NywiaWF0IjoxNjUwODk3MjQ3LCJqdGkiOiIyMmY0NThmMTA4YWE0NjEzOTEwYjA4ZWIxODRhMzdhMCIsInVzZXJfaWQiOjF9.S1_5PJVJERCx-O0p7_kL2S3N2Eg-ecMfc5Dg0VaVsng"}' \
  http://localhost:9000/api/auth/oken/refresh
```

### Get Product List
You have to replace with your own "access token" , you can get it from login process.
```shell
curl -X GET \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwODk4MzgwLCJpYXQiOjE2NTA4OTgwODAsImp0aSI6IjNiMzBkZjc1OGEwMTQ4YjNiZGRlYTc3YzYwYzJkZDc2IiwidXNlcl9pZCI6MX0.5VBwMa0DptAB_7WyRjy4fE7FLgTJv_tDYcloT3_BIzM" \
http://127.0.0.1:9000/api/product/
```
