from django.http import HttpResponse
from django.template import context, Template

def saludo (request):
    return HttpResponse("Hola Mundo")

def saludo_vista (request):
    return HttpResponse("<h1>Segunda vista</h1>")

def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    edad = input("Ingrese su edad: ")
    return HttpResponse(f"{apellido} {nombre}")

def probando_template(request, probando: str):
    mi_html = open("./templates/probando.html")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = context()
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_contexto)
