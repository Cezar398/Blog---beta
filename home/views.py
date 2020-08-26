from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from django.shortcuts import render
from django.utils.html import escape

from posts import models as post_models
from home import models as home_models

class HomeListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home/index.html'

    def get(self, request, format=None):
        posts = post_models.Post.objects.all().filter(is_active=True).order_by('-id')[:10]
        home = home_models.Index.objects.get(pk=1)
        return Response({'posts': posts, 'index':home})
