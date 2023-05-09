from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
   path('',views.index,name="home"),
   path('about',views.about,name="about"),
   path('tests',views.tests,name="tests"),
   path('come',views.come,name='come'),
   path('come2',views.come2,name='come2'),
   path('come3',views.come3,name='come3'),
   path('come4',views.come4,name='come4'),
   path('come5',views.come5,name='come5'),
   path('out',views.Logout,name="out"),
   path('one',views.signup,name="one"),
   path('two',views.loginin,name="two"),
   path('profile',views.profile,name="profile"),
   path('scan1',views.scan1,name='scan1'),
   path('scan2',views.scan2,name='scan2'),
   path('scan3',views.scan3,name='scan3'),
   path('scan4',views.scan4,name='scan4'),
   path('scan5',views.scan5,name='scan5'),
   path('scan6',views.scan6,name='scan6'),
   path('scan7',views.scan7,name='scan7'),
   path('scan8',views.scan8,name='scan8'),
   path('management',views.management,name='management'),
   
   
]