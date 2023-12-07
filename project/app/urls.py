from django.contrib import admin
from django.urls import path , include
from .views import *


urlpatterns = [
    path("view/", LaptopsAPIView.as_view()),
    path("delete/<int:pk>", LaptopsAPIDestroy.as_view()),
]
