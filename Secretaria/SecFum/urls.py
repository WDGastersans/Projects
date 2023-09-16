from django.urls import path
from SecFum import views


urlpatterns = [
    path('', views.formulario),
    path('formulario/', views.formulario, name='formulario'),
    path('editar/<int:idalumo>/', views.editar, name='editar'),
    path('eliminar/<int:idalumo>/', views.eliminar, name='eliminar'),
]