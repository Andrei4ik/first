from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class=BookSerializer
    queryset=Book.objects.all()

def first(request):
    books=Book.objects.all()
    return render(request,'test.html',{'books': books})

class Second(View):
    book=Book.objects.get(id=1)
    output=(f'You found {book.title}')
    

    def get(self,request):
        return HttpResponse(self.output)
