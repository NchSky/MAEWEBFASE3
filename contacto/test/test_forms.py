from django.test import TestCase
from  contacto.forms import FormularioForm, EntradaForm
from  contacto.models import Entrada, Formulario
from django.core.files.uploadedfile import SimpleUploadedFile

class FormularioFormTest(TestCase):
    def test_valid_form(self):
        g = Formulario.objects.create(edad='Prueba1', curso='Prueba' , correo= 'juanito@as.cl',problema='ayurenme' , reporte='nop ', detalle='ama me mie')
        data = {'edad': g.edad, 'curso': g.curso, 'correo': g.correo , 'problema': g.problema , 'reporte': g.reporte , 'detalle': g.detalle}
        form = FormularioForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Formulario.objects.create(edad='', curso='Prueba')
        data = {'edad': g.edad, 'curso': g.curso, 'correo': g.correo , 'problema': g.problema , 'reporte': g.reporte , 'detalle': g.detalle}
        form = FormularioForm(data=data)
        self.assertFalse(form.is_valid())
    
class EntradaFormTest(TestCase):
    def test_valid_form(self):
        g = Entrada.objects.create(titulo='Prueba1', tema='Prueba')
        data = {'titulo': g.titulo, 'tema': g.tema}
        form = EntradaForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        g = Entrada.objects.create(titulo='', tema='Prueba')
        data = {'titulo': g.titulo, 'tema': g.tema}
        form = EntradaForm(data=data)
        self.assertFalse(form.is_valid())