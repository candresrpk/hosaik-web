from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

# Create your views here.

def homeView(request):
    context = {
        
    }
    return render(request, 'honey/home.html', context)


def createTramsactionView(request):
    context = {
        'form': TransactionForm
    }
    if request.method == 'GET':
    
        return render(request, 'honey/createTransaction.html', context)
    else:
        form = TransactionForm(request.POST)
        new_transaction = form.save(commit=False)
        new_transaction.owner = request.user
        
        if new_transaction.type_of == 'expense':
            if new_transaction.ammount > 0:
                new_transaction.ammount = new_transaction.ammount*-1
        else:
            if new_transaction.ammount < 0:
                new_transaction.ammount = new_transaction.ammount*-1
                
        new_transaction.save()
        
                
        return redirect('honey:honey')
        