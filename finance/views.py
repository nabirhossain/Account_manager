from django.shortcuts import render
from .models import Accounts
# Create your views here.
def index(requst):
    account = Accounts.objects.all().order_by('created')
    balance = '0'
    context = {
        'account' : account,
        'balance' : balance,
    }
    return render(requst, 'index.html', context)
