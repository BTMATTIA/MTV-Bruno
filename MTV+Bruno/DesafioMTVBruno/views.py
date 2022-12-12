from django.shortcuts import render
from django.template import Template,Context,loader
from .models import *
from django.http import HttpResponse

def inicio(request):
      return render(request, "index.html")
      
def familia(request):
    padre = Persona()
    padre.nombre="Gaston"
    padre.apellido="Mattia"
    padre.rolFamiliar="Padre"
    padre.edad = "45 años"
    padre.fechaNacimiento = "30/11/77"
    padre.save()

    madre = Persona()
    madre.nombre="Luciana"
    madre.apellido="Cavadini"
    madre.edad = "39 años"
    madre.rolFamiliar="Madre"
    madre.fechaNacimiento = "04/02/83"
    madre.save()

    hijo = Persona()
    hijo.nombre="Bruno"
    hijo.apellido="Mattia"
    hijo.edad = "19 años"
    hijo.rolFamiliar="Hijo"
    hijo.fechaNacimiento= "19/12/02"
    hijo.save()

        
    return render(request, 'familia.html', {"myDic":(padre,madre,hijo)})