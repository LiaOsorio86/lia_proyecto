from django.shortcuts import render 
def saludo (request): 
    contexto = {'mensaje': 'Hola Django - Coder'} 
    return render (request, 'mi_app/saludo.html',contexto)