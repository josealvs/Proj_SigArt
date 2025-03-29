from django.core.management.base import BaseCommand
from tasks.models import Task
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Popula o banco de dados com 15 tarefas aleatórias'

    def handle(self, *args, **kwargs):
        statuses = ['new', 'in_progress', 'completed', 'canceled']
        Task.objects.all().delete()  # Limpa as tarefas antes de criar novas

        for i in range(15):
            Task.objects.create(
                title=f'Tarefa {i+1}',
                description=f'Descrição da tarefa {i+1}',
                due_date=datetime.today().date() + timedelta(days=random.randint(1, 30)),
                completion_date=None if random.choice([True, False]) else datetime.today().date(),
                status=random.choice(statuses)
            )

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com 15 tarefas!'))
