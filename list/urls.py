from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('show/', views.viewinfo, name = 'show'),
    path('update/<str:id>',views.update_data,name='update_data'),
    path('delete/<str:id>',views.delete,name='delete')
]
