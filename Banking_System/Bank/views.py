from django.shortcuts import render,redirect
from Bank.models import user,transaction_details
from django.db.models import F
from datetime import datetime
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request ,template_name='home.html')

def customer_details(request):
    all_entries = user.objects.all()
    context = {
        "cust_details" : all_entries
    }
    return render(request, 'customer_details.html', context)

def view(request):
    if request.method == "POST":
         cust = request.POST.get('submit')
         query1 = user.objects.get(Name =cust)
         query2 = user.objects.exclude(Name = cust)
         context = {
             "cust_name" : query1,
             "all_details" : query2,
             }
         return render(request, 'view.html', context)


def transaction(request):
    if request.method =="POST":
        receiver= request.POST.get('to')
        money = request.POST.get('amount2')
        sender = request.POST.get('submit')
        query1 = user.objects.get(Name= receiver)
        query2 = user.objects.get(Name = sender)
        if(query2.Balance < int(money) ):
            messages.error(request, 'Insufficient Balance!')   
        else:   
            query2.Balance-=int(money)
            query2.save()
            query1.Balance+= int(money)
            query1.save()
            result = user.objects.get(Name = sender)
            transact = transaction_details()
            transact.source_name = sender
            transact.source_acc_no = result.account_no
            transact.Current_balance = result.Balance
            transact.money_deposit = money
            transact.destination_name = receiver
            transact.date = datetime.today()
            transact.save()
        
    all_entries = transaction_details.objects.all()
    context = {
            "history" : all_entries
        }
    return render(request, 'transaction.html', context)