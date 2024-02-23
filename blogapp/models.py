from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    avatar = models.ImageField(upload_to="images/")
    bio = models.CharField(max_length=150)

    def __str__(self):
        return self.username


class Tags(models.Model):
    tag = models.CharField(verbose_name="Tag", max_length=222)

    class Meta:
        verbose_name_plural = 'Tags'
        verbose_name = 'Tag'

    def __str__(self):
        return self.tag


class Category(models.Model):
    category_name = models.CharField(verbose_name="Category name", max_length=222)
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    def __str__(self):
        return self.category_name


class BlogModel(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Title', max_length=222)
    image = models.ImageField(upload_to='images/')
    tag = models.ManyToManyField(Tags, verbose_name='Tag')
    paragraph = models.TextField(verbose_name='Paragraph')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    def __str__(self):
        return self.autor.username

    def get_absolute_url(self):
        return reverse('blog_single', kwargs={"pk": str(self.pk)})


class MessageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    message = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name= "replies")
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.user.username}:{self.message[:20]} --> {self.parent}"

    @property
    def children(self):
        return MessageModel.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent in None:
            return True
        return False

