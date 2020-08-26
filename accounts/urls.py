from django.urls import path, include
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='accounts-login'),
    path('register/', views.RegisterView.as_view(), name='accounts-register'),
    path('logout/', views.LogOutView.as_view(), name='accounts-logout'),
]
