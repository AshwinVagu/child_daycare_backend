from django.urls import path
from .views import user_login,register_user, get_Registered_User

urlpatterns = [
    path('login/', user_login, name='json_login'),
    path('register/', register_user, name='register_user'),
    path('getRegisteredUser/', get_Registered_User, name='get_registered_user'),
]


