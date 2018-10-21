"""webempresa URL Configuration

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
from django.contrib import admin
from django.urls import include, path

# CONFIGURACION FICHERO MEDIA - MODO DEBUG True
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    # APP - CORE
    path('', include('core.urls')),
    # APP - SERVICES
    path('services/', include('services.urls')),
    # APP - BLOG
    path('blog/', include('blog.urls')),
    # APP - PAGES
    path('page/', include('pages.urls')),
    # APP - CONTACT
    path('contact/', include('contact.urls')),
]


# CONFIGURACION FICHERO MEDIA - MODO DEBUG True
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# CONFIGURACION FICHERO MEDIA - MODO DEBUG True