from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_countries.fields import CountryField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(blank=True, verbose_name='图片')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='上传时间')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    country = CountryField(blank_label='(哪个国家)', multiple=True, default='US', verbose_name='国家')
    content = models.TextField(verbose_name='内容')

    class Meta:
        db_table = 'blog_post'
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', verbose_name='上传图片')

    class Meta:
        db_table = 'blog_postimage'
        verbose_name = '博客图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.post.title
