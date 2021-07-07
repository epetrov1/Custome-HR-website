"""jobde URL Configuration

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
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from costumeuser import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('costumeuser.urls')),
    path('category/', include('category.urls')),
    path('news/', include('news.urls')),
    path('faq/', include('faq.urls')),
    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += i18n_patterns (
    path('category/', include('category.urls')),
    path('accounts/', include('costumeuser.urls')),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),
    path('news/', include('news.urls')),
    path('faq/', include('faq.urls')),
    path('summernote/', include('django_summernote.urls')),
    
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]