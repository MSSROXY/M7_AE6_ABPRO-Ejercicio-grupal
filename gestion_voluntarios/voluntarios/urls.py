from django.urls import path
from .views import (
    HomeView,
    VoluntarioListView,
    VoluntarioCreateView,
    VoluntarioUpdateView,
    VoluntarioDeleteView,
    EventoListView,
    EventoCreateView,
    EventoUpdateView,
    EventoDeleteView
)

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),

    # CRUD Voluntarios
    path('voluntarios/', VoluntarioListView.as_view(), name='voluntario_list'),
    path('voluntarios/nuevo/', VoluntarioCreateView.as_view(), name='voluntario_create'),
    path('voluntarios/editar/<int:pk>/', VoluntarioUpdateView.as_view(), name='voluntario_edit'),
    path('voluntarios/eliminar/<int:pk>/', VoluntarioDeleteView.as_view(), name='voluntario_delete'),

    # CRUD Eventos
    path('eventos/', EventoListView.as_view(), name='evento_list'),
    path('eventos/nuevo/', EventoCreateView.as_view(), name='evento_create'),
    path('eventos/editar/<int:pk>/', EventoUpdateView.as_view(), name='evento_edit'),
    path('eventos/eliminar/<int:pk>/', EventoDeleteView.as_view(), name='evento_delete'),
]
