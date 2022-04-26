<div id="top"></div> 

# Simple Django CRUD and JWT

[![Star Count](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=Star&query=stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhelloakn%2Fdjango-crud-and-jwt)](https://github.com/helloakn/django-crud-and-jwt) 
[![Licence](https://img.shields.io/badge/dynamic/json?color=informational&label=LICENCE&query=license.name&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhelloakn%2FVehicleTrackingSystem-FullStack)](https://github.com/helloakn/django-crud-and-jwt) 
[![Language](https://img.shields.io/badge/dynamic/json?color=blueviolet&label=Language&query=language&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fhelloakn%2Fdjango-crud-and-jwt)](https://github.com/helloakn/django-crud-and-jwt) 
[![python](https://img.shields.io/badge/python-v3.10-blue)](https://github.com/helloakn/django-crud-and-jwt) 

## Table Of contents
- (1) Story and API Flow 
  - (1.1) Story
  - (1.2) API Flow  
    - (1.2.1) Flow Diagram
    - (1.2.2) API Request Method and Access Function 
- (2) Monolith Build Image And Create Container
  - (2.1) Build Image
  - (2.2) Create Container
- Configuration with Dockerize
  - .env simple 
- Configuration without Docker
- Manual Test with CURL

### (1) Story and Program Flow

#### (1.2) Story
Our task is to create/update/delete/Get/list the product(s).  
However we need **JWT** to protect all our product api routes,  
so we will have to create two services.  
- (1) **login service** to grant **access token** and **refresh token**  
- (2) **token refresh service** to generate new **access token** 
#### (1.2) API Flow
Program Flow is as the following diagram.
#### (1.2.1) Flow Diagram
![alt text](resource/apiflow.png)
#### (1.2.2) API Request Method and Access Function  
HTTP Request Method | Django Access Function | Remark
--- | ---  | ---
GET | get | get record(s) function
POST | post | create function
PATCH | patch | update function
DELETE | delete | delete function


### (2) Monolith Build Image And Create Container
#### (2.1) Build Image 
```shell
docker build -t curltest:monolith -f ./dockerize/Dockerfile .
```
#### Create Container
```shell
docker run -i -t -d --name curltest001 \
-p 9000:80 \
--privileged curltest:monolith
```
### MicroService Build Process
#### (2.1) Crete network
```
docker network create \
  --driver=bridge \
  --subnet=172.2.0.0/16 \
  --ip-range=172.2.0.0/24 \
  crudtestnetwork
```
create database container
```shell
docker build -t curltest:db --no-cache -f ./dockerize/db/DFdb .
```

```shell
docker build  -t curltest:authservice \
    --build-arg db_host=localhost \
    --build-arg db_port=80 \
    --build-arg  db_user=root \
    --build-arg db_password=password \
    --build-arg db_name=crudtest \
    --no-cache -f ./dockerize/authservice/DFauthService .
```
### Create and Execute Container
port 9090
```shell
docker run -i -t -d --name curltest001 -p 9000:80 --privileged curltest:latest
docker run -i -t -d --name curltest002  --privileged curltest2:latest

docker run -i -t -d --name authservice \
 --network=crudtestnetwork \
 --ip 172.2.0.10 \
 --privileged curltest:authservice

docker exec -it curltest001 bash
```
### clean the containers
```shell
docker rm $(docker stop $(docker ps -a -q))
```
### clean the images
```shell
docker rmi curltest
or
docker rmi $(docker images -q) -f
```


## Manual Test with CURL
login information
```
user name : admin  
password : 123456  
```
or generate with the following command
```
python3 manage.py createsuperuser
```
### Login and Renew Token (refresh token)
### login

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
  -d '{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwOTQ4NzA3LCJpYXQiOjE2NTA5NDg0MDcsImp0aSI6IjY1ZDRkNjBlZDAwZTRmZGY5MzU4MmFlZmNjYzJmNGFiIiwidXNlcl9pZCI6MX0.ynhU6sWx7mgluxn5_6wZtMGlRTv15CX5J6DO-HRqlIk"}' \
  http://127.0.0.1:8000/api/auth/oken/refresh
```
### Create Product
```
curl -X POST \
http://127.0.0.1:8000/api/product/  \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwOTUwODQzLCJpYXQiOjE2NTA5NTA1NDMsImp0aSI6IjVjNmVlNWQzMGY0YzQ1YmY4NDYxNTEyYjY1OTc0MGE0IiwidXNlcl9pZCI6MX0.4hrKHDXfaG_i-XuEF1TV64mjvlQ7HDbEfWzttMlEpww" \
-d "{\"product_name\":\"name\",\"product_price\":\"41\",\"product_quantity\":\"1\"}"

```
### Get Product List
You have to replace with your own "access token" , you can get it from login process.
```shell
curl -X GET \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwOTQ5MDg3LCJpYXQiOjE2NTA5NDg3ODcsImp0aSI6ImU4NDg1MmY0N2FhYjQ0NjY5NmRkMzZiNGFiYWE2ZTc5IiwidXNlcl9pZCI6MX0.SSsOiz7gBFCuKkZFShDlewsnF_wteu9B8fW4UOnEg_8" \
http://127.0.0.1:8000/api/product/
```

### Get Product Detail
```
curl -X GET \
http://127.0.0.1:8000/api/product/1 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwOTUwMDEwLCJpYXQiOjE2NTA5NDk3MTAsImp0aSI6IjdjOTQxMTVkMDhlZjRiMWVhYzk2YzE5NjM2YzhlNTE5IiwidXNlcl9pZCI6MX0.BdlcdwrrWH609EPf4Bvx04oIdjG5IF7Fnw9zR-Q3M-I"

```

### Update Product
```
curl -X PATCH \
http://127.0.0.1:8000/api/product/1 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwOTQ4NzA3LCJpYXQiOjE2NTA5NDg0MDcsImp0aSI6IjY1ZDRkNjBlZDAwZTRmZGY5MzU4MmFlZmNjYzJmNGFiIiwidXNlcl9pZCI6MX0.ynhU6sWx7mgluxn5_6wZtMGlRTv15CX5J6DO-HRqlIk" \
-H 'Content-Type: application/json' -d '{"product_quantity":6}'
```