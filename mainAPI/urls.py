from django.urls import path,re_path
from .views import AllMenuItems,SingleMenuItem,menu,secret
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    #class bassed mapping
    # path("items",AllMenuItems.as_view()),
    # path('items/<int:pk>',SingleMenuItem.as_view())
    #function based mapping
    path("items",AllMenuItems),
    path('items/<int:pk>',SingleMenuItem),
    path('menu',menu),
    path('api-toke-auth',view=obtain_auth_token)

]