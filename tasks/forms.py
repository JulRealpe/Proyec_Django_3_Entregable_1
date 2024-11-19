from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    # Definir las opciones de tipo de material
    MATERIAL_CHOICES = [
        ('electrico', 'Sistema Eléctrico'),
        ('comunicaciones', 'Comunicaciones'),
        ('conductos', 'Conductos'),
        ('otros', 'Otros'),
    ]
    
    # Añadir el campo para el tipo de material
    material_type = forms.ChoiceField(choices=MATERIAL_CHOICES, label='Tipo de Material')

    class Meta:
        model = Task
        fields = ['title', 'description', 'important', 'material_type']
