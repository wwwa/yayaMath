from django.contrib import admin

# Register your models here.
from exercises.models import Exercise, ExerciseBook, ExerciseCard, ExerciseCardRecord, Record


class ExerciseBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


class ExerciseCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'exercise_book', 'description']


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'answer', 'exercise_card', 'description']
    list_editable = ['question', 'answer', 'exercise_card']
    search_fields = [
        # 'description',
        # 'question',
        'answer',
    ]


class RecordAdmin(admin.ModelAdmin):
    """

    """
    list_display = ('id', 'user', 'exercise', 'user_answer',
                    'is_right', 'delta_time', 'exercise_card_record', 'add_time')


class ExerciseCardRecordAdmin(admin.ModelAdmin):
    """

    """
    list_display = ('id', 'user', 'total_time', 'exercise_card', 'right_ratio', 'add_time')


admin.site.register(ExerciseBook, ExerciseBookAdmin)
admin.site.register(ExerciseCard, ExerciseCardAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(ExerciseCardRecord, ExerciseCardRecordAdmin)
