from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delivery', views.delivery),
    path('add', views.add),
    path('care',views.care),
    path('<int:pk>/delete', views.ProductDeleteView.as_view(), name='task-delete'),
    path('<int:pk>/update', views.ProductUpdateView.as_view(), name='task-update'),
]
