
from django.contrib import admin
from django.urls import path, include
import polaris.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(polaris.urls)),
]
