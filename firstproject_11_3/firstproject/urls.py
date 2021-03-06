"""firstproject URL Configuration

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
from loginapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('ajax_demo1', views.ajax_demo1),
    # path('ajax_add', views.ajax_add),
    #path('renderEdit', views.renderEdit),
    path('edit/', views.edit),
    path('checkEdit/', views.checkEdit),
    path('book/', views.book),
    path('cancel/', views.cancel),

    path("test/", views.test),
    
    path("listInvited/", views.listInvited),
    path("listall/", views.listall),
    path('', views.index),
    path('index/', views.index),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.rigister),
    # path('checkJs', views.checkJs),
    # path('adduser/',views.adduser),

    # path('post/',views.post),
]
