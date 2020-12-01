from django import forms

from . models import Entrada, Formulario


class EntradaForm(forms.ModelForm):
    titulo = forms.CharField(label='Titulo',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    tema = forms.CharField(label='Descripción', max_length=5000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Entrada
        fields = ('titulo', 'tema')


class FormularioForm(forms.ModelForm):
    
    edad = forms.CharField(label='Ingrese su Edad', widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    cursos = forms.CharField(label= 'Ingrese su Curso', widget= forms.TextInput (
        attrs={
            'class':'form-control'
        }
    ))

    correo = forms.EmailField(label='Ingrese su Correo electronico',max_length=60, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    problema = forms.CharField(label= 'Indique su problema', widget= forms.TextInput (
        attrs={
            'class':'form-control'
        }
    ))

    reporte = forms.CharField(label= '¿Le informó a un adulto?', widget= forms.TextInput (
        attrs={
            'class':'form-control'
        }
    ))

    detalle = forms.CharField(label='Describa aquí su problema', max_length=5000, widget=forms.Textarea (
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Formulario
        fields = ('cursos', 'problema', 'correo', 'edad', 'reporte', 'detalle')