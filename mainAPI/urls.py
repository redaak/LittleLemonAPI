from django.urls import path,re_path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    #class bassed mapping
    # path("items",AllMenuItems.as_view()),
    # path('items/<int:pk>',SingleMenuItem.as_view())
    #function based mapping
    path("items",AllMenuItems),
    path('items/<int:pk>',SingleMenuItem),
    path('menu',menu),
    path('api-toke-auth',view=obtain_auth_token),
    path('manager',manager_view),
    path('throttel_check',throtteling_check),

]

#jhon deo token: cf8ad6f9a424364754bb28ccc2005c9a99256439
#jimmu toke: f47a4b4ea5ebaa45cb41396b83aa4ad0e56e6305