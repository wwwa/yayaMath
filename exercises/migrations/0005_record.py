# Generated by Django 2.0 on 2018-09-14 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0004_auto_20180908_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delta_time', models.IntegerField(blank=True, default=1000, null=True, verbose_name='花费时间')),
                ('is_rigtht', models.BooleanField(default=True, verbose_name='是否正确')),
                ('user_answer', models.CharField(blank=True, max_length=64, null=True, verbose_name='用户答案')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exercises.Exercise')),
                ('exercise_card', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exercises.ExerciseCard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
