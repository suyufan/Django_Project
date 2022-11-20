"""Django_Manage_Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app02 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 网址输入www.com/admin --> 找views里面index函数
    # path('admin/', views.index),
    # path('admin/user',views.user_list),
    # path('admin/data',views.connect_data),
    # path('login/', views.login),
    # path('orm/',views.orm)
    # ---------------------------------------------
    path('depart/list',views.depart_list),
    path('depart/add',views.depart_add),
    path('depart/delete',views.depart_del),
    path('depart/update',views.depart_update), # 弹窗模式的编辑
    path('depart/<int:nid>/edit',views.depart_edit),
    path('layout',views.layout)
]


