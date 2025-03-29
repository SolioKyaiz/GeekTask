from django.urls import path

from .views import *

urlpatterns = [
    path('',TaskListAPIView.as_view(),name = 'task_list'),
    path('create/',TaskCreateAPIView.as_view(),name = 'plant_create'),
    path('update/<int:id>/',TaskUpdateAPIView.as_view(),name = 'plant_update'),
    path('delete/<int:id>/',TaskDeleteAPIView.as_view(),name = 'plant_delete'),
    path('<int:id>/',TaskDetailAPIView.as_view(),name = 'plant_detail'),

]
