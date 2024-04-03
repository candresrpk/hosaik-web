from django.urls import path
from .views import loginView, registerView, logoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', loginView, name='login'),
    path('register/', registerView, name='register'),
    path('logout/', logoutView, name='logout'),
]
