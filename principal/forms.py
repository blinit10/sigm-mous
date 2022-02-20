from django import forms
from .models import *

class EstacionForm(forms.ModelForm):
    class Meta:
        model = Estacion
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