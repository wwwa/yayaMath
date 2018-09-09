from django.db import models


# Create your models here.

class BookMall(models.Model):
    """

    """

    title = models.CharField('名字', max_length=64, null=True, blank=True)
    content = models.CharField('内容', max_length=64, null=True, blank=True)
    description = models.CharField('描述', max_length=64, null=True, blank=True)
    add_time = models.DateTimeField('添加时间', auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.title} ({self.content})'


class Tag(models.Model):
    """
    书籍标签
    """

    name = models.CharField('名字', max_length=64, null=True, blank=True)
    value = models.CharField('值', max_length=64, null=True, blank=True)
