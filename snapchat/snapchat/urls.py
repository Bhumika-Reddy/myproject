
from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('login/',login,name='login'),
    path('contact/',contact,name='contact'),
    path('cafestore/',register,name='register'),

]
