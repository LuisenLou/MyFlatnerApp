from django.urls import path
from .views import *

urlpatterns = [
    path('List', ListFlatView.as_view())
]