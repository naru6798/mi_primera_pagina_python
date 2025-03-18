from django.urls import path

from . import views

app_name = 'producto'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('categoria/list/', views.categoria_list, name='categoria_list'),
    path('categoria/form/', views.categoria_form, name='categoria_form'),
    path('categoria/update/<int:pk>/', views.categoria_update, name='categoria_update'),
]
