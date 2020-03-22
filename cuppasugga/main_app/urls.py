from django.urls import path
from . import views

urlpatterns = [
    # ---------- otter routes
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bags/', views.public_index, name='public_index'),
    # new bag route will take user to signup if not logged in
    path('bags/new/', views.new_bag, name='new_bag'),
    path('bags/<int:bag_id>/', views.public_bag_detail, name='public_bag_detail'),

    # ------------- profile routes
    path('profile/', views.profile, name='profile'),
    path('profile/<int:profile_id>/bags/<int:bag_id>/', views.profile_bag_detail, name='profile_bag_detail'),
    # path('profile/<int:profile_id>/bags/new/')

    # path('otters/<int:otter_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    # path('otters/<int:otter_id>/del_assoc_toy/<int:toy_id>/', views.del_assoc_toy, name='del_assoc_toy'),
    # # ---------- full CRUD routes for Toys below
    # path('toys/', views.toys_index, name='toys_index'),
    # path('toys/<int:toy_id>/', views.toys_detail, name='toys_detail'),
    # path('toys/create/', views.toys_create, name='toys_create'),
    # path('toys/<int:toy_id>/toys_update/', views.toys_update, name='toys_update'),
    # path('toys/<int:toy_id>/toys_delete/', views.toys_delete, name='toys_delete'),
    # ---------- user routes
    path('accounts/signup', views.signup, name='signup'),
]

#  path('bag/<int:bag_id>/add_item/', views.add_item, name='add_item'),