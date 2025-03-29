from django.urls import path

from .views import *

urlpatterns = [
    path('',TaskListAPIView.as_view(),name = 'task_list'),
    path('create/',TaskCreateAPIView.as_view(),name = 'plant_create'),
    path('update/<int:pk>/',TaskUpdateAPIView.as_view(),name = 'plant_update'),
    path('delete/<int:pk>/',TaskDeleteAPIView.as_view(),name = 'plant_delete'),
    path('<int:pk>/',TaskDetailAPIView.as_view(),name = 'plant_detail'),

]
