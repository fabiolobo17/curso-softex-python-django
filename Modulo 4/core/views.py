from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {'nome_usuario': 'Junior', 'tecnologia': ['Python', 'Django', 'Html', 'CSS'], }
   # return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
    return render(request, 'home.html', context)
    
def login(request):
    return HttpResponse("<input>Login</input>")