from django.contrib import admin
from django.urls import path, include

from eventa import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('event.urls')),
    path('api/', include('category.urls')),
    path('api/', include('user.urls')),
    path('api/', include('ticket.urls')),
]
