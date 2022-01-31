from django import forms

from catalog.models import Genero,  Paciente, Evaluacion, Medico, Especialidad



# Se encuentran todos las cajas de texto q se usa para realizar un registro o actuliacion
# correspondiente a la tabla de base de datos
class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['genero', 'activo']
        widgets = {
            'genero': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Descripción de genero'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['especialidad', 'activo']
        widgets = {
            'especialidad': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Especialidad del médico'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['genero', 'cedula', 'nombre', 'apellido',
                  'fecha_nacimiento', 'email', 'telefono', 'celular', 'activo']

        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Escriba su número de cedula', 'size': '11'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Escriba sus nombres'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Escriba sus apellidos'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Escriba la fecha nacimiento'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Escriba su correo electronico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Escriba su numero de teléfono', 'size': '9'}),
            'celular': forms.TextInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Escriba su numero de celular', 'size': '10'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].widget.attrs['placeholder'] = 'dd/mm/aaaa '
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['genero'].empty_label = "Seleccione el Genero"

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Paciente.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "El email ya está registrado, prueba con otro.")
        return email


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['user', 'genero', 'cedula', 'nombre',
                  'apellido', 'email', 'especialidad', 'activo']

        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Escriba su número de cedula', 'size': '11'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Escriba sus nombres'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Escriba sus apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2 ', 'placeholder': 'Escriba su correo electronico'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['genero'].empty_label = "Seleccione el Genero"
        self.fields['user'].empty_label = "Seleccione el usuario correspondiente"
        self.fields['especialidad'].empty_label = "Seleccione  especialidad médica"

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Medico.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "El email ya está registrado, prueba con otro.")
        return email

 # =============================== Foto===========================


class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['paciente', 'imagen']
        labels = {
            'paciente': "Nombre del paciente",
            'imagen': "Imagen del paciente",
        }
        widget = {'paciente': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['paciente'].empty_label = "Seleccione el paciente"
