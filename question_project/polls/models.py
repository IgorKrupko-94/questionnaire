from django.db import models


class Question(models.Model):
    question_text = models.CharField(
        'Вопрос',
        max_length=200,
        help_text='Задайте вопрос'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question_text[:40]


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices',
        verbose_name='Вопрос',
        help_text='Выберите вопрос'
    )
    choice_text = models.CharField(
        'Ответ',
        max_length=200,
        help_text='Введите вариант ответа'
    )
    votes = models.IntegerField(
        'Балл',
        default=0,
        help_text='Введите количество баллов'
    )

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'

    def __str__(self):
        return self.choice_text[:40]
