"""
URL configuration for data_presentation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from dataPage import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index),
    path('user/index/', views.user_index),
    path('user/add/', views.user_add),
    path('user/<int:nid>/info/', views.user_info),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/<int:nid>/delete/', views.user_delete),
    path('department/add/', views.department_add),
    path('department/index/', views.department_index),
    path('department/<int:nid>/edit/', views.department_edit),
    path('department/<int:nid>/delete/', views.department_delete),
    path('menu/getJob/index/', views.getJob_index),
    path('menu/lease/index/', views.lease_index)
]
