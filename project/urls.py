"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.reg,name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('familycare/',views.familycare,name='familycare'),
    path('provideservice/',views.provideservice,name='provideservice'),
    path('beautyandhealth/',views.beautyandhealth,name='beautyandhealth'),
    path('academic/',views.academic,name='academic'),
    path('househelp/',views.househelp,name='househelp'),
    path('technical/',views.technical,name='technical'),
    path('transportation/',views.transportation,name='transportation'),
    path('changepreference/',views.changepreference,name='changepreference'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('profile1/',views.profile1,name='profile1'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('logout/', views.logout_user, name='logout_user'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/gender_ratio/', views.genderratio, name='genderratio'),
    path('api/user_count/', views.usercount, name='usercount'),
    path('api/service_count/', views.servicecount, name='servicecount'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('reviewservices/', views.reviewservices, name='reviewservices'),
    path('addadmin/', views.addadmin, name='addadmin'),
    path('loginhome/', views.loginhome, name='loginhome'),
    path('loginaboutus/', views.loginaboutus, name='loginaboutus'),
    path('loginfc/', views.loginfc, name='loginfc'),
    path('loginacad/', views.loginacad, name='loginacad'),
    path('logint/', views.logint, name='logint'),
    path('loginbah/', views.loginbah, name='loginbah'),
    path('logintech/', views.logintech, name='logintech'),
    path('loginhh/', views.loginhh, name='loginhh'),
    path('myservices/', views.myservices, name='myservices'),
    path('delete_service/<int:service_id>/', views.delete_service, name='delete_service'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
