from django.contrib import admin

# Register your models here.
from exercises.models import Exercise, ExerciseBook, ExerciseCard


class ExerciseBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


class ExerciseCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'exercise_book', 'description']


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'answer', 'exercise_card', 'description']
    list_editable = ['question', 'answer', 'exercise_card']


admin.site.register(ExerciseBook, ExerciseBookAdmin)
admin.site.register(ExerciseCard, ExerciseCardAdmin)
admin.site.register(Exercise, ExerciseAdmin)
