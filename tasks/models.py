from django.db import models
from django.utils import timezone
from datetime import datetime

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Nova'),
        ('in_progress', 'Em andamento'),
        ('completed', 'Concluída'),
        ('canceled', 'Cancelada'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250, blank=True, null=True)
    due_date = models.DateField(null=True)
    completion_date = models.DateField(blank=True, null=True)  # Data de Conclusão
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return self.title
