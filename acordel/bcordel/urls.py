from django.urls import path
from .views import CordelView

urlpatterns = [
    path('', CordelView, name="cordel-view"),
]