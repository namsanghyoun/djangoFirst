from django.db import models
from django.contrib.auth.models import User
import os


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

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

    # 카테고리기능 추가
    # null, blank 설정을 통해 공백입력, 필수입력 조건 설정
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    # 태그기능 추가
    # ManyToManyField는 기본적으로 null=True가 설정되어 있음.
    # on_delete 설정을 하지 않아도 삭제시 알아서 빈칸으로 처리됨.
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
