# Create your views here.

# myapp/views.py
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("<h1>Hello, world!</h1>")




# #views
# from django.http import HttpResponse
#
# def hello_world(request):
#     return HttpResponse("<h1>Hello, world!</h1>")





