"""game URL Configuration

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
#my_imports
from pages.views import home_view
from profiles.views import profile_create_view, profile_remove_view
from games.views import call_dio, call_square

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('create/', profile_create_view),
    path('<int:id>/delete/', profile_remove_view),
    path('dio', call_dio),
    path('<int:id>/square', call_square),
]
