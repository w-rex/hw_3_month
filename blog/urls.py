from django.urls import path, include
from .views import *

urlpatterns = [
    path("", blog_view),
    path("<int:id>", detail_post),
    path("<int:id>/change", change_view),
    path("hello", hello),
    path("num", random_number),
    path('form', form),
    path("create", create_blog)
]