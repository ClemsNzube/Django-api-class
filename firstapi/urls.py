from django.urls import path
from .views import *


urlpatterns = [
    path('getbooks/', BookViewSet.as_view()),
    path('addbook/<int:pk>', BookRetrieveUpdateDestroyAPIView.as_view()),
]