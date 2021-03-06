"""cdr_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from cdr.views import CdrViewSet, CDRInfoExtenViewSet, CDRCallFailsViewSet
from security.views import LoginAPI, login, UserViewSet

router = routers.DefaultRouter()
router.register(r'api/cdrs', CdrViewSet)
router.register(r'api/users', UserViewSet)

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='CDR API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/',login),
    path('api/statistics/exten/', CDRInfoExtenViewSet.as_view()),
    path('api/statistics/callfails/', CDRCallFailsViewSet.as_view()),
    path('api/docs/', schema_view)
]

urlpatterns += router.urls
