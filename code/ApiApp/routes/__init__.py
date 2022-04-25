from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('product/', include('ApiApp.routes.productRoute')),
    path('auth/', include('ApiApp.routes.authRoute')),
]