from django.urls import path
from .views import *
urlpatterns = [
    path('',createprofile,name='create'),
    # path('sellcreate/',CreateSell.as_view(),name='sellcreate'),
    path('sellcreate/',createsell,name='sellcreate'),
    path('logout/',handlelogout,name='logout'),
]
