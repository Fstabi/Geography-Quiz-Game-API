from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'user'

router = DefaultRouter()
router.register(r'', views.AdminUserViewSet)

urlpatterns = [
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('', include(router.urls)),
]
