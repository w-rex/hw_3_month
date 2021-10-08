from django.urls import path
from .views import *

urlpatterns = [
    path("", blog_view),
    path("<int:id>", detail_post),
    path("hello", hello),
    path("num", random_number),
    path('form', form),
    path("create", create_blog)
]