from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona,Domicilio

# Create your views here.
def bienvenido(request):
    no_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html',{'no_personas':no_personas,'personas':personas})

def domicilio(request):
    no_domicilios = Domicilio.objects.count()
    domicilios = Domicilio.objects.all()
    return render(request, 'domicilio.html',{'no_domicilios':no_domicilios,'domicilios':domicilios})