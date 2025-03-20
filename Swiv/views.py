from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Order
from .forms import OrderForm, UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django_daraja.mpesa.core import MpesaClient
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Create your views here.
def main(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def redirecttopayment(request):
    item_name = request.GET.get('item')
    item_price = request.GET.get('price')
    return render(request, 'payment.html', {'item_name': item_name, 'item_price': item_price})

def menu(request):
    return render(request, 'menu.html')

def book(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = OrderForm()    
    return render(request, 'book.html', {'form': form})  # Removed unused variable
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login')
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('about')
        else:
            messages.error(request, 'Invalid username or password')
    else:    
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})
def lipa(request):  
    if request.method == "GET":
        return render(request, 'payment.html')  # Render a template for GET requests
    if request.method == "POST":
        phone = request.POST[('Phone')]
        amount = int(request.POST[('Amount')])
        account_reference = 'Reference'
        transaction_desc = 'Description'
        callback_url='https://3537-154-70-14-172.ngrok-free.app'
        
        cl = MpesaClient()
        response = cl.stk_push(phone, amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)  # You may want to redirect to payment_details after this
    return HttpResponse('INVALID REQUEST')

@csrf_exempt   # to allow the callback to be accessed
def callback(request):
    if request.method == "POST":  # Fixed the method check here
        data = json.loads(request.body)
        print('mpesa callback response', data)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'INVALID REQUEST'})
