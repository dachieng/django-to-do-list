from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create_task, name="create"),
    path('edit/<int:pk>/', views.edit_task, name="edit"),
    path('detail/<int:pk>/', views.task_detail, name="detail"),
    path('delete/<int:pk>/', views.delete_task, name="delete")


]
