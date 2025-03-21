from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'principal'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('login/', views.MiLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='principal/logout.html'), name='logout')
]
