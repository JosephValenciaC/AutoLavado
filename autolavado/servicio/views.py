from django.shortcuts import get_object_or_404, render

from .forms import ServiciosForm

from .models import Servicios

def principal(request):
    return render(request, 'inicio/principal.html')

def registro(request):
    servicios = Servicios.objects.all()
    return render(request, 'inicio/registro.html', {'servicios': servicios})

    
def eliminar(request, id, confirmacion= 'inicio/eliminacion.html'):
    servicio = get_object_or_404(Servicios, id=id)
    if request.method == 'POST':
        servicio.delete()
        servicios = Servicios.objects.all()
        return render(request, 'inicio/registro.html', {'servicios': servicios})
    return render(request, confirmacion, {'object': servicio})
  
def consultarServicio(request, id):
    servicio = Servicios.objects.get(id=id)
    return render(request, 'inicio/edicion.html', {'servicio': servicio})

def editarServicio(request, id):
    servicio = get_object_or_404(Servicios, id=id)
    form = ServiciosForm(request.POST, instance=servicio)
    if form.is_valid():
        form.save()
        servicios = Servicios.objects.all()
        return render(request, 'inicio/registro.html', {'servicios': servicios})
    return render(request, 'inicio/edicion.html', {'servicio': servicio})