from django.urls import path
from .views import index, ScriptViewSet

urlpatterns = [
    path('', index, name='index'),  # Ruta para la página de índice
    path('scripts/', ScriptViewSet.as_view({'post': 'create'}), name='executar-script'),
]
