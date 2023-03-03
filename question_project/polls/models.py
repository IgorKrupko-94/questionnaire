from django.db import models


class Question(models.Model):
    question_text = models.CharField(
        'Вопрос',
        max_length=200
    )
    pub_date = models.DateTimeField(
        'Дата публикации'
    )


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(
        'Ответ',
        max_length=200
    )
    votes = models.IntegerField(
        'Балл',
        default=0
    )
