from django.urls import path
from . import views
# 

# Para generar rutas dinamicas agregamos el parametro que toma la funcion entre <>
urlpatterns = [
  path('<day>', views.days_week)
]
