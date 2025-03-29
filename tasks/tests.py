from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Task

class TaskAPITestCase(APITestCase):

    def setUp(self):
        """Configuração inicial: cria uma tarefa de exemplo"""
        self.task = Task.objects.create(
            title="Tarefa Teste",
            description="Descrição da tarefa",
            due_date="2025-04-01",
            status="new"
        )
        self.list_url = reverse('task-list')  # URL para listar tarefas

    def test_list_tasks(self):
        """Teste para listar tarefas"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        """Teste para criar uma nova tarefa"""
        data = {
            "title": "Nova Tarefa",
            "description": "Criando uma nova tarefa",
            "due_date": "2025-04-10",
            "status": "new"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_retrieve_task(self):
        """Teste para visualizar uma tarefa específica"""
        url = reverse('task-detail', kwargs={'pk': self.task.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        """Teste para atualizar uma tarefa existente"""
        url = reverse('task-detail', kwargs={'pk': self.task.id})
        data = {"title": "Tarefa Atualizada", "status": "in_progress"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Tarefa Atualizada")

    def test_delete_task(self):
        """Teste para excluir uma tarefa"""
        url = reverse('task-detail', kwargs={'pk': self.task.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_create_task_missing_field(self):
        """Teste de exceção: criar tarefa sem título (campo obrigatório)"""
        data = {"description": "Sem título", "due_date": "2025-04-10"}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
