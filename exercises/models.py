from django.db import models


# Create your models here.

class ExerciseBook(models.Model):
    """

    """

    name = models.CharField('练习簿', max_length=64, null=True, blank=True)
    example = models.CharField('样例', max_length=64, null=True, blank=True)
    description = models.CharField('描述', max_length=64, null=True, blank=True)
    order = models.IntegerField('顺序', default=1, null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.name} ({self.description})'


class ExerciseCard(models.Model):
    """
    练习题卡
    """

    name = models.CharField('题卡', max_length=64, null=True, blank=True)
    description = models.CharField('描述', max_length=64, null=True, blank=True)
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
    description = models.CharField('描述', max_length=64, null=True, blank=True)

    exercise_card = models.ForeignKey(ExerciseCard, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.id}: {self.question} ({self.description})'
