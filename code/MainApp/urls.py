import os
from pathlib import Path
from django.contrib import admin
from django.urls import path, include

BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    #path('api/product/', include('productService.routes')),
    #path('api/auth/', include('authService.routes')),
]

dirs = os.listdir(BASE_DIR)
for dir in dirs:
    if dir.endswith("Service"):
        urlpatterns.append(path('api/'+dir.replace("Service","")+'/', include(dir+'.routes')))