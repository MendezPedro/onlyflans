from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def sobre(request):
    ...

def login(request):
    return redirect('account/login')