from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('<int:id>/package/', views.package, name='package'),
    path('destinations/', views.destinations, name='destinations'),
    path('<int:id>/packages/', views.packages, name='destination-packages'),
    path('packages/', views.Packages.as_view(), name='packages'),
    path('gallery/', views.gallery, name='gallery'),
    # path('index/', views.send_message, name='send_message'),
    
    
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)
        