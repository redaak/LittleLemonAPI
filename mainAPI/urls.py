from django.urls import path,re_path
from .views import AllMenuItems,SingleMenuItem
urlpatterns=[
    path("items",AllMenuItems.as_view()),
    path('items/<int:pk>',SingleMenuItem.as_view())
]