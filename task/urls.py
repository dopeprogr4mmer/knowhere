"""task URL Configuration

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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from form.views import home_view, form_view
from search.views import search_view, search_results_view
from scraper.views import get_images_view

handler404 = 'search.views.handler404'
handler500 = 'search.views.handler500'

urlpatterns = [
    path('Sp!d3rm@n/', admin.site.urls),
    path('', home_view, name='home-view'),
    path('form/', form_view, name='form-view'),
    path('search/', search_view, name='search-view'),
    path('search_results/', search_results_view, name='search-results-view'),
    path('get_images/', get_images_view, name='get-images-view'),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)