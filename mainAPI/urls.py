from django.urls import path,re_path
from .views import AllMenuItems,SingleMenuItem
urlpatterns=[
    #class bassed mapping
    path("items",AllMenuItems.as_view()),
    path('items/<int:pk>',SingleMenuItem.as_view())
    #function based mapping
    # path("items",AllMenuItems),
    # path('items/<int:pk>',SingleMenuItem)
]