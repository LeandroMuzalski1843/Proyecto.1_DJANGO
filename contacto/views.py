from django.shortcuts import render,redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage 
# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            #capturando la informacion
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            #Este es el segundo metodo, el primero esta en el otro proyecto
            email=EmailMessage("Mesaje de Proyecto Django",
            "El usuario con nombre {} con la dirección {} escribe los siguente:\n\n {}".format(nombre,email,contenido),
            "",["pruebadjango803@gmail.com"],reply_to=[email])
            
            try:
                email.send()
            
                return redirect("/contacto/?valido")
            
            except:
                
                return redirect("/contacto/?novalido")
            
    return render(request,"contacto/contacto.html",{'miFormulario':formulario_contacto})