from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView  # Adicionando para redirecionamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('', RedirectView.as_view(url='/api/')),  # Redireciona a raiz para /api/
]
