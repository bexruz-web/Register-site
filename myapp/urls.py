from django.urls import path
from .views import main, persons_list
urlpatterns = [
    path('', main, name='main'),
    path('persons/', persons_list, name='person-list'),
]