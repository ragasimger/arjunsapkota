from django.urls import path, include

allpatterns = [
    path('blog/', include('apps.blog.urls')),
    path('info/', include('apps.main.urls')),
]