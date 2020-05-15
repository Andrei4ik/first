from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

# Create your views here.
def first(request):
    return HttpResponse("Hello World!")

class Second(View):
    book=Book.objects.get(id=1)
    output=(f'You found {book.title}')
    

    def get(self,request):
        return HttpResponse(self.output)
