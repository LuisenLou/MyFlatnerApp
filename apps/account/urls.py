from django.urls import path
from .views import *

urlpatterns = [
    path('List', ListAccountView.as_view())
]