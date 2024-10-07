from django.urls import path
from .views import log_user_agent

urlpatterns = [
    path('', log_user_agent, name='log_user_agent'),
]
