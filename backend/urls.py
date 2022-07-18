from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    path('member', include('backend.member.urls', namespace='member')),
    path('admin/', admin.site.urls),
]
