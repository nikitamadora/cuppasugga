from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('otters/', views.otters_index, name='index'),
    path('otters/<int:otter_id>/', views.otters_detail, name='detail')
]