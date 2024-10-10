from django.contrib import admin
from django.urls import path, include

from tasks.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('', HomeView.as_view(), name='home'),
]
