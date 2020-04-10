from django.urls import path
from contas.views import Profile

urlpatterns = [
    path('users', Profile.as_view()),
]