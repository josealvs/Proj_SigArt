from django.urls import path
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls  # Registra as rotas automaticamente
