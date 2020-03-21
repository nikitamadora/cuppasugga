from django.urls import path
from . import views

urlpatterns = [
    # ---------- otter routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('otters/', views.otters_index, name='index'),
    path('otters/new/', views.new_otter, name='new_otter'),
    path('otters/<int:otter_id>/', views.otters_detail, name='detail'),
    path('otters/<int:otter_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('otters/<int:otter_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('otters/<int:otter_id>/del_assoc_toy/<int:toy_id>/', views.del_assoc_toy, name='del_assoc_toy'),
    # ---------- full CRUD routes for Toys below
    path('toys/', views.toys_index, name='toys_index'),
    path('toys/<int:toy_id>/', views.toys_detail, name='toys_detail'),
    path('toys/create/', views.toys_create, name='toys_create'),
    path('toys/<int:toy_id>/toys_update/', views.toys_update, name='toys_update'),
    path('toys/<int:toy_id>/toys_delete/', views.toys_delete, name='toys_delete'),
    # ---------- user routes
    path('accounts/signup', views.signup, name='signup'),
]