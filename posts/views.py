from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.throttling import UserRateThrottle
from rest_framework import permissions

from throttle.decorators import throttle

from django.shortcuts import render, redirect
from django.http import Http404
from django.utils.html import escape
from django.utils.decorators import method_decorator

from posts import models as post_models
from posts import serializers
from home import models as home_models

class PostDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'posts/post-detail.html'
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk, format=None):
        post = post_models.Post.objects.get(pk=pk)
        index = home_models.Index.objects.get(pk=1)
        return Response({'post': post, 'index': index})

class PostCreateView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'posts/post-create.html'

    def get(self, request, format=None):
        serializer = serializers.NewPostSerializer()
        return Response({'serializer': serializer})

    @method_decorator(throttle(zone='default'))
    def post(self, request, format=None):
        serializer = serializers.NewPostSerializer(data=request.data)
        content = request.POST.get('content')

        if serializer.is_valid():
            serializer.save(author=self.request.user, content=content)
            return redirect('home:home')
        raise Http404

class PostUpdateView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'posts/post-update.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk, format=None):
        post = post_models.Post.objects.get(pk=pk)
        serializer = serializers.NewPostSerializer(instance=post)
        return Response({'serializer': serializer, 'content': post.content})

    def post(self, request, pk, format=None):
        post = post_models.Post.objects.get(pk=pk)
        serializer = serializers.NewPostSerializer(data=request.data, instance=post)
        content = request.POST.get('content')
        if serializer.is_valid():
            serializer.save(content=content)
            return redirect('posts:post-detail', pk=pk)
        raise Http404
