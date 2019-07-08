from django.urls import path

from course import views as course_views

urlpatterns = [
    #
    path('index', course_views.index),
]