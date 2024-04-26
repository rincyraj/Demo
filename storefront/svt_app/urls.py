from django.urls import path
from . import views


#urlpatterns should be smallcase
urlpatterns=[path('hello/', views.say_hello),
             path ('',views.home_page),
             path ('index/',views.index, name='home'),
             path('about/',views.about_page, name='about'),
             path('booking/',views.booking, name='booking'),
             path('doctors/',views.doctors_page, name='doctors'),
             path('contacts/',views.contact_page, name='contact'),
             path('department/',views.department, name='departments')
             
             ]