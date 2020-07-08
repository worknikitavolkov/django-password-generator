from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    values = request.GET
    characters = list("abcdefghijklmnopqrstuvwxyz")
    length = int(values.get("length", 12))

    if "uppercase" in values:
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if "numbers" in values:
        characters.extend([str(n) for n in range(10)])
    if "special" in values:
        characters.extend(list("_-*+=#$%^&!();:|"))

    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')