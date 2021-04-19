from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('myApp/', include('myApp.urls')),
    path('admin/', admin.site.urls),
    path('', include('single_pages.urls')),
]
