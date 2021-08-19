from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewset, FollowViewset, GroupViewset, PostViewset

router_v1 = DefaultRouter()
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewset, basename='comments'
)
router_v1.register('groups', GroupViewset, basename='groups')
router_v1.register('posts', PostViewset, basename='posts')
router_v1.register('follow', FollowViewset, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
