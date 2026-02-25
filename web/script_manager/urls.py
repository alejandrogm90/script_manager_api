from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import index, ScriptViewList, ScriptViewSet

# Custom 404 error view
#handler404 = '.views.error_404'
# Custom 500 error view
#handler500 = '.views.error_500'

router = DefaultRouter()
router.register(r'launch', ScriptViewSet, basename='script-launch')
router.register(r'list', ScriptViewList, basename='script-list')

urlpatterns = [
    path('index/', index, name='index'),  # Ruta para la página de índice
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
