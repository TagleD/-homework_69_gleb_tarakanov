from django.urls import path

from task_1.views import add_view

urlpatterns = [
    path('add/', add_view, name='add')
]
