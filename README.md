# Gestión de Voluntarios – Proyecto Django

## Descripción
Aplicación web para registrar voluntarios, crear y gestionar eventos comunitarios, y mantener la información actualizada. Permite crear, listar, editar y eliminar registros de **voluntarios** y **eventos** mediante un CRUD completo.

## Tecnologías
- Python 3.14  
- Django 5.x  
- Bootstrap 5  
- SQLite (por defecto, se puede cambiar a otra base de datos)

## Instalación

1. Clonar el repositorio:  
```bash
git clone <URL_DEL_REPO>
cd gestion_voluntarios
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```
3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Aplicar migraciones:
```bash
python manage.py migrate
```

5. Crear superusuario (opcional):
```bash
python manage.py createsuperuser
```

6. Ejecutar el servidor:
```bash
python manage.py runserver
```

### Uso

- Acceder al Home: http://127.0.0.1:8000/
- Navegar por el navbar para listar, crear, editar o eliminar voluntarios y eventos.
- Formularios con validación y protección CSRF.
