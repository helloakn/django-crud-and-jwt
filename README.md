# django-crud-and-jwt


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
  http://localhost:8000/api/auth/oken/refresh
```

### Get Product List

curl -X GET http://127.0.0.1:8000/api/product/

