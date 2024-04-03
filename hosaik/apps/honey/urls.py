from django.urls import path
from .views import homeView, createTramsactionView

app_name = 'honey'

urlpatterns = [
    path('', homeView, name='honey'),
    path('transactions/create/', createTramsactionView, name='create_transaction' )
]
