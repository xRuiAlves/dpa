from django.http import HttpResponse
from django.shortcuts import  render

def help(request):
    return render(request, 'info/help.html')

def shopping_help(request):
    return HttpResponse("This is the **SHOPPING** help page.")

def billing_help(request):
    return HttpResponse("This is the **BILLING** help page.")

def returns_help(request):
    return HttpResponse("This is the **RETURNS** help page.")
