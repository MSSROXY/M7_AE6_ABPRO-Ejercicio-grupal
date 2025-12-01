from django import forms
from .models import Voluntario, Evento

# Formulario para Voluntario
class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nombre', 'email', 'telefono']

# Formulario para Evento
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha', 'voluntarios']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'voluntarios': forms.CheckboxSelectMultiple(),
        }
