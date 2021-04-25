from django.db import models
from django.contrib.auth.models import User
import os


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_test = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 작성자 추가
    # CASCADE : 종속의 의미. 작성자가 지워지면 관련글도 삭제됨.
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # SET_NULL : 작성자가 삭제되었을 때 작성자는 NONE 으로 출력됨. null=True 처리 필수
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # 카테고리 추가
    # blank 설정을 통해 필수로 등록해야하는지 체크
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
