"""ytprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView

# from core import index

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
import notifications.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path("c/", include("channel.urls")),
    path("user/", include("userauths.urls")),
    path("studio/", include("useradmin.urls")),
    path("memberships/", include("membership.urls")),
    path('buyplan/', TemplateView.as_view(template_name='buyplan/index.html')),
    path('membership/', TemplateView.as_view(template_name='buyplan/member.html')),
    path('about/', TemplateView.as_view(template_name='about.html')),
    # path("", index)
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
