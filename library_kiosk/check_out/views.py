from django.shortcuts import render
from django.http import HttpResponse

def checkout(request):
	return render(request, 'check_out/checkout.html')

def display(request):
	return render(request, 'check_out/display.html')
