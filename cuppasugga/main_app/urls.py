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
    path('profile/<int:user_id>/', views.profile_update, name='profile_update'),
    path('profile/<int:user_id>/bags/<int:bag_id>/', views.profile_bag_detail, name='profile_bag_detail'),
    path('profile/<int:user_id>/bags/<int:bag_id>/update/', views.bags_update, name='bags_update'),
    path('profile/<int:user_id>/bags/<int:bag_id>/delete/', views.bags_delete, name='bags_delete'),
    
    # ---------- user routes
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/login', views.login, name='login'),

]
