from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.


from foxApp.models import Book, Author
from foxApp.models import Director, Movie



admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Director)
admin.site.register(Movie)



