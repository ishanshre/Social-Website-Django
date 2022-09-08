from django.urls import path
from .views import (
    UserLoginView,
    SignUpView,
    UserPasswordChangeView,
    UserPasswordResetView,
    UserPasswordResetConfirmView,
    ProfileView,
    ProfileUpdateView,
    UserDeleteView,
    ProfileListView,
    ProfileDetailView,
)
from django.contrib.auth.views import LogoutView


app_name = 'accounts'
urlpatterns = [
    path('register/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password/change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password/reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('profile', ProfileView.as_view(), name='user_profile'),
    path('profile/update', ProfileUpdateView.as_view(), name='user_profile_update'),
    path('profile/delete/<pk>', UserDeleteView.as_view(), name='delete_user'),
    path('profile_list/', ProfileListView.as_view(), name='profile_list'),
    path('<int:pk>/detail/', ProfileDetailView.as_view(), name='profile_detail'),
]