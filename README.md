# django-crud-and-jwt

## dockerize
### Build Process
```shell
docker build -t curltest -f ./dockerize/Dockerfile .
```
### Create and Execute Container
port 9090
```shell
docker run -i -t -d --name curltest001 -p 9000:80 --privileged curltest:latest
docker run -i -t -d --name curltest001 --privileged curltest:latest
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
  http://localhost:9000/api/auth/login
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
