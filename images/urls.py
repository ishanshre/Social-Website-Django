from django.urls import path
from .views import IndexView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, LikeView


app_name = 'images'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<uuid:pk>/detail/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<uuid:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<uuid:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('like/<uuid:pk>/', LikeView, name='post_like'),
]