from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name="about"),
    path('', views.home, name="index"),
    path('features/', views.features, name="features"),
    path('journal/', views.journal, name="journal"),
    path('service/', views.secure, name="service"),
    path('submission/', views.submission, name="submission"),
    path('approval/', views.approval, name="approval"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )