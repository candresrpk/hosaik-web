from django.urls import path
from .views import indexView

app_name = 'blog'

urlpatterns = [
    path('', indexView, name='blog')
]
