from django.urls import path,re_path
from .views import AllMenuItems
urlpatterns=[
    path("items",AllMenuItems.as_view())
]