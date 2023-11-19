from django.db import models


class Task(models.Model):
    """Класс для задания"""
    
    
    SUBJECT_CHOICES = [
        ('Информатика', 'Информатика'),
        ('Математика', 'Математика'),
        ('Русский язык', 'Русский язык'),
        ('Английский язык', 'Английский язык'),
        ('Обществознание', 'Обществознание'),
        ('География', 'География'),
        ('Физика', 'Физика'),
        ('Химия', 'Химия'),
        ('Биология', 'Биология'),
        ('Литература', 'Литература'),
        ('История', 'История'),
        ('Не задано', 'Не задано'),
    ]

    subject_type = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='Не задано')
    task_number = models.IntegerField()
    title = models.CharField(max_length=255)
    task_condition = models.TextField()
    points = models.IntegerField()

    def __str__(self):
        return str(self.subject_type) if hasattr(self, 'subject_type') else "No subject"
