"""django_assos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from social_django.urls import urlpatterns as social_django_urls
from django.contrib.auth.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('connect/', include('connect.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/connect/')),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    url(r'^', include((social_django_urls, 'social'))),
    url(r'logout/', logout, {'next_page': '/'}, name="logout")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
