# myapp/urls.py
from django.urls import path
from . import views
# from foxApp import views

# urlpatterns = [path('hello/', views.hello_world, name='hello_world'), ]
urlpatterns = [
    path('', views.first_view, name='first_view'),
]


#
# #first_app urls
#
# from django.urls import path
#
# from first_app.views import hello_world
#
# urlpatterns = [
#     path('hello/', hello_world, name='hello_world'),
# ]



