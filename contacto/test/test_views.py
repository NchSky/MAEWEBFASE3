from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Formulario, Entrada

class EntradaListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_entrada = 13

        for entrada_id in range(number_of_entrada):
            Entrada.objects.create(
                titulo=f'Accion {entrada_id}',
                tema=f'Prueba {entrada_id}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/contacto/entrada/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('entrada'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('entrada'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'entrada/entrada_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('entrada'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['entrada_list']) == 10)

    def test_lists_all_entrada(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('entrada')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['entrada_list']) == 3)

class FormularioListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_formulario = 13

        for formulario_id in range(number_of_formulario):
            Formulario.objects.create(
                edad=f'Accion {formulario_id}',
                cursos=f'Prueba {formulario_id}',
                correo=f'Prueba1 {formulario_id}',
                problema=f'Prueba2 {formulario_id}',
                reporte=f'Prueba3 {formulario_id}',
                detalle=f'Prueba4 {formulario_id}',

            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/contacto/formulario/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('formulario'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('formulaerio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'entrada/entrada_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('formulario'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['formulario_list']) == 10)

    def test_lists_all_entrada(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('formulario')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['formulario_list']) == 3)
        
    """def test_pagination_is_ten(self):
        response = self.client.get(reverse('movies'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['movie_list']) == 10)

    def test_lists_all_movies(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('movies')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['movie_list']) == 3)

        """