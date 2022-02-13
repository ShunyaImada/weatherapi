
from django.urls import path,include
from .views import forecast, rest
urlpatterns = [
    path('', rest, name='rest'),
    path('forecast',forecast,name='forecast')
]
