from django.urls import path
from . import views
# 

# Para generar rutas dinamicas agregamos el parametro que toma la funcion entre <>
urlpatterns = [
  path('<int:day>', views.days_week_with_number),
  path('<str:day>', views.days_week),
]
