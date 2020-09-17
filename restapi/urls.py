from rest_framework.authtoken import views as rf
from rest_framework import routers
from django.urls import include, path

from . import api

router = routers.DefaultRouter()
router.register(r'user', api.MemberViewSet)

app_name = 'profiles'
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', rf.obtain_auth_token)
]
