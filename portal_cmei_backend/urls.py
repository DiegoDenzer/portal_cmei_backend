
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS)
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),
]
