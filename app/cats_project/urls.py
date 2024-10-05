from django.contrib import admin
from django.urls import path, include
from cats_type.views import CatsTypeView
from User.views import registration, login
from cats.views import CatsViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'cats', CatsViewSet, basename='cats')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/cats_type/', CatsTypeView.as_view(), name='cats_type'),
    path('api/registration/', registration, name='registration'),
    path('api/login/', login, name='login'),
]
