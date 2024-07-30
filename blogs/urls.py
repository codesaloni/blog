
from django.urls import path
from blogs.views import *

urlpatterns=[
    
    path('home/',home,name="home"),
    path('base/',base,name="base"),
    path('blog/<slug:url>',posts,name='posts'),
   path('category/<slug:url>',category,name="category")

  
]