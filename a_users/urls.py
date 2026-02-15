from django.urls import path
from .views import profile_view, profile_edit, settings_view

urlpatterns = [
    path('', profile_view),
    path('edit/', profile_edit, name='profile_edit'),
    path('settings/', settings_view, name='settings'),
]