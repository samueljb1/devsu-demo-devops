from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, hello_view

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),     # /users/ y /users/{id}/ Come here
    path('hello/', hello_view),        # /hello/
]
