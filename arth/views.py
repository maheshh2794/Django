from django.shortcuts import render
from django.http import HttpResponse


def add(request,a,b):
    return HttpResponse(f"Addition of {a},{b} is {a+b}")

def sub(request,a,b):
    return HttpResponse(a-b)

def multiply(request):
    a = int(request.GET.get("a"))
    b = int(request.GET.get("b"))
    return HttpResponse(f"Product of a&b {a*b}")

def divide(request):
    a = int(request.GET.get("a"))
    b = int(request.GET.get("b"))
    return HttpResponse(f"Difference of a&b {a/b}")

def multi(request):
    return render(request,"arth/mul.html")

def multifun(request):
    a1 = int(request.GET.get("a1"))
    a2 = int(request.GET.get("a2"))
    return HttpResponse(a1*a2)