from django.urls import path
from app_lesson_4.view import indx

urlpatterns = [
    path('', indx)
]