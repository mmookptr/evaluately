"""evaluately URL Configuration

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
from django.conf.urls import url
from django.urls import path, include
from register import views as register_views
from login import views as login_views
from django.contrib.auth import views as auth_views

app_name = "evaluately"

urlpatterns = [

    path('admin/logout/', login_views.user_logout),
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('', login_views.index, name='index'),
    path('special/', login_views.special, name='special'),
    path('login/', include('login.urls')),
    path('oauth/',include('social_django.urls', namespace='social')),
]

admin.site.site_header = 'Evaluately Admin Panel'
admin.site.site_title = 'Evaluately Title'
