from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=True, null=True, default='Title...')
    description = models.CharField(max_length=150, blank=True, null=True, default='Description...')
    content = models.TextField(blank=True, null=True, default='None')
    thumb_image = models.ImageField(blank=True, default='/posts/default.jpg', upload_to='media/posts/')
    post_date = models.DateTimeField(auto_now_add=True)

    is_important = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} by {self.author}'
