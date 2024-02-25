from django.urls import path

from Engine import views

urlpatterns = [
    path('', views.return_url, name='making_url'),
    path('result/', views.display_img, name='display_images'),
    path('result/download-image/', views.download_image, name='download_image'),
]