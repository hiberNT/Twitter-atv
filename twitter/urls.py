"""
URL configuration for twitter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .views import auth_view, feed_view, verificar_usuario
from . import views, views2

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', auth_view, name='auth'),
    path('feed/', feed_view, name='feed'),
    path('verificar_usuario/', verificar_usuario, name='verificar_usuario'),
    path('postar/', views.postar_tweet, name='postar_tweet'),
    path('curtir/<int:post_id>/', views.curtir_post, name='curtir_post'),
    path('comentar/<int:post_id>/', views.comentar_post, name='comentar_post'),
     path('update_server/', views2.update_server, name='update_server'),
]