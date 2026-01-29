from django.urls import path
from .views import ScriptViewSet

urlpatterns = [
    path('scripts/', ScriptViewSet.as_view({'post': 'create'}), name='executar-script'),
]
