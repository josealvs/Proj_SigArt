from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Nova'),
        ('in_progress', 'Em andamento'),
        ('finished', 'Finalizada'),
        ('canceled', 'Cancelada'),
    ]


    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250, blank=True, null=True)
    due_date = models.DateTimeField(null=True, blank=True)  
    completion_data = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')


    def __str__(self):
        return self.title

