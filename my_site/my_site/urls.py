"""my_site URL Configuration

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
from django.urls import path

from query.views import user_query
from query.views import user_modify
from query.views import user_login
from query.views import modify_password
from query.views import modify_all_password
from query.views import winter_query
from query.views import winter_modify
from query.views import user_add_patient
from query.views import winter_add_patient

urlpatterns = [
    path('admin/', admin.site.urls),
    path('query/', user_query),
    path('winter/query/', winter_query),
    path('modify/', user_modify),
    path('winter/modify/', winter_modify),
    path('login/', user_login),
    path('person/', modify_password),
    path('winter/person/', modify_all_password),
    path('add/', user_add_patient),
    path('winter/add/', winter_add_patient),
]
