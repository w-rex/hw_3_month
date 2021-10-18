from django.urls import path
from .views import *

urlpatterns = [
    path("signup", register_view),
    path("login/", login_views),
    path('logout/', logout_views),
]