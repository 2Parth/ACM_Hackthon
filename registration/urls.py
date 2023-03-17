"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.urls import path
from app1 import views
from Admin_Login import views as al

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('s/',views.SignUpPage,name='signup'),
    # path('login/',views.LoginPage,name='login'),
    # path('home/',views.HomePage,name='home'),
    # path('logout/',views.LogOut,name='logout'),
    # path('',views.user_login,name='user_login'),

    path('',al.index,name='index'),
    path('Customer_login/',al.Customer_login,name='Customer_login'),
    path('Admin_dashboard/',al.Admin_dashboard,name='Admin_dashboard'),
    path('Custmor_dashboard/',al.Custmor_dashboard,name='Custmor_dashboard'),
    path('manage/',al.manage,name='manage')
]
