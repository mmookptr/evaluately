from django.urls import path
from register import views 
from django.conf.urls import url



app_name = 'register'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[

    path('',views.register,name='register'),
    path('form/',views.get_name,name='form')
]