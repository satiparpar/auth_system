from django.urls import path

from .views import home, register, profile, is_superuser_check, is_staff_check, is_silvern_check, \
    is_golden_check, login, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('check_superuser/', is_superuser_check, name='is_superuser_check'),
    path('is_staff/', is_staff_check, name='is_staff_check'),
    path('is_golden/', is_golden_check, name='is_golden_user'),
    path('is_silvern/', is_silvern_check, name='is_silvern_check'),
]

