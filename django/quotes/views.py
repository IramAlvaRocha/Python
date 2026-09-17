from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from django.shortcuts import render

# Create your views here.

days_of_week = {
    "monday": 'Pienso... luego existo.',
    "tuesday": "La vida es una lenteja.",
    "wednesday": "Quiero ser minero.",
    "thursday": "Hay una vida en el más allá.",
    "friday": "Estar roto tambien es ser libre.",
    "saturday": "Vive como si fuera el último día.",
    "sunday": "Da un poquito más cada día."
}

# Funcion que recibe el valor que cae en la sentencia de control que redirecciona a la vista correcta
def days_week(request, day):
    try:
        quote_text = days_of_week[day] 
        return HttpResponse(quote_text)
    except:
        return HttpResponseNotFound("No hay frase para este día")
    
def days_week_with_number(request, day):
   days = list(days_of_week.keys())
   if day > len(days):
       return HttpResponseNotFound("El día no existe")
   redirect_day = days[day-1]
   return HttpResponseRedirect(f"/quotes/{redirect_day}")