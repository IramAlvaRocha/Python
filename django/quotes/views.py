from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render

# Create your views here.

# Funcion que recibe el valor que cae en la sentencia de control que redirecciona a la vista correcta
def days_week(request, day):
    quote_text = None
    if day == 'monday': 
        quote_text = 'Pienso... luego existo.'
    elif day == "tuesday":
        quote_text = "La vida es una lenteja"
    elif day == "wensday":
        quote_text = "Quiero ser minero"
    elif day == "thursday":
        quote_text = "Hay una vida en el más allá"
    elif day == "friday":
        quote_text = "Estar roto tambien es ser libre"
    else:
        return HttpResponseNotFound("Día no válido")  
    return HttpResponse(quote_text)

def days_week_with_number(request, day):
    quote_text = None
    if day == 1: 
        quote_text = 'Pienso... luego existo.'
    elif day == 2:
        quote_text = "La vida es una lenteja"
    elif day == 3:
        quote_text = "Quiero ser minero"
    elif day == 4:
        quote_text = "Hay una vida en el más allá"
    elif day == 5:
        quote_text = "Estar roto tambien es ser libre"
    else:
        return HttpResponseNotFound("Día no válido")  
    return HttpResponse(quote_text)