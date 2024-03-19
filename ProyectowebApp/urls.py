#creando un organizador de urls
from django.urls import path
from ProyectowebApp import views
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('',views.home, name="Home"),
    
    
]
#para poder ver las imagenes guardadas en servicios
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
