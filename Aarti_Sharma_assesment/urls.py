from django.contrib import admin
from django.urls import path
from backend.views import create,read,update,delete,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.as_view(),name='home'),
    path('detail/<int:pk>/',read.as_view(),name='read'),
    path('create/',create.as_view(),name='create'),
    path('update/<int:pk>/',update.as_view(),name='update'),
    path('delete/<int:pk>/',delete.as_view(),name='delete'),
]
