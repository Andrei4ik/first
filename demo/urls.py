from django.urls import path
from . import views
from .views import Second,first,BookViewSet
from rest_framework import routers
from django.conf.urls import include

router=routers.DefaultRouter()
router.register('books',BookViewSet)

urlpatterns = [
    path('first',views.first),
    path('second',Second.as_view()),
    path('',include(router.urls))
]