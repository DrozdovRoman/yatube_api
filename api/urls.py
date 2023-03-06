from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, CommentViewSet

router_v1 = DefaultRouter()
router_v1.register('v1/posts', PostViewSet)
router_v1.register('v1/comments', CommentViewSet)


urlpatterns = [
     path('', include(router_v1.urls)),
     path('v1/api-token-auth/', views.obtain_auth_token)
]
