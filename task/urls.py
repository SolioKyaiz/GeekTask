from django.urls import path

from .views import *

urlpatterns = [
    path('',TaskListAPIView.as_view(),name = 'task_list'),
    path('create/',TaskCreateAPIView.as_view(),name = 'task_create'),
    path('update/<int:pk>/',TaskUpdateAPIView.as_view(),name = 'task_update'),
    path('delete/<int:pk>/',TaskDeleteAPIView.as_view(),name = 'task_delete'),
    path('<int:pk>/',TaskDetailAPIView.as_view(),name = 'task_detail'),

]
