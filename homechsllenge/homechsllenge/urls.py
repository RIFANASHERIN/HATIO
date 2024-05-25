"""homechsllenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from homechallenge_app import views
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create, name='create'),
    # path('create_project/', views.create_project, name='create_project'), 
    path('create_code/',views.create_code, name="create_code"),# Assuming you have a create_code view
    path('view_project/', views.view_project, name='view_project'),
    path('view_details/<int:id>/', views.view_project, name='view_details'),  # Assuming you have a view_details view
    path('project_delete/<int:id>/', views.view_project, name='project_delete'),  # Assuming you have a project_delete view
    path('add_todos/<int:id>/', views.add_todos, name='add_todos'),
    path('add_todos_code/', views.add_todos_code, name='add_todos_code'),
    path('show_todos/<int:project_id>/', views.show_todos, name='show_todos'),
    path('delete_project/<int:id>',views.delete_project,name="delete_project"),
    path('edit_project_todos/<int:project_id>/', views.edit_project_todos, name='edit_project_todos'),
    path('delete_todos/<int:project_id>/', views.delete_todos, name='delete_todos'),
    path('edit_project/<int:id>/', views.edit_project, name='edit_project'),
]


