from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Adicionando a funcionalidade de busca por título e descrição
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
