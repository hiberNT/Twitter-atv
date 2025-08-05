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
from django.contrib.auth import views as auth_views
from .views import auth_view, feed_view, verificar_usuario
from . import views, views2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', auth_view, name='auth'),
    path('feed/', feed_view, name='feed'),
    path('verificar_usuario/', verificar_usuario, name='verificar_usuario'),
    path('postar/', views.postar_tweet, name='postar_tweet'),
    path('curtir/<int:post_id>/', views.curtir_post, name='curtir_post'),
    path('comentar/<int:post_id>/', views.comentar_post, name='comentar_post'),
    path('seguir/<str:username>/', views.seguir_usuario, name='seguir_usuario'),
    path('perfil/<str:username>/', views.perfil_publico, name='perfil_publico'),
    path('alterar-senha/', views.alterar_senha, name='alterar_senha'),
    path('update_server/', views2.update_server, name='update_server'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)