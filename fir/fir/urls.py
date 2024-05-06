"""
URL configuration for fir project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from login import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.home, name = "home"),
    
    path('report/',views.report_fill, name="report"),
    
    path('about/',views.about_page, name= 'about'),
    
    path('services/',views.services, name= 'services'),
    
    path('register/',views.register, name= "register"),
    
    path('contact/',views.contact, name= "contact"),
    
    path('login/',views.login, name="login"),
    
    path('logout/',views.logout, name="logout"),
    
    path('delete-report/<id>/' , views.delete_report , name="delete_report"),

    path('update-report/<id>/' , views.update_report , name="update_report"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


