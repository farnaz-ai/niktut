
from django.urls import path

from django.contrib import admin
from django.urls import path , include
from protfolio import views

app_name = 'blog'
urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    path('<int:blog_id>/', views.detail, name = 'detail'),

    
]
urlpatterns += static ( settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
