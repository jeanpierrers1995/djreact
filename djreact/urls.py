from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rest framework
    path('api-auth/', include('rest_framework.urls')),

    # Rest auth
    path('rest-auth/', include('rest_auth.urls')),

    # rest alluth
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    # Traer api
    path('api/', include('articles.api.urls'))

]
