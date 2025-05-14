from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
]
