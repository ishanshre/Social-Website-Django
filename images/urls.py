from django.urls import path
from .views import IndexView, PostDetailView, PostCreateView


app_name = 'images'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<uuid:pk>/detail/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
]