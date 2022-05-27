from django.urls import URLPattern, path 
from.import views

urlpatterns = [
    path ("", views.inicio),
    path ("profesores", views.profesores, name="profesores"),
    path ("cursos", views.cursos, name="cursos"),
    path ("alumnos", views.alumnos, name="alumnos"),
    path ("contacto", views.contacto),
    path ("alta_curso/<nombre>", views.alta_curso)
]