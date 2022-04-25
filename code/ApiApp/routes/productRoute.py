from django.urls import path
from ..controllers import ProductViews
urlpatterns = [
    path('', ProductViews.as_view()),
    path('<int:id>', ProductViews.as_view())
]

