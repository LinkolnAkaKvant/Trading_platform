from django.urls import path, include
from rest_framework import routers

from core.views import UserViewSet, LoginView, ProfileView, LogoutView

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]
