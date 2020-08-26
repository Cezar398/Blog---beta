from rest_framework import serializers

from posts import models

class NewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['title', 'description', 'thumb_image']
