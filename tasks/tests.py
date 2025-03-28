from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import status
from rest_framework import status
from .models import Task

class TaskAPITestCase(APITestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title = "Primeira Tarefa",
            description = "Tarefa Teste",
            due_date = "2025-04-01",
            status = "new",
        )
        
# Create your tests here.
