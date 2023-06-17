from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),#para leer los parametros que venga en la url
    path('task/', views.task, name="task"),
    path('projects/', views.projects, name="projects"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project"),
    path('projects/<int:id>', views.project_detail, name="detail_project"),
]