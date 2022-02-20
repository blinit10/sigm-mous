from django import forms
from .models import *

#se crea un formulario que hereda de modelform es decir
# un formulario que esta asociado a un modelo d ela base de datos
class EstacionForm(forms.ModelForm):
    # se definen los metadatos del formulario
    class Meta:
        # se define el modelo asociado al formulario
        model = Estacion
        # se definen los campos que tendra este formulario, en este caso serian __all__ (todos)
        # los campos que presenta el modelo Estacion
        fields = '__all__'

class RVMForm(forms.ModelForm):
    fecha_hora = forms.DateTimeField()
    class Meta:
        model = ReporteVariableMeteorologica
        fields = '__all__'

class IOVMGForm(forms.ModelForm):
    class Meta:
        model = InformeVariableMeteorologicaGeneral
        fields = '__all__'

class IOVMPForm(forms.ModelForm):
    class Meta:
        model = InformeOficialVariableMeteorologicaPronvincial
        fields = '__all__'

class PMPForm(forms.ModelForm):
    class Meta:
        model = ParteMeteorologicoProvincial
        fields = '__all__'

class PMGForm(forms.ModelForm):
    class Meta:
        model = ParteMeteorologicoGeneral
        fields = '__all__'