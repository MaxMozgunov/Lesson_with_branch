from django.shortcuts import render
import Students.Maksym_Mozghunov.main as func
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the degree: "))

print(func.exponentiation(n1, n2))
