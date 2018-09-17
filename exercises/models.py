from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class ExerciseBook(models.Model):
    """

    """

    name = models.CharField('练习簿', max_length=64, null=True, blank=True)
    example = models.CharField('样例', default='', max_length=64, null=True, blank=True)
    description = models.CharField('描述', default='', max_length=64, null=True, blank=True)
    order = models.IntegerField('顺序', default=1, null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.name} ({self.description})'


class ExerciseCard(models.Model):
    """
    练习题卡
    """

    name = models.CharField('题卡', max_length=64, null=True, blank=True)
    description = models.CharField('描述', default='', max_length=64, null=True, blank=True)
    order = models.IntegerField('顺序', default=1, null=True, blank=True)

    exercise_book = models.ForeignKey(ExerciseBook, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.id}: {self.name} ({self.description})'

    @property
    def count(self):
        """
        当前题卡题量
        :return:
        """
        return self.exercise_set.count()


class Exercise(models.Model):
    """
    练习题卡
    """

    question = models.CharField('问题', max_length=64, null=True, blank=True)
    answer = models.CharField('答案', max_length=64, null=True, blank=True)
    order = models.IntegerField('顺序', default=1, null=True, blank=True)
    description = models.CharField('描述', default='', max_length=64, null=True, blank=True)

    exercise_card = models.ForeignKey(ExerciseCard, on_delete=models.DO_NOTHING)

    def __str__(self):
        s = f'{self.id}: {self.question} = {self.answer}'
        return s


class ExerciseCardRecord(models.Model):
    """
    题卡记录
    """

    add_time = models.DateTimeField('添加时间', auto_now=True)
    exercise_card = models.ForeignKey(ExerciseCard, on_delete=models.DO_NOTHING)
    total_time = models.IntegerField('总计时间', default=0, null=True, blank=True)
    right_ratio = models.IntegerField('正确率', default=0, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        total_seconds = self.total_time / 1000
        return f'{self.exercise_card} cost:{total_seconds}s'

    @property
    def add_day(self):
        return timezone.localtime(self.add_time).strftime('%m-%d %H:%M')

    @property
    def total_seconds(self):
        return self.total_time / 1000


class Record(models.Model):
    """
    答题记录
    """

    add_time = models.DateTimeField('添加时间', auto_now=True)
    exercise_card = models.ForeignKey(ExerciseCard, on_delete=models.DO_NOTHING)
    exercise = models.ForeignKey(Exercise, on_delete=models.DO_NOTHING)
    delta_time = models.IntegerField('花费时间', default=1000, null=True, blank=True)
    is_right = models.BooleanField('是否正确', default=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    user_answer = models.CharField('用户答案', max_length=64, null=True, blank=True)
    exercise_card_record = models.ForeignKey(ExerciseCardRecord, on_delete=models.DO_NOTHING, null=True, blank=True)
