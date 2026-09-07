from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Proyecto, Tarea


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = Usuario
        # 🚀 Se eliminan 'password1' y 'password2' de aquí porque UserCreationForm los maneja internamente
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("¡Este correo ya está registrado!")
        return email


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'estado', 'proyecto']

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)
        if usuario:
            # Filtra el desplegable para que solo aparezcan los proyectos del usuario logueado
            self.fields['proyecto'].queryset = Proyecto.objects.filter(usuario=usuario)
