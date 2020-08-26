from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.throttling import UserRateThrottle
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from throttle.decorators import throttle

from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import login, authenticate, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from accounts import serializers

class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'accounts/auth/login.html'

    def get(self, request, format=None):
        return Response()

    def post(self, request, format=None):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            return redirect('home:home')
        else:
            raise Http404

class LogOutView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'accounts/auth/logout.html'

    def get(self, request, format=None):
        logout(request)
        return Response()

class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'accounts/auth/register.html'

    def get(self, request, format=None):
        return Response()

    def post(self, request, format=None):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            raise ValidationError('Parolele nu se potrivesc!')

        user = User(username=username, email=email)
        user.set_password(password1)
        user.save()
        return redirect('accounts:accounts-login')
