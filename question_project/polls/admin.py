from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    search_fields = ('question_text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    list_editable = ('question',)
    search_fields = ('choice_text',)
    list_filter = ('question',)
    empty_value_display = '-пусто-'


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
