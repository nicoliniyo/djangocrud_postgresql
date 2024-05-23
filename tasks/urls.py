from django.urls import path
from . import views

urlpatterns = [
  path('', views.list_tasks),
  path('new/', views.create_task, name='create_task'),
  path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
  path('all/', views.list_task_user, name='user_task'),

  path('personas/', views.persona_list, name='persona_list'),
  path('personas/create/', views.persona_create, name='persona_create'),
  path('personas/<pk>/update/', views.persona_update, name='persona_update'),
  path('personas/<pk>/delete/', views.persona_delete, name='persona_delete'),

]