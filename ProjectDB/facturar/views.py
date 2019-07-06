from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def facturar(request):
	return HttpResponse("this is Page Fact")