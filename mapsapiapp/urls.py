from django.urls import path,include
from .views import Users_Create_endpoint,password_reset
from . import views


urlpatterns = [
    path('',Users_Create_endpoint.as_view()),
    path('pass',password_reset),
     path('accounts/', include('django.contrib.auth.urls')),
]
