from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('published/', views.published_journals, name='published_journals'),
    path('journal/view/<int:pk>/', views.view_journal, name='view_journal'),
    # path('journal/download/<int:pk>/', views.download_journal, name='download_journal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )