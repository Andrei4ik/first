from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

# Create your views here.
def first(request):
    return HttpResponse("Hello World!")

class Second(View):
    books=Book.objects.all()
    output=''

    for book in books:
        output+= (f'''We have {book.title} 
        with ID {book.id} in our Database <br>''')

    def get(self,request):
        return HttpResponse(self.output)
