# myapp/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('first/', views.first_view, name='first'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('', views.hello_world, name='hello'),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)


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



