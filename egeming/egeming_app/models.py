from django.db import models


class Task(models.Model):
    """Класс для задания"""

    title = models.CharField(max_length=255)
    description = models.TextField()
    points = models.IntegerField()
    subject_type = models.CharField(max_length=50, default="No subject")

    def __str__(self):
        return str(self.title) if hasattr(self, 'title') else "No Title"
