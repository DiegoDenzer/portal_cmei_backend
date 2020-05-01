
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import refresh_jwt_token

from portal_fotos.apis.album_view_set import AlbumViewSet
from portal_fotos.apis.aluno_view_set import AlunoViewSet
from portal_fotos.apis.educador_view_set import EducadorViewSet
from portal_fotos.apis.turma_view_set import TurmaViewSet

router = routers.DefaultRouter()
router.register(r'turma', TurmaViewSet, basename='turma')
router.register(r'aluno', AlunoViewSet, basename='aluno')
router.register(r'educador', EducadorViewSet, basename='educador')
router.register(r'album', AlbumViewSet, basename='album')
# router.register(r'foto', FotoViewSet, basename='foto')


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS)
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),
    path('api/', include(router.urls)),
]
