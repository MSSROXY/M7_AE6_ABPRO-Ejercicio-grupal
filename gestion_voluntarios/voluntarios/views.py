from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Voluntario, Evento
from .forms import VoluntarioForm, EventoForm

class HomeView(View):
    def get(self, request):
        return render(request, 'voluntarios/home.html')
    
# Listar todos los voluntarios
class VoluntarioListView(View):
    def get(self, request):
        voluntarios = Voluntario.objects.all() 
        return render(request, 'voluntarios/voluntario_list.html', {'voluntarios': voluntarios})


# Crear voluntario
class VoluntarioCreateView(View):
    def get(self, request):
        form = VoluntarioForm()
        return render(request, 'voluntarios/voluntario_form.html', {'form': form})

    def post(self, request):
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voluntario_list')
        return render(request, 'voluntarios/voluntario_form.html', {'form': form})

# Editar voluntario
class VoluntarioUpdateView(View):
    def get(self, request, pk):
        voluntario = get_object_or_404(Voluntario, pk=pk)  # Recupera el registro existente
        form = VoluntarioForm(instance=voluntario)         # Prellena el formulario
        return render(request, 'voluntarios/voluntario_form.html', {'form': form})

    def post(self, request, pk):
        voluntario = get_object_or_404(Voluntario, pk=pk)
        form = VoluntarioForm(request.POST, instance=voluntario)  # Guarda cambios
        if form.is_valid():
            form.save()
            return redirect('voluntario_list')
        return render(request, 'voluntarios/voluntario_form.html', {'form': form})

# Lista de eventos
class EventoListView(View):
    def get(self, request):
        eventos = Evento.objects.all()  # Recupera todos los eventos
        return render(request, 'voluntarios/evento_list.html', {'eventos': eventos})

# Delete Voluntario
class VoluntarioDeleteView(DeleteView):
    model = Voluntario
    template_name = 'voluntarios/voluntario_confirm_delete.html'
    success_url = reverse_lazy('voluntario_list')

# Delete Evento
class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'voluntarios/evento_confirm_delete.html'
    success_url = reverse_lazy('evento_list')
    
# Crear Evento
class EventoCreateView(View):
    def get(self, request):
        form = EventoForm()
        return render(request, 'voluntarios/evento_form.html', {'form': form})

    def post(self, request):
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
        return render(request, 'voluntarios/evento_form.html', {'form': form})

# Editar Evento
class EventoUpdateView(View):
    def get(self, request, pk):
        evento = get_object_or_404(Evento, pk=pk)       # Recupera el evento existente
        form = EventoForm(instance=evento)             # Prellena el formulario
        return render(request, 'voluntarios/evento_form.html', {'form': form})

    def post(self, request, pk):
        evento = get_object_or_404(Evento, pk=pk)
        form = EventoForm(request.POST, instance=evento)  # Guarda cambios
        if form.is_valid():
            form.save()
            return redirect('evento_list')
        return render(request, 'voluntarios/evento_form.html', {'form': form})